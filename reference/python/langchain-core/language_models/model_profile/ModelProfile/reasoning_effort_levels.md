---
title: "reasoning_effort_levels"
description: "Supported reasoning-effort levels (e.g. ['low', 'medium', 'high'])."
source: "https://reference.langchain.com/python/langchain-core/language_models/model_profile/ModelProfile/reasoning_effort_levels"
category: "reference"
tags: [reference, langchain-core, language_models, model_profile, modelprofile, reasoning_effort_levels]
---

# reasoning_effort_levels

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/model_profile/ModelProfile/reasoning_effort_levels)

Supported reasoning-effort levels (e.g. `['low', 'medium', 'high']`).

Absent or empty if the model does not support a configurable reasoning
effort. Only meaningful when `reasoning_output` is `True`.

## Signature

```python
reasoning_effort_levels: list[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/model_profile.py#L94)
