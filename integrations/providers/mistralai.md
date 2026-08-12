> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MistralAI integrations

> Integrate with MistralAI using LangChain Python.

> [Mistral AI](https://docs.mistral.ai/api/) is a platform that offers hosting for their powerful open source models.

## Installation and setup

A valid [API key](https://console.mistral.ai/users/api-keys/) is needed to communicate with the API.

You will also need the `langchain-mistralai` package:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install langchain-mistralai
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-mistralai
  ```
</CodeGroup>

## Chat models

### ChatMistralAI

See a [usage example](/oss/python/integrations/chat/mistralai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mistralai.chat_models import ChatMistralAI
```

## Embedding models

### MistralAIEmbeddings

See a [usage example](/oss/python/integrations/embeddings/mistralai).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_mistralai import MistralAIEmbeddings
```

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/mistralai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
