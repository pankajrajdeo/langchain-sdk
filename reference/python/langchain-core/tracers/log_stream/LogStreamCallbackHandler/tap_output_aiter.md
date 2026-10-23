---
title: "tap_output_aiter"
description: "Tap an output async iterator to stream its values to the log."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/tap_output_aiter"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, logstreamcallbackhandler, tap_output_aiter]
---

# tap_output_aiter

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/LogStreamCallbackHandler/tap_output_aiter)

Tap an output async iterator to stream its values to the log.

## Signature

```python
tap_output_aiter(
    self,
    run_id: UUID,
    output: AsyncIterator[T],
) -> AsyncIterator[T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_id` | `UUID` | Yes | The ID of the run. |
| `output` | `AsyncIterator[T]` | Yes | The output async iterator. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/tracers/log_stream.py#L322)
