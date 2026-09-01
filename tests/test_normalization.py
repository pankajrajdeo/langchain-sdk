import unittest
from unittest.mock import patch

from update_docs import (
    Download,
    OUTPUT_ROOT,
    add_fragment_aliases,
    canonical_page_url,
    discover_seed_urls,
    download_one,
    links_from,
    local_path_for,
    normalize_markdown,
    validate_mirror_links,
)


PAGE_URL = "https://docs.langchain.com/oss/python/deepagents/example"


class MarkdownNormalizationTests(unittest.TestCase):
    def normalize(self, text: str) -> str:
        body, warnings = normalize_markdown(text.encode(), PAGE_URL)
        self.assertEqual(warnings, [])
        return body.decode()

    def test_openwiki_paths_use_lowercase_directory(self) -> None:
        path = local_path_for(
            "https://docs.langchain.com/oss/openwiki/automate-updates"
        )
        self.assertEqual(path.parent.name, "openwiki")
        self.assertEqual(path.name, "automate-updates.md")

    @patch("update_docs.request_bytes")
    def test_page_markdown_is_fresher_than_llms_full(self, request) -> None:
        page = "https://docs.langchain.com/langsmith/example"
        request.return_value = (
            b"# Current\n\n## Example agent\n",
            f"{page}.md",
            "text/markdown",
        )
        result = download_one(page, 30, {page: b"# Older aggregate\n"})
        self.assertEqual(result.raw_body, b"# Current\n\n## Example agent\n")
        self.assertEqual(result.content_source, "page-markdown")
        request.assert_called_once_with(f"{page}.md", 30)

    @patch("update_docs.request_bytes", side_effect=RuntimeError("temporary failure"))
    def test_llms_full_is_only_a_download_fallback(self, request) -> None:
        page = "https://docs.langchain.com/langsmith/example"
        result = download_one(page, 30, {page: b"# Aggregate fallback\n"})
        self.assertEqual(result.raw_body, b"# Aggregate fallback\n")
        self.assertEqual(result.content_source, "llms-full.txt-fallback")
        request.assert_called_once_with(f"{page}.md", 30)

    def test_nested_tabs_and_code_groups_become_gfm(self) -> None:
        output = self.normalize(
            '''# Setup
<Tabs>
  <Tab title="pip">
    <CodeGroup>
      ```bash theme={"dark":"example"}
      pip install deepagents
      ```
    </CodeGroup>
  </Tab>
</Tabs>
'''
        )
        self.assertIn("#### pip\n```bash\npip install deepagents\n```", output)
        self.assertNotIn("<Tabs>", output)
        self.assertNotIn("theme=", output)

    def test_generated_embed_source_is_removed_but_invocation_is_preserved(self) -> None:
        output = self.normalize(
            '''# Demo
export const PatternEmbed = ({pattern}) => { return <div>{pattern}</div>; }
<PatternEmbed pattern="sandbox" />
'''
        )
        self.assertNotIn("export const", output)
        self.assertIn("Interactive example", output)
        self.assertIn(PAGE_URL, output)

    def test_generated_undefined_placeholders_are_removed(self) -> None:
        output = self.normalize(
            "# Changelog\n\n"
            "export const sandbox_slug_0 = undefined\n\n"
            "export const snapshot_id_0 = undefined;\n\n"
            'export const prefix_0 = "api.smith"\n\n'
            "export const protocol_0 = false\n\n"
            "Weekly updates.\n"
        )
        self.assertEqual(output, "# Changelog\n\nWeekly updates.\n")

    @patch("update_docs.request_bytes")
    def test_new_python_project_is_discovered_and_mapped_dynamically(self, request) -> None:
        project = "https://docs.langchain.com/oss/python/future-project"
        page = f"{project}/guides/get-started"

        def response(url, timeout):
            self.assertEqual(timeout, 30)
            if url.endswith("/sitemap.xml"):
                return (
                    f"<urlset><url><loc>{page}</loc></url></urlset>".encode(),
                    url,
                    "application/xml",
                )
            if url.endswith("/llms.txt"):
                return f"- [Future project]({project})\n".encode(), url, "text/plain"
            if url.endswith("/llms-full.txt"):
                return b"", url, "text/plain"
            self.fail(f"unexpected discovery URL: {url}")

        request.side_effect = response
        seeds, full_pages, errors = discover_seed_urls(30)

        self.assertEqual(errors, [])
        self.assertEqual(full_pages, {})
        self.assertIn(project, seeds)
        self.assertIn(page, seeds)
        self.assertEqual(canonical_page_url(page), page)
        self.assertEqual(
            local_path_for(page).relative_to(OUTPUT_ROOT).as_posix(),
            "future-project/guides/get-started.md",
        )

    def test_mirrored_links_and_fragments_become_repository_relative(self) -> None:
        mirrored = {
            PAGE_URL,
            "https://docs.langchain.com/oss/python/deepagents/overview",
            "https://docs.langchain.com/oss/python/langchain",
        }
        body, warnings = normalize_markdown(
            b"[section](#setup) [sibling](overview) [root](/oss/python/langchain)\n",
            PAGE_URL,
            mirrored,
        )
        self.assertEqual(warnings, [])
        output = body.decode()
        self.assertIn("[section](#setup)", output)
        self.assertIn("[sibling](overview.md)", output)
        self.assertIn("[root](../langchain/index.md)", output)

    def test_unmirrored_document_link_stays_on_official_site(self) -> None:
        output = self.normalize("[JavaScript docs](/oss/javascript/langchain/overview)\n")
        self.assertIn(
            "https://docs.langchain.com/oss/javascript/langchain/overview",
            output,
        )

    def test_code_that_looks_like_markdown_link_is_not_rewritten(self) -> None:
        output = self.normalize(
            "```javascript\n"
            "const response = toolNameMap[functionName](functionArguments);\n"
            "```\n"
        )
        self.assertIn("toolNameMap[functionName](functionArguments)", output)
        self.assertNotIn("docs.langchain.com/langsmith/functionArguments", output)

    def test_code_that_looks_like_markdown_link_is_not_discovered(self) -> None:
        download = Download(
            page_url="https://docs.langchain.com/langsmith/example",
            raw_body=(
                b"```javascript\n"
                b"toolNameMap[functionName](functionArguments);\n"
                b"```\n"
                b"[Real page](/langsmith/observability)\n"
            ),
        )
        self.assertEqual(
            links_from(download),
            {"https://docs.langchain.com/langsmith/observability"},
        )

    def test_missing_mintlify_fragment_gets_local_anchor_alias(self) -> None:
        source = "https://docs.langchain.com/oss/python/deepagents/example"
        target = "https://docs.langchain.com/oss/python/deepagents/overview"
        completed = {
            source: Download(
                page_url=source,
                body=b"# Example\n[Concepts](overview.md#configuration-file-concepts)\n",
            ),
            target: Download(
                page_url=target,
                body=b"# Overview\n\n## Configuration file\n",
            ),
        }
        self.assertEqual(add_fragment_aliases(completed), 1)
        self.assertIn(
            b'<a id="configuration-file-concepts"></a>',
            completed[target].body,
        )

    def test_encoded_ampersand_fragment_alias_validates(self) -> None:
        source = "https://docs.langchain.com/oss/python/deepagents/example"
        target = "https://docs.langchain.com/oss/python/deepagents/overview"
        completed = {
            source: Download(
                page_url=source,
                body=b"# Example\n[Projects](overview.md#projects-%26-datasets)\n",
            ),
            target: Download(
                page_url=target,
                body=b"# Overview\n\n## Projects & datasets\n",
            ),
        }
        self.assertEqual(add_fragment_aliases(completed), 1)
        self.assertIn(b'<a id="projects-&amp;-datasets"></a>', completed[target].body)
        self.assertEqual(validate_mirror_links(completed), {})

    def test_root_namespace_without_leading_slash_does_not_nest(self) -> None:
        output = self.normalize("[Gateway](langsmith/llm-gateway)\n")
        self.assertIn("https://docs.langchain.com/langsmith/llm-gateway", output)
        self.assertNotIn("/oss/python/deepagents/langsmith/", output)

    def test_html_heading_and_missing_iframe_source_become_native_markdown(self) -> None:
        output = self.normalize(
            '<h2 className="styled">Setup</h2>\n<iframe title="Demo" />\n'
        )
        self.assertIn("## Setup", output)
        self.assertIn(
            f"> **Embedded Content:** Demo — [Open it in the original LangChain documentation]({PAGE_URL}).",
            output,
        )
        self.assertNotIn("<iframe", output)

    def test_file_tree_and_prompt_remain_semantic(self) -> None:
        output = self.normalize(
            '''<Tree>
  <Tree.Folder name="skills">
    <Tree.File name="SKILL.md" />
  </Tree.Folder>
</Tree>
<Prompt description="Turn this fix into a skill.">
Use the current conversation.
</Prompt>
'''
        )
        self.assertIn('- 📁 `skills/`\n  - 📄 `SKILL.md`', output)
        self.assertIn("> **Prompt:** Turn this fix into a skill.", output)
        self.assertIn("Use the current conversation.", output)

    def test_jsx_logo_card_becomes_single_markdown_link(self) -> None:
        output = self.normalize(
            '''<a href="/langsmith/trace-openai" className="grid-item">
  <img className="light" src="/light.svg" alt="" />
  <img className="dark" src="/dark.svg" alt="" />
  <span className="font-semibold">OpenAI</span>
</a>
'''
        )
        self.assertEqual(
            output,
            "- [OpenAI](https://docs.langchain.com/langsmith/trace-openai)\n",
        )

    def test_adjacent_logo_cards_remain_separate_list_items(self) -> None:
        output = self.normalize(
            '''<a href="/one">
  <img src="/one.svg" alt="" />
  <span>One</span>
</a>

<a href="/two">
  <img src="/two.svg" alt="" />
  <span>Two</span>
</a>
'''
        )
        self.assertIn(
            "- [One](https://docs.langchain.com/one)\n\n"
            "- [Two](https://docs.langchain.com/two)",
            output,
        )


if __name__ == "__main__":
    unittest.main()
