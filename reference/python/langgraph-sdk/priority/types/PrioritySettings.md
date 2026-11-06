---
title: "PrioritySettings"
description: "Priority settings returned by the @priority.assign function."
source: "https://reference.langchain.com/python/langgraph-sdk/priority/types/PrioritySettings"
category: "reference"
tags: [reference, langgraph-sdk, priority, types, prioritysettings]
---

# PrioritySettings

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/priority/types/PrioritySettings)

Priority settings returned by the `@priority.assign` function.

Every key is optional: a missing key or a key set to `None` takes its
default, and returning `None` instead of a dict gives every key its default.
A `priority` outside -5 to 5, or a `fairness_group` longer than 256
characters, is an error.

## Signature

```python
PrioritySettings()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    priority: int | None,
    fairness_group: str | None,
)
```

| Name | Type |
|------|------|
| `priority` | `int \| None` |
| `fairness_group` | `str \| None` |

## Properties

- `priority`
- `fairness_group`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5847733bcb186c26b32da5cc822eaf8a89deffeb/libs/sdk-py/langgraph_sdk/priority/types.py#L48)
