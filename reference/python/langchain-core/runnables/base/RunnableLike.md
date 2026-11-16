---
title: "RunnableLike"
description: "Type Alias in langchain_core"
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLike"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablelike]
---

# RunnableLike

> **Type Alias** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLike)

## Signature

```python
RunnableLike = Runnable[Input, Output] | Callable[[Input], Output] | Callable[[Input], Awaitable[Output]] | Callable[[Iterator[Input]], Iterator[Output]] | Callable[[AsyncIterator[Input]], AsyncIterator[Output]] | _RunnableCallableSync[Input, Output] | _RunnableCallableAsync[Input, Output] | _RunnableCallableIterator[Input, Output] | _RunnableCallableAsyncIterator[Input, Output] | Mapping[str, Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/runnables/base.py#L6595)
