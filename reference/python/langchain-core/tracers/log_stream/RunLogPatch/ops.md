---
title: "ops"
description: "List of JSONPatch operations, which describe how to create the run state from an empty dict."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunLogPatch/ops"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, runlogpatch, ops]
---

# ops

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunLogPatch/ops)

List of `JSONPatch` operations, which describe how to create the run state
from an empty dict.

This is the minimal representation of the log, designed to be serialized as JSON and
sent over the wire to reconstruct the log on the other side. Reconstruction of the
state can be done with any JSONPatch-compliant library, see https://jsonpatch.com
for more information.

## Signature

```python
ops: list[dict[str, Any]] = list(ops)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/tracers/log_stream.py#L135)
