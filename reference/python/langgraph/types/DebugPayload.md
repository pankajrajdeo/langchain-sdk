---
title: "DebugPayload"
description: "Wrapper payload for debug events. Discriminate on type."
source: "https://reference.langchain.com/python/langgraph/types/DebugPayload"
category: "reference"
tags: [reference, langgraph, types, debugpayload]
---

# DebugPayload

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/DebugPayload)

Wrapper payload for debug events. Discriminate on `type`.

## Signature

```python
DebugPayload = TypeAliasType('DebugPayload', _DebugCheckpointPayload[StateT] | _DebugTaskPayload | _DebugTaskResultPayload, type_params=(StateT,))
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/types.py#L266)
