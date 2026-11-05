---
title: "Call"
description: "- func - input - retry_policy - cache_policy - callbacks - timeout"
source: "https://reference.langchain.com/python/langgraph/pregel/_algo/Call"
category: "reference"
tags: [reference, langgraph, pregel, algo, call]
---

# Call

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_algo/Call)

## Signature

```python
Call(
    self,
    func: Callable,
    input: tuple[tuple[Any, ...], dict[str, Any]],
    *,
    retry_policy: Sequence[RetryPolicy] | None,
    cache_policy: CachePolicy | None,
    callbacks: Callbacks,
    timeout: TimeoutPolicy | None = None,
)
```

## Constructors

```python
__init__(
    self,
    func: Callable,
    input: tuple[tuple[Any, ...], dict[str, Any]],
    *,
    retry_policy: Sequence[RetryPolicy] | None,
    cache_policy: CachePolicy | None,
    callbacks: Callbacks,
    timeout: TimeoutPolicy | None = None,
) -> None
```

| Name | Type |
|------|------|
| `func` | `Callable` |
| `input` | `tuple[tuple[Any, ...], dict[str, Any]]` |
| `retry_policy` | `Sequence[RetryPolicy] \| None` |
| `cache_policy` | `CachePolicy \| None` |
| `callbacks` | `Callbacks` |
| `timeout` | `TimeoutPolicy \| None` |

## Properties

- `func`
- `input`
- `retry_policy`
- `cache_policy`
- `callbacks`
- `timeout`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_algo.py#L122)
