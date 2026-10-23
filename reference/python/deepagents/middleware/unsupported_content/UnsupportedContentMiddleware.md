---
title: "UnsupportedContentMiddleware"
description: "Replace multimodal input blocks the active model can't accept with a text notice."
source: "https://reference.langchain.com/python/deepagents/middleware/unsupported_content/UnsupportedContentMiddleware"
category: "reference"
tags: [reference, deepagents, middleware, unsupported_content, unsupportedcontentmiddleware]
---

# UnsupportedContentMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/unsupported_content/UnsupportedContentMiddleware)

Replace multimodal input blocks the active model can't accept with a text notice.

Without it, a request carrying content the model can't accept (e.g. an image sent
to a text-only model) fails, and since that content stays in the thread, every
later request fails too. This middleware replaces such blocks with a text notice
on every model request. The thread itself keeps the original content, so switching
to a model that accepts it sends it again.

Support is read from
[`model.profile`](../../../../../langchain/models.md#model-profiles).

Place this middleware last in the `middleware` list, so that if
`ModelRequest.model` changes, this middleware will apply to the correct one.

[`create_deep_agent`][deepagents.graph.create_deep_agent] adds it automatically.

## Signature

```python
UnsupportedContentMiddleware()
```

## Description

**Example:**

```python
from deepagents.middleware import FilesystemMiddleware, UnsupportedContentMiddleware
from langchain.agents import create_agent

agent = create_agent(model, middleware=[FilesystemMiddleware(), UnsupportedContentMiddleware()])
```

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Properties

- `trace_policy`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/unsupported_content/UnsupportedContentMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/unsupported_content/UnsupportedContentMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/unsupported_content.py#L109)
