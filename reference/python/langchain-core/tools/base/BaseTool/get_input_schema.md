---
title: "get_input_schema"
description: "The tool's input schema."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/get_input_schema"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, get_input_schema]
---

# get_input_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/get_input_schema)

The tool's input schema.

## Signature

```python
get_input_schema(
    self,
    config: RunnableConfig | None = None,
) -> TypeBaseModel
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The configuration for the tool. (default: `None`) |

## Returns

`TypeBaseModel`

The input schema for the tool.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/tools/base.py#L740)
