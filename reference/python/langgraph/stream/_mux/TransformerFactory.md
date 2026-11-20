---
title: "TransformerFactory"
description: "Factory that builds a scoped transformer for a mux."
source: "https://reference.langchain.com/python/langgraph/stream/_mux/TransformerFactory"
category: "reference"
tags: [reference, langgraph, stream, mux, transformerfactory]
---

# TransformerFactory

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_mux/TransformerFactory)

Factory that builds a scoped transformer for a mux.

Called once per `StreamMux` with the mux's scope (typically `()` for
the root). Standard transformer classes accept a single positional
scope argument, so the class itself is a valid factory. User
transformers can close over their config:
`lambda scope: MyTransformer(scope, foo=...)`.

## Signature

```python
TransformerFactory = Callable[['tuple[str, ...]'], StreamTransformer]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/stream/_mux.py#L15)
