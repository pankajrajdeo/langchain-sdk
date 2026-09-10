---
title: "run_in_executor"
description: "Run a function in an executor."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/transform/run_in_executor"
category: "reference"
tags: [reference, langchain-core, output_parsers, transform, run_in_executor]
---

# run_in_executor

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/run_in_executor)

Run a function in an executor.

## Signature

```python
run_in_executor(
    executor_or_config: Executor | RunnableConfig | None,
    func: Callable[P, T],
    *args: P.args = (),
    **kwargs: P.kwargs = {},
) -> T
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `executor_or_config` | `Executor \| RunnableConfig \| None` | Yes | The executor or config to run in. |
| `func` | `Callable[P, T]` | Yes | The function. |
| `*args` | `P.args` | No | The positional arguments to the function. (default: `()`) |
| `**kwargs` | `P.kwargs` | No | The keyword arguments to the function. (default: `{}`) |

## Returns

`T`

The output of the function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/config.py#L678)
