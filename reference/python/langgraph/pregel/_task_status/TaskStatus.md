---
title: "TaskStatus"
description: "The status of one task, read from the writes recorded for its superstep."
source: "https://reference.langchain.com/python/langgraph/pregel/_task_status/TaskStatus"
category: "reference"
tags: [reference, langgraph, pregel, task_status, taskstatus]
---

# TaskStatus

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_task_status/TaskStatus)

The status of one task, read from the writes recorded for its superstep.

## Signature

```python
TaskStatus(
    self,
    output: tuple[tuple[str, Any], ...] = (),
    interrupts: tuple[Interrupt, ...] = (),
    error: BaseException | None = None,
)
```

## Constructors

```python
__init__(
    self,
    output: tuple[tuple[str, Any], ...] = (),
    interrupts: tuple[Interrupt, ...] = (),
    error: BaseException | None = None,
) -> None
```

| Name | Type |
|------|------|
| `output` | `tuple[tuple[str, Any], ...]` |
| `interrupts` | `tuple[Interrupt, ...]` |
| `error` | `BaseException \| None` |

## Properties

- `output`
- `interrupts`
- `error`
- `finished`
- `pending_interrupts`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_task_status.py#L75)
