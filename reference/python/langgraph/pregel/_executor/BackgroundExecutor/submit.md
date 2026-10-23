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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/_executor.py#L54)
