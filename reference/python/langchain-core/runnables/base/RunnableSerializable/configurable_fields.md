---
title: "configurable_fields"
description: "Configure particular Runnable fields at runtime."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSerializable/configurable_fields"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableserializable, configurable_fields]
---

# configurable_fields

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSerializable/configurable_fields)

Configure particular `Runnable` fields at runtime.

## Signature

```python
configurable_fields(
    self,
    **kwargs: AnyConfigurableField = {},
) -> RunnableSerializable[Input, Output]
```

## Description

!!! example

```python
from langchain_core.runnables import ConfigurableField
from langchain_openai import ChatOpenAI

model = ChatOpenAI(max_tokens=20).configurable_fields(
    max_tokens=ConfigurableField(
        id="output_token_number",
        name="Max tokens in the output",
        description="The maximum number of tokens in the output",
    )
)

# max_tokens = 20
print(
    "max_tokens_20: ", model.invoke("tell me something about chess").content
)

# max_tokens = 200
print(
    "max_tokens_200: ",
    model.with_config(configurable={"output_token_number": 200})
    .invoke("tell me something about chess")
    .content,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `AnyConfigurableField` | No | A dictionary of `ConfigurableField` instances to configure. (default: `{}`) |

## Returns

`RunnableSerializable[Input, Output]`

A new `Runnable` with the fields configured.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L2855)
