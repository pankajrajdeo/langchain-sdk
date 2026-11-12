---
title: "ModelRefusalError"
description: "Exception raised when a model declines to produce the requested output."
source: "https://reference.langchain.com/python/langchain-core/exceptions/ModelRefusalError"
category: "reference"
tags: [reference, langchain-core, exceptions, modelrefusalerror]
---

# ModelRefusalError

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/exceptions/ModelRefusalError)

Exception raised when a model declines to produce the requested output.

Providers report a refusal as a successful response rather than an HTTP error
(for example Anthropic's `stop_reason="refusal"`, or the `refusal` field in
OpenAI Structured Outputs), so a plain model call returns the message as-is.
Integrations raise this exception from paths that need the content the model
withheld, such as `with_structured_output`, so callers can handle refusals the
same way across providers instead of receiving a parsing error.

Retrying the same request is unlikely to succeed.

!!! version-added "Added in `langchain-core` 1.7.5"

## Signature

```python
ModelRefusalError(
    self,
    message: str = 'Model refused to produce the requested output',
    *,
    raw_message: BaseMessage | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `str` | No | Error message. (default: `'Model refused to produce the requested output'`) |
| `raw_message` | `BaseMessage \| None` | No | The model response that contained the refusal. Its `content_blocks` hold the refusal block, including any provider-specific details in `extras`. (default: `None`) |

## Extends

- `ModelError`

## Constructors

```python
__init__(
    self,
    message: str = 'Model refused to produce the requested output',
    *,
    raw_message: BaseMessage | None = None,
) -> None
```

| Name | Type |
|------|------|
| `message` | `str` |
| `raw_message` | `BaseMessage \| None` |

## Properties

- `raw_message`

## Methods

- [`from_refusal()`](https://reference.langchain.com/python/langchain-core/exceptions/ModelRefusalError/from_refusal)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/exceptions.py#L137)
