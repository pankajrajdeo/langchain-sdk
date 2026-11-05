---
title: "StateLike"
description: "Type Alias in langgraph"
source: "https://reference.langchain.com/python/langgraph/_internal/_typing/StateLike"
category: "reference"
tags: [reference, langgraph, internal, typing, statelike]
---

# StateLike

> **Type Alias** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_typing/StateLike)

Type alias for state-like types.

It can either be a `TypedDict`, `dataclass`, or Pydantic `BaseModel`.
Note: we cannot use either `TypedDict` or `dataclass` directly due to limitations in type checking.

## Signature

```python
StateLike: TypeAlias = TypedDictLikeV1 | TypedDictLikeV2 | DataclassLike | BaseModel
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/_internal/_typing.py#L38)
