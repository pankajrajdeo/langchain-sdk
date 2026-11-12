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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/structured_output.py#L391)
