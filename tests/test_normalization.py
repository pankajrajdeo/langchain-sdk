import unittest

from update_docs import normalize_markdown


PAGE_URL = "https://docs.langchain.com/oss/python/deepagents/example"


class MarkdownNormalizationTests(unittest.TestCase):
    def normalize(self, text: str) -> str:
        body, warnings = normalize_markdown(text.encode(), PAGE_URL)
        self.assertEqual(warnings, [])
        return body.decode()

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

    def test_relative_links_and_fragments_become_official_absolute_urls(self) -> None:
        output = self.normalize(
            "[section](#setup) [sibling](overview) [root](/oss/python/langchain)\n"
        )
        self.assertIn(f"{PAGE_URL}#setup", output)
        self.assertIn("https://docs.langchain.com/oss/python/deepagents/overview", output)
        self.assertIn("https://docs.langchain.com/oss/python/langchain", output)

    def test_root_namespace_without_leading_slash_does_not_nest(self) -> None:
        output = self.normalize("[Gateway](langsmith/llm-gateway)\n")
        self.assertIn("https://docs.langchain.com/langsmith/llm-gateway", output)
        self.assertNotIn("/oss/python/deepagents/langsmith/", output)

    def test_html_heading_and_missing_iframe_source_become_native_markdown(self) -> None:
        output = self.normalize(
            '<h2 className="styled">Setup</h2>\n<iframe title="Demo" />\n'
        )
        self.assertIn("## Setup", output)
        self.assertIn(f"> **Embedded Content:** [Demo]({PAGE_URL})", output)
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
