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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/types.py#L1104)
