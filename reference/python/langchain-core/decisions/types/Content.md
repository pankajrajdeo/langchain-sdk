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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/decisions/types.py#L13)
