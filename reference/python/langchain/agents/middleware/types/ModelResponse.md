---
title: "ModelResponse"
description: "Response from model execution including messages and optional structured output."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/ModelResponse"
category: "reference"
tags: [reference, langchain, agents, middleware, types, modelresponse]
---

# ModelResponse

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/ModelResponse)

Response from model execution including messages and optional structured output.

The result will usually contain a single `AIMessage`, but may include an additional
`ToolMessage` if the model used a tool for structured output.

## Signature

```python
ModelResponse(
    self,
    result: list[BaseMessage],
    structured_response: ResponseT | None = None,
)
```

## Extends

- `Generic[ResponseT]`

## Constructors

```python
__init__(
    self,
    result: list[BaseMessage],
    structured_response: ResponseT | None = None,
) -> None
```

| Name | Type |
|------|------|
| `result` | `list[BaseMessage]` |
| `structured_response` | `ResponseT \| None` |

## Properties

- `result`
- `structured_response`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/middleware/types.py#L272)
