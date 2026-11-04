---
title: "BytesLineDecoder"
description: "Handles incrementally reading lines from text."
source: "https://reference.langchain.com/python/langgraph-sdk/sse/BytesLineDecoder"
category: "reference"
tags: [reference, langgraph-sdk, sse, byteslinedecoder]
---

# BytesLineDecoder

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/sse/BytesLineDecoder)

Handles incrementally reading lines from text.

Has the same behaviour as the stdllib bytes splitlines,
but handling the input iteratively.

## Signature

```python
BytesLineDecoder(
    self,
)
```

## Constructors

```python
__init__(
    self,
) -> None
```

## Properties

- `buffer`
- `trailing_cr`

## Methods

- [`decode()`](https://reference.langchain.com/python/langgraph-sdk/sse/BytesLineDecoder/decode)
- [`flush()`](https://reference.langchain.com/python/langgraph-sdk/sse/BytesLineDecoder/flush)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/sse.py#L17)
