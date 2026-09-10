---
title: "reasoning_effort_default"
description: "The provider's documented default reasoning-effort level, if known."
source: "https://reference.langchain.com/python/langchain-core/language_models/model_profile/ModelProfile/reasoning_effort_default"
category: "reference"
tags: [reference, langchain-core, language_models, model_profile, modelprofile, reasoning_effort_default]
---

# reasoning_effort_default

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/model_profile/ModelProfile/reasoning_effort_default)

The provider's documented default reasoning-effort level, if known.

Absent when no default is documented. Only meaningful when
`reasoning_effort_levels` is non-empty; not necessarily a member of
`reasoning_effort_levels` itself (a model may default to unconfigurable
behavior distinct from any explicit level).

## Signature

```python
reasoning_effort_default: str
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/model_profile.py#L101)
