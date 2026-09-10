---
title: "pick"
description: "Pick keys from the output dict of this Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/pick"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, pick]
---

# pick

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/pick)

Pick keys from the output `dict` of this `Runnable`.

!!! example "Pick a single key"

```python
    import json

    from langchain_core.runnables import RunnableLambda, RunnableMap

    as_str = RunnableLambda(str)
    as_json = RunnableLambda(json.loads)
    chain = RunnableMap(str=as_str, json=as_json)

    chain.invoke("[1, 2, 3]")
    # -> {"str": "[1, 2, 3]", "json": [1, 2, 3]}

    json_only_chain = chain.pick("json")
    json_only_chain.invoke("[1, 2, 3]")
    # -> [1, 2, 3]
```

!!! example "Pick a list of keys"

```python
    from typing import Any

    import json

    from langchain_core.runnables import RunnableLambda, RunnableMap

    as_str = RunnableLambda(str)
    as_json = RunnableLambda(json.loads)

    def as_bytes(x: Any) -> bytes:
        return bytes(x, "utf-8")

    chain = RunnableMap(
        str=as_str, json=as_json, bytes=RunnableLambda(as_bytes)
    )

    chain.invoke("[1, 2, 3]")
    # -> {"str": "[1, 2, 3]", "json": [1, 2, 3], "bytes": b"[1, 2, 3]"}

    json_and_bytes_chain = chain.pick(["json", "bytes"])
    json_and_bytes_chain.invoke("[1, 2, 3]")
    # -> {"json": [1, 2, 3], "bytes": b"[1, 2, 3]"}
```

## Signature

```python
pick(
    self,
    keys: str | list[str],
) -> RunnableSerializable[Any, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | `str \| list[str]` | Yes | A key or list of keys to pick from the output dict. |

## Returns

`RunnableSerializable[Any, Any]`

a new `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/base.py#L773)
