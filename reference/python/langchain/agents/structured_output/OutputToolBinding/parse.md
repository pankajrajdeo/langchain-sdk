---
title: "parse"
description: "Parse tool arguments according to the schema."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding/parse"
category: "reference"
tags: [reference, langchain, agents, structured_output, outputtoolbinding, parse]
---

# parse

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding/parse)

Parse tool arguments according to the schema.

## Signature

```python
parse(
    self,
    tool_args: dict[str, Any],
) -> SchemaT | dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tool_args` | `dict[str, Any]` | Yes | The arguments from the tool call |

## Returns

`SchemaT | dict[str, Any]`

The parsed response according to the schema type

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/structured_output.py#L359)
