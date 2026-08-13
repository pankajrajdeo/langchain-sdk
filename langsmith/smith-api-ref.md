# LangSmith API reference
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/smith-api-ref)
The LangSmith REST API provides programmatic access to LangSmith platform features including tracing, datasets, experiments, annotations, and more.

Browse the full API reference in the **LangSmith REST API** section in the sidebar.

## Authentication

Pass the `X-Api-Key` header with each request. The value should be a valid [LangSmith API key](create-account-api-key.md).

```shell
curl --request GET \
  --url https://api.smith.langchain.com/api/v1/workspaces \
  --header 'X-Api-Key: LANGSMITH_API_KEY'
```

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/smith-api-ref.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
