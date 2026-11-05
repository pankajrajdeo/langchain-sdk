---
title: "from_schema_spec"
description: "Create a ProviderStrategyBinding instance from a SchemaSpec."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategyBinding/from_schema_spec"
category: "reference"
tags: [reference, langchain, agents, structured_output, providerstrategybinding, from_schema_spec]
---

# from_schema_spec

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategyBinding/from_schema_spec)

Create a `ProviderStrategyBinding` instance from a `SchemaSpec`.

## Signature

```python
from_schema_spec(
    cls,
    schema_spec: _SchemaSpec[SchemaT],
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `schema_spec` | `_SchemaSpec[SchemaT]` | Yes | The `SchemaSpec` to convert |

## Returns

`Self`

A `ProviderStrategyBinding` instance for parsing native structured output

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d1d95b79213b0212613ae1aa4fad38bea6f1dccf/libs/langchain_v1/langchain/agents/structured_output.py#L390)
