---
title: "PregelScratchpad"
description: "- step - stop - call_counter - interrupt_counter - get_null_resume - resume - subgraph_counter"
source: "https://reference.langchain.com/python/langgraph/_internal/_scratchpad/PregelScratchpad"
category: "reference"
tags: [reference, langgraph, internal, scratchpad, pregelscratchpad]
---

# PregelScratchpad

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_scratchpad/PregelScratchpad)

## Signature

```python
PregelScratchpad(
    self,
    step: int,
    stop: int,
    call_counter: Callable[[], int],
    interrupt_counter: Callable[[], int],
    get_null_resume: Callable[[bool], Any],
    resume: list[Any],
    subgraph_counter: Callable[[], int],
)
```

## Constructors

```python
__init__(
    self,
    step: int,
    stop: int,
    call_counter: Callable[[], int],
    interrupt_counter: Callable[[], int],
    get_null_resume: Callable[[bool], Any],
    resume: list[Any],
    subgraph_counter: Callable[[], int],
) -> None
```

| Name | Type |
|------|------|
| `step` | `int` |
| `stop` | `int` |
| `call_counter` | `Callable[[], int]` |
| `interrupt_counter` | `Callable[[], int]` |
| `get_null_resume` | `Callable[[bool], Any]` |
| `resume` | `list[Any]` |
| `subgraph_counter` | `Callable[[], int]` |

## Properties

- `step`
- `stop`
- `call_counter`
- `interrupt_counter`
- `get_null_resume`
- `resume`
- `subgraph_counter`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/_internal/_scratchpad.py#L8)
