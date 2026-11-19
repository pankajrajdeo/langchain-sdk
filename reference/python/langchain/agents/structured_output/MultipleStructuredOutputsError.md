---
title: "MultipleStructuredOutputsError"
description: "Raised when model returns multiple structured output tool calls when only one is expected."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/MultipleStructuredOutputsError"
category: "reference"
tags: [reference, langchain, agents, structured_output, multiplestructuredoutputserror]
---

# MultipleStructuredOutputsError

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/MultipleStructuredOutputsError)

Raised when model returns multiple structured output tool calls when only one is expected.

## Signature

```python
MultipleStructuredOutputsError(
    self,
    tool_names: list[str],
    ai_message: AIMessage,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tool_names` | `list[str]` | Yes | The names of the tools called for structured output. |
| `ai_message` | `AIMessage` | Yes | The AI message that contained the invalid multiple tool calls. |

## Extends

- `StructuredOutputError`

## Constructors

```python
__init__(
    self,
    tool_names: list[str],
    ai_message: AIMessage,
) -> None
```

| Name | Type |
|------|------|
| `tool_names` | `list[str]` |
| `ai_message` | `AIMessage` |

## Properties

- `tool_names`
- `ai_message`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/structured_output.py#L43)
