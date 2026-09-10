---
title: "StructuredPrompt"
description: "Structured prompt template for a language model."
source: "https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt"
category: "reference"
tags: [reference, langchain-core, prompts, structured, structuredprompt]
---

# StructuredPrompt

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt)

Structured prompt template for a language model.

## Signature

```python
StructuredPrompt(
    self,
    messages: Sequence[MessageLikeRepresentation],
    schema_: dict[str, Any] | type[BaseModel] | None = None,
    *,
    structured_output_kwargs: dict[str, Any] | None = None,
    template_format: PromptTemplateFormat = 'f-string',
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `messages` | `Sequence[MessageLikeRepresentation]` | Yes | Sequence of messages. |
| `schema_` | `dict[str, Any] \| type[BaseModel] \| None` | No | Schema for the structured prompt. (default: `None`) |
| `structured_output_kwargs` | `dict[str, Any] \| None` | No | Additional kwargs for structured output. (default: `None`) |
| `template_format` | `PromptTemplateFormat` | No | Template format for the prompt. (default: `'f-string'`) |

## Extends

- `ChatPromptTemplate`

## Constructors

```python
__init__(
    self,
    messages: Sequence[MessageLikeRepresentation],
    schema_: dict[str, Any] | type[BaseModel] | None = None,
    *,
    structured_output_kwargs: dict[str, Any] | None = None,
    template_format: PromptTemplateFormat = 'f-string',
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `messages` | `Sequence[MessageLikeRepresentation]` |
| `schema_` | `dict[str, Any] \| type[BaseModel] \| None` |
| `structured_output_kwargs` | `dict[str, Any] \| None` |
| `template_format` | `PromptTemplateFormat` |

## Properties

- `schema_`
- `structured_output_kwargs`

## Methods

- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/get_lc_namespace)
- [`from_messages_and_schema()`](https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/from_messages_and_schema)
- [`pipe()`](https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/pipe)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/structured.py#L36)
