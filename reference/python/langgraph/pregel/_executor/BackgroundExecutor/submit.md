---
title: "submit"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_executor/BackgroundExecutor/submit"
category: "reference"
tags: [reference, langgraph, pregel, executor, backgroundexecutor, submit]
---

# submit

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_executor/BackgroundExecutor/submit)

## Signature

```python
submit(
    self,
    fn: Callable[P, T],
    args: P.args = (),
    *,
    __name__: str | None = None,
    __cancel_on_exit__: bool = False,
    __reraise_on_exit__: bool = True,
    __next_tick__: bool = False,
    kwargs: P.kwargs = {},
) -> concurrent.futures.Future[T]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_executor.py#L62)
