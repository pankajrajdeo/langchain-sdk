---
title: "criteria"
description: "Candidate labels mapped to their descriptions."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/Choice/criteria"
category: "reference"
tags: [reference, langchain-core, decisions, types, choice, criteria]
---

# criteria

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/Choice/criteria)

Candidate labels mapped to their descriptions.

Descriptions may be text, structured JSON, or `None`. Include an `other` or
`none_of_the_above` label when the supplied alternatives may not cover every input.

## Signature

```python
criteria: dict[str, JsonValue] = Field(min_length=1)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/decisions/types.py#L149)
