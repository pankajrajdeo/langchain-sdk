---
title: "UnknownInterruptError"
description: "Raised in strict resume mode when a resume doesn't match the pending interrupts."
source: "https://reference.langchain.com/python/langgraph/errors/UnknownInterruptError"
category: "reference"
tags: [reference, langgraph, errors, unknowninterrupterror]
---

# UnknownInterruptError

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/errors/UnknownInterruptError)

Raised in strict resume mode when a resume doesn't match the pending interrupts.

`reason` says how it doesn't match:

- `"not_pending"`: the resume names interrupts that aren't pending, listed in
  `interrupt_ids`.
- `"empty_map"`: the resume is an empty map.
- `"ambiguous"`: the resume is a single value while several interrupts are
  pending.

`pending_ids` lists the interrupts still waiting for an answer. The error is
raised before anything is written, so they can still be answered.

A single value with no interrupt pending is accepted, because it resumes a
graph paused at a static breakpoint (`interrupt_before` or `interrupt_after`).

The interrupts one task raises share an id, so an answer retried after the
task asked its next question answers that question.

## Signature

```python
UnknownInterruptError(
    self,
    message: str,
    *,
    reason: Literal['not_pending', 'empty_map', 'ambiguous'],
    interrupt_ids: Sequence[str] = (),
    pending_ids: Sequence[str] = (),
)
```

## Extends

- `Exception`

## Constructors

```python
__init__(
    self,
    message: str,
    *,
    reason: Literal['not_pending', 'empty_map', 'ambiguous'],
    interrupt_ids: Sequence[str] = (),
    pending_ids: Sequence[str] = (),
) -> None
```

| Name | Type |
|------|------|
| `message` | `str` |
| `reason` | `Literal['not_pending', 'empty_map', 'ambiguous']` |
| `interrupt_ids` | `Sequence[str]` |
| `pending_ids` | `Sequence[str]` |

## Properties

- `reason`
- `interrupt_ids`
- `pending_ids`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/errors.py#L150)
