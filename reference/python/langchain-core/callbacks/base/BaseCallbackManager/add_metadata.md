---
title: "add_metadata"
description: "Add metadata to the callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/add_metadata"
category: "reference"
tags: [reference, langchain-core, callbacks, base, basecallbackmanager, add_metadata]
---

# add_metadata

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/add_metadata)

Add metadata to the callback manager.

## Signature

```python
add_metadata(
    self,
    metadata: dict[str, Any],
    inherit: bool = True,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `metadata` | `dict[str, Any]` | Yes | The metadata to add. |
| `inherit` | `bool` | No | Whether to inherit the metadata. (default: `True`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/base.py#L1197)
