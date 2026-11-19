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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/types.py#L266)
