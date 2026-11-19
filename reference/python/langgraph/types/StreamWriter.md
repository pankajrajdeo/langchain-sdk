---
title: "StreamWriter"
description: "Callable that accepts a single argument and writes it to the output stream. Always injected into nodes if requested as a keyword argument, but it's a no-op when not using stream_mode=\"custom\"."
source: "https://reference.langchain.com/python/langgraph/types/StreamWriter"
category: "reference"
tags: [reference, langgraph, types, streamwriter]
---

# StreamWriter

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/StreamWriter)

`Callable` that accepts a single argument and writes it to the output stream.
Always injected into nodes if requested as a keyword argument, but it's a no-op
when not using `stream_mode="custom"`.

## Signature

```python
StreamWriter = Callable[[Any], None]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/types.py#L148)
