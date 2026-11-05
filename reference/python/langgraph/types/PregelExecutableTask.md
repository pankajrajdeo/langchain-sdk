---
title: "PregelExecutableTask"
description: "- name - input - proc - writes - config - triggers - retry_policy - cache_key - id - path - writers - subgraphs - timeout"
source: "https://reference.langchain.com/python/langgraph/types/PregelExecutableTask"
category: "reference"
tags: [reference, langgraph, types, pregelexecutabletask]
---

# PregelExecutableTask

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/PregelExecutableTask)

## Signature

```python
PregelExecutableTask(
    self,
    name: str,
    input: Any,
    proc: Runnable,
    writes: deque[tuple[str, Any]],
    config: RunnableConfig,
    triggers: Sequence[str],
    retry_policy: Sequence[RetryPolicy],
    cache_key: CacheKey | None,
    id: str,
    path: tuple[str | int | tuple, ...],
    writers: Sequence[Runnable] = (),
    subgraphs: Sequence[PregelProtocol] = (),
    timeout: TimeoutPolicy | None = None,
)
```

## Constructors

```python
__init__(
    self,
    name: str,
    input: Any,
    proc: Runnable,
    writes: deque[tuple[str, Any]],
    config: RunnableConfig,
    triggers: Sequence[str],
    retry_policy: Sequence[RetryPolicy],
    cache_key: CacheKey | None,
    id: str,
    path: tuple[str | int | tuple, ...],
    writers: Sequence[Runnable] = (),
    subgraphs: Sequence[PregelProtocol] = (),
    timeout: TimeoutPolicy | None = None,
) -> None
```

| Name | Type |
|------|------|
| `name` | `str` |
| `input` | `Any` |
| `proc` | `Runnable` |
| `writes` | `deque[tuple[str, Any]]` |
| `config` | `RunnableConfig` |
| `triggers` | `Sequence[str]` |
| `retry_policy` | `Sequence[RetryPolicy]` |
| `cache_key` | `CacheKey \| None` |
| `id` | `str` |
| `path` | `tuple[str \| int \| tuple, ...]` |
| `writers` | `Sequence[Runnable]` |
| `subgraphs` | `Sequence[PregelProtocol]` |
| `timeout` | `TimeoutPolicy \| None` |

## Properties

- `name`
- `input`
- `proc`
- `writes`
- `config`
- `triggers`
- `retry_policy`
- `cache_key`
- `id`
- `path`
- `writers`
- `subgraphs`
- `timeout`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/types.py#L704)
