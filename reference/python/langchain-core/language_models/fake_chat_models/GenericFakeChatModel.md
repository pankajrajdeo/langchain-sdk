---
title: "GenericFakeChatModel"
description: "Generic fake chat model that can be used to test the chat model interface."
source: "https://reference.langchain.com/python/langchain-core/language_models/fake_chat_models/GenericFakeChatModel"
category: "reference"
tags: [reference, langchain-core, language_models, fake_chat_models, genericfakechatmodel]
---

# GenericFakeChatModel

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/fake_chat_models/GenericFakeChatModel)

Generic fake chat model that can be used to test the chat model interface.

* Chat model should be usable in both sync and async tests
* Invokes `on_llm_new_token` to allow for testing of callback related code for new
    tokens.
* Includes logic to break messages into message chunk to facilitate testing of
    streaming.

## Signature

```python
GenericFakeChatModel(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseChatModel`

## Properties

- `messages`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/fake_chat_models.py#L227)
