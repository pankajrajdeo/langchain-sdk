---
title: "get_enhanced_type_hints"
description: "Attempt to extract default values and descriptions from provided type, used for config schema."
source: "https://reference.langchain.com/python/langgraph/_internal/_fields/get_enhanced_type_hints"
category: "reference"
tags: [reference, langgraph, internal, fields, get_enhanced_type_hints]
---

# get_enhanced_type_hints

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_fields/get_enhanced_type_hints)

Attempt to extract default values and descriptions from provided type, used for config schema.

## Signature

```python
get_enhanced_type_hints(
    type: type[Any],
) -> Generator[tuple[str, Any, Any, str | None], None, None]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/_internal/_fields.py#L125)
