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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/types.py#L147)
