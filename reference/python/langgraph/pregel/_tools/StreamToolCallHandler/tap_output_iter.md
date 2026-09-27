---
title: "tap_output_iter"
description: "Pass-through — sync counterpart to tap_output_aiter."
source: "https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/tap_output_iter"
category: "reference"
tags: [reference, langgraph, pregel, tools, streamtoolcallhandler, tap_output_iter]
---

# tap_output_iter

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/tap_output_iter)

Pass-through — sync counterpart to `tap_output_aiter`.

## Signature

```python
tap_output_iter(
    self,
    run_id: UUID,
    output: Iterator[T],
) -> Iterator[T]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_tools.py#L209)
