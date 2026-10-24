---
title: "put_writes_accepts_task_path"
description: "Whether a saver's put_writes or aput_writes takes task_path."
source: "https://reference.langchain.com/python/langgraph/pregel/main/put_writes_accepts_task_path"
category: "reference"
tags: [reference, langgraph, pregel, main, put_writes_accepts_task_path]
---

# put_writes_accepts_task_path

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/put_writes_accepts_task_path)

Whether a saver's `put_writes` or `aput_writes` takes `task_path`.

Savers written before the parameter existed don't, so it is passed only
when this is true.

## Signature

```python
put_writes_accepts_task_path(
    put_writes: Callable[..., Any],
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_checkpoint.py#L56)
