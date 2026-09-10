---
title: "profile"
description: "Profile detailing model capabilities."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/profile"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel, profile]
---

# profile

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/profile)

Profile detailing model capabilities.

!!! warning "Beta feature"

    This is a beta feature. The format of model profiles is subject to change.

If not specified, automatically loaded from the provider package on initialization
if data is available.

Example profile data includes context window sizes, supported modalities, or support
for tool calling, structured output, and other features.

!!! version-added "Added in `langchain-core` 1.1.0"

## Signature

```python
profile: ModelProfile | None = Field(default=None, exclude=True)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/chat_models.py#L378)
