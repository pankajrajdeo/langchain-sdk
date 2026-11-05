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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/priority/types.py#L48)
