---
title: "ToolStrategy"
description: "Use a tool calling strategy for model responses."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/ToolStrategy"
category: "reference"
tags: [reference, langchain, agents, structured_output, toolstrategy]
---

# ToolStrategy

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/ToolStrategy)

Use a tool calling strategy for model responses.

## Signature

```python
ToolStrategy(
    self,
    schema: type[SchemaT] | UnionType | dict[str, Any],
    *,
    tool_message_content: str | None = None,
    handle_errors: bool | str | type[Exception] | tuple[type[Exception], ...] | Callable[[Exception], str] = True,
)
```

## Extends

- `Generic[SchemaT]`

## Constructors

```python
__init__(
    self,
    schema: type[SchemaT] | UnionType | dict[str, Any],
    *,
    tool_message_content: str | None = None,
    handle_errors: bool | str | type[Exception] | tuple[type[Exception], ...] | Callable[[Exception], str] = True,
) -> None
```

| Name | Type |
|------|------|
| `schema` | `type[SchemaT] \| UnionType \| dict[str, Any]` |
| `tool_message_content` | `str \| None` |
| `handle_errors` | `bool \| str \| type[Exception] \| tuple[type[Exception], ...] \| Callable[[Exception], str]` |

## Properties

- `schema`
- `schema_specs`
- `tool_message_content`
- `handle_errors`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/structured_output.py#L195)
