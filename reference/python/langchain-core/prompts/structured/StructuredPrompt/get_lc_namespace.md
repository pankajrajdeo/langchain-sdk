---
title: "get_lc_namespace"
description: "Get the namespace of the LangChain object."
source: "https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/get_lc_namespace"
category: "reference"
tags: [reference, langchain-core, prompts, structured, structuredprompt, get_lc_namespace]
---

# get_lc_namespace

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/get_lc_namespace)

Get the namespace of the LangChain object.

For example, if the class is `langchain.llms.openai.OpenAI`, then the namespace
is `["langchain", "llms", "openai"]`

## Signature

```python
get_lc_namespace(
    cls,
) -> list[str]
```

## Returns

`list[str]`

The namespace of the LangChain object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/structured.py#L84)
