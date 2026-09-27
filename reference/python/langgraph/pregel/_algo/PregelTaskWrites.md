---
title: "PregelTaskWrites"
description: "Simplest implementation of WritesProtocol, for usage with writes that don't originate from a runnable task, eg. graph input, update_state, etc."
source: "https://reference.langchain.com/python/langgraph/pregel/_algo/PregelTaskWrites"
category: "reference"
tags: [reference, langgraph, pregel, algo, pregeltaskwrites]
---

# PregelTaskWrites

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_algo/PregelTaskWrites)

Simplest implementation of WritesProtocol, for usage with writes that
don't originate from a runnable task, eg. graph input, update_state, etc.

## Signature

```python
PregelTaskWrites()
```

## Extends

- `NamedTuple`

## Properties

- `path`
- `name`
- `writes`
- `triggers`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_algo.py#L110)
