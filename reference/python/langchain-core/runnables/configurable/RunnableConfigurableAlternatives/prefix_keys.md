---
title: "prefix_keys"
description: "Whether to prefix configurable fields of each alternative with a namespace of the form ==, e.g. a key named \"temperature\" used by the alternative named \"gpt3\" becomes \"model==gpt3/temperature\"."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableAlternatives/prefix_keys"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, runnableconfigurablealternatives, prefix_keys]
---

# prefix_keys

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/RunnableConfigurableAlternatives/prefix_keys)

Whether to prefix configurable fields of each alternative with a namespace
of the form <which.id>==<alternative_key>, e.g. a key named "temperature" used by
the alternative named "gpt3" becomes "model==gpt3/temperature".

## Signature

```python
prefix_keys: bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/1a41b51b0295d7cc6df45cdede199b4a34649b1d/libs/core/langchain_core/runnables/configurable.py#L544)
