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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/types.py#L265)
