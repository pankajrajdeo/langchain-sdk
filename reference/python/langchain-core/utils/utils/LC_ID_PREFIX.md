---
title: "LC_ID_PREFIX"
description: "Internal tracing/callback system identifier."
source: "https://reference.langchain.com/python/langchain-core/utils/utils/LC_ID_PREFIX"
category: "reference"
tags: [reference, langchain-core, utils, lc_id_prefix]
---

# LC_ID_PREFIX

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/LC_ID_PREFIX)

Internal tracing/callback system identifier.

Used for:

- Tracing. Every LangChain operation (LLM call, chain execution, tool use, etc.)
    gets a unique run_id (UUID)
- Enables tracking parent-child relationships between operations

## Signature

```python
LC_ID_PREFIX = 'lc_run-'
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/utils/utils.py#L498)
