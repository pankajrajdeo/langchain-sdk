---
title: "internal_call_transformer"
description: "Tag and filter middleware-internal model calls."
source: "https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer"
category: "reference"
tags: [reference, langchain, agents, middleware, internal_call_transformer]
---

# internal_call_transformer

> **Module** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer)

Tag and filter middleware-internal model calls.

Tag internal calls with `internal_call_metadata()` and declare
`transformers = (InternalCallTransformer,)` on the middleware class to keep
them out of `run.messages`. Both APIs are public for third-party middleware.

## Properties

- `INTERNAL_CALL_METADATA_KEY`

## Methods

- [`internal_call_metadata()`](https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/internal_call_metadata)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/internal_call_transformer.py)
