---
title: "mid_conversation_tools"
description: "Whether tools can be added mid-conversation."
source: "https://reference.langchain.com/python/langchain-core/language_models/model_profile/ModelProfile/mid_conversation_tools"
category: "reference"
tags: [reference, langchain-core, language_models, model_profile, modelprofile, mid_conversation_tools]
---

# mid_conversation_tools

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/model_profile/ModelProfile/mid_conversation_tools)

Whether tools can be added mid-conversation.

The tool is added through a message rather than the request's tool list, so
the prompt prefix before it stays unchanged. Implies
`mid_conversation_system_messages`.

The message format is provider-specific. Every provider that sets this
accepts a tool's full definition; some also accept a reference to a tool
already in the request, or can remove a tool.

## Signature

```python
mid_conversation_tools: bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/language_models/model_profile.py#L146)
