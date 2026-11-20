---
title: "type"
description: "Discriminator field. Lets the channel reducer recognise an Overwrite even after its dataclass form is JSON-serialised and the typed instance is lost (e.g. an orjson-encoded state update routed..."
source: "https://reference.langchain.com/python/langgraph/types/Overwrite/type"
category: "reference"
tags: [reference, langgraph, types, overwrite, type]
---

# type

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/Overwrite/type)

Discriminator field. Lets the channel reducer recognise an `Overwrite`
even after its dataclass form is JSON-serialised and the typed instance
is lost (e.g. an `orjson`-encoded state update routed through the
LangGraph API server).

## Signature

```python
type: Literal['__overwrite__'] = '__overwrite__'
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/types.py#L1104)
