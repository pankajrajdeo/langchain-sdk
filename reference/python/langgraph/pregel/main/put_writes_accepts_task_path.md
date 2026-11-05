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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_checkpoint.py#L56)
