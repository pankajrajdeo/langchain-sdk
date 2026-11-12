---
title: "mid_conversation_system_messages"
description: "Whether a SystemMessage after the first turn is sent where it sits."
source: "https://reference.langchain.com/python/langchain-core/language_models/model_profile/ModelProfile/mid_conversation_system_messages"
category: "reference"
tags: [reference, langchain-core, language_models, model_profile, modelprofile, mid_conversation_system_messages]
---

# mid_conversation_system_messages

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/model_profile/ModelProfile/mid_conversation_system_messages)

Whether a `SystemMessage` after the first turn is sent where it sits.

Absent or `False` means the chat model may move it into the leading system
prompt instead.

## Signature

```python
mid_conversation_system_messages: bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/language_models/model_profile.py#L139)
