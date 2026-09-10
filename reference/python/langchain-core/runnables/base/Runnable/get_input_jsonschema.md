---
title: "get_input_jsonschema"
description: "Get a JSON schema that represents the input to the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_input_jsonschema"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, get_input_jsonschema]
---

# get_input_jsonschema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/get_input_jsonschema)

Get a JSON schema that represents the input to the `Runnable`.

## Signature

```python
get_input_jsonschema(
    self,
    config: RunnableConfig | None = None,
) -> dict[str, Any]
```

## Description

**Example:**

```python
from langchain_core.runnables import RunnableLambda

def add_one(x: int) -> int:
    return x + 1

runnable = RunnableLambda(add_one)

print(runnable.get_input_jsonschema())
```

!!! version-added "Added in `langchain-core` 0.3.0"

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | A config to use when generating the schema. (default: `None`) |

## Returns

`dict[str, Any]`

A JSON schema that represents the input to the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L420)
