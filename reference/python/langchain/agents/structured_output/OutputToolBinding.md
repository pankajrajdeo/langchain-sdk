---
title: "OutputToolBinding"
description: "Information for tracking structured output tool metadata."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding"
category: "reference"
tags: [reference, langchain, agents, structured_output, outputtoolbinding]
---

# OutputToolBinding

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding)

Information for tracking structured output tool metadata.

This contains all necessary information to handle structured responses generated via
tool calls, including the original schema, its type classification, and the
corresponding tool implementation used by the tools strategy.

## Signature

```python
OutputToolBinding(
    self,
    schema: type[SchemaT] | dict[str, Any],
    schema_kind: SchemaKind,
    tool: BaseTool,
)
```

## Extends

- `Generic[SchemaT]`

## Constructors

```python
__init__(
    self,
    schema: type[SchemaT] | dict[str, Any],
    schema_kind: SchemaKind,
    tool: BaseTool,
) -> None
```

| Name | Type |
|------|------|
| `schema` | `type[SchemaT] \| dict[str, Any]` |
| `schema_kind` | `SchemaKind` |
| `tool` | `BaseTool` |

## Properties

- `schema`
- `schema_kind`
- `tool`

## Methods

- [`from_schema_spec()`](https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding/from_schema_spec)
- [`parse()`](https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding/parse)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/structured_output.py#L317)
