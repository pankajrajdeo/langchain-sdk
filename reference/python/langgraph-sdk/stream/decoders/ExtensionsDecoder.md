---
title: "ExtensionsDecoder"
description: "Yields params.data from one named custom channel."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/decoders/ExtensionsDecoder"
category: "reference"
tags: [reference, langgraph-sdk, stream, decoders, extensionsdecoder]
---

# ExtensionsDecoder

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/decoders/ExtensionsDecoder)

Yields `params.data` from one named custom channel.

Mirrors `_ExtensionProjection._iter` (`_async/stream.py:1278-1299`), with
an added name filter so it can share one subscription in interleave.

## Signature

```python
ExtensionsDecoder(
    self,
    name: str,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | Yes | The extension name. Only `custom` events whose `data["name"]` matches are consumed. |

## Constructors

```python
__init__(
    self,
    name: str,
)
```

| Name | Type |
|------|------|
| `name` | `str` |

## Methods

- [`feed()`](https://reference.langchain.com/python/langgraph-sdk/stream/decoders/ExtensionsDecoder/feed)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/stream/decoders.py#L334)
