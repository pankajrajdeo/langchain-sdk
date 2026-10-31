---
title: "is_supported_by_pydantic"
description: "Check if a given \"complex\" type is supported by pydantic."
source: "https://reference.langchain.com/python/langgraph/_internal/_pydantic/is_supported_by_pydantic"
category: "reference"
tags: [reference, langgraph, internal, pydantic, is_supported_by_pydantic]
---

# is_supported_by_pydantic

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_pydantic/is_supported_by_pydantic)

Check if a given "complex" type is supported by pydantic.

This will return False for primitive types like int, str, etc.

The check is meant for container types like dataclasses, TypedDicts, etc.

## Signature

```python
is_supported_by_pydantic(
    type_: Any,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/_internal/_pydantic.py#L252)
