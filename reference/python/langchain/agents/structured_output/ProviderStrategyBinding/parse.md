---
title: "parse"
description: "Parse AIMessage content according to the schema."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategyBinding/parse"
category: "reference"
tags: [reference, langchain, agents, structured_output, providerstrategybinding, parse]
---

# parse

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategyBinding/parse)

Parse `AIMessage` content according to the schema.

## Signature

```python
parse(
    self,
    response: AIMessage,
) -> SchemaT | dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `response` | `AIMessage` | Yes | The `AIMessage` containing the structured output |

## Returns

`SchemaT | dict[str, Any]`

The parsed response according to the schema

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/structured_output.py#L405)
