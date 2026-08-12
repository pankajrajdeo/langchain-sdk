> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Localai reranker integration

> Integrate with the Localai reranker document transformer using LangChain Python.

<Info>
  **`langchain-localai` is a 3rd party integration package for LocalAI. It provides a simple way to use LocalAI services in LangChain.**

  The source code is available on [GitHub](https://github.com/mkhludnev/langchain-localai)
</Info>

This notebook shows how to use [LocalAI Reranker API](https://localai.io/features/reranker/) for document compression and retrieval.

Let's load the `LocalAIRerank` class. In order to use the `LocalAIRerank` class, you need to have the LocalAI service hosted somewhere and configure the reranker. See the documentation at [localai.io/basics/getting\_started/index.html](https://localai.io/basics/getting_started/index.html) and [localai.io/features/reranker/index.html](https://localai.io/features/reranker/index.html).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install -U langchain-localai
```

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
from langchain_localai import LocalAIRerank
from langchain_core.documents import Document

# Set your LocalAI/OpenAI API key as an environment variable for security.
# For example, in your shell: export OPENAI_API_KEY="your-key-here"
reranker = LocalAIRerank(
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    model="bge-reranker-v2-m3",
    openai_api_base="http://localhost:8080",
)
reranked_docs = reranker.compress_documents(
    documents=[
        Document(page_content="Green tea is rich in antioxidants and may improve brain function."),
        Document(page_content="Coffee contains caffeine and can increase alertness."),
        Document(page_content="Black tea has a strong flavor and contains various polyphenols."),
    ],
    query="What are the health benefits of green tea?"
)
```

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/document_transformers/localai_rerank.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
