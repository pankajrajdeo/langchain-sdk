---
title: "include_run"
description: "Check if a Run should be included in the log."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/include_run"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, logstreamcallbackhandler, include_run]
---

# include_run

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/include_run)

Check if a `Run` should be included in the log.

## Signature

```python
include_run(
    self,
    run: Run,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run` | `Run` | Yes | The `Run` to check. |

## Returns

`bool`

`True` if the `Run` should be included, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/log_stream.py#L386)
