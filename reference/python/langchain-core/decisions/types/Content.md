---
title: "Content"
description: "Type Alias in langchain_core"
source: "https://reference.langchain.com/python/langchain-core/decisions/types/Content"
category: "reference"
tags: [reference, langchain-core, decisions, types, content]
---

# Content

> **Type Alias** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/Content)

Text, a JSON object, or a JSON array used in question instructions.

As in `State`, LangChain standard media blocks may appear anywhere in instructions and
criteria. Providers send them as media, or raise an error if their API does not accept
that media in questions.

## Signature

```python
Content: TypeAlias = str | dict[str, JsonValue] | list[JsonValue]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/decisions/types.py#L13)
