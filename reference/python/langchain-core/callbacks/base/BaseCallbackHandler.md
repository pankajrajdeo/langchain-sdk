---
title: "BaseCallbackHandler"
description: "Base callback handler."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackHandler"
category: "reference"
tags: [reference, langchain-core, callbacks, base, basecallbackhandler]
---

# BaseCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackHandler)

Base callback handler.

## Signature

```python
BaseCallbackHandler()
```

## Extends

- `LLMManagerMixin`
- `ChainManagerMixin`
- `ToolManagerMixin`
- `RetrieverManagerMixin`
- `CallbackManagerMixin`
- `RunManagerMixin`

## Properties

- `raise_error`
- `run_inline`
- `ignore_llm`
- `ignore_retry`
- `ignore_chain`
- `ignore_agent`
- `ignore_retriever`
- `ignore_chat_model`
- `ignore_custom_event`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/base.py#L496)
