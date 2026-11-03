---
title: "description"
description: "Custom description of the schema."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/_SchemaSpec/description"
category: "reference"
tags: [reference, langchain, agents, structured_output, schemaspec, description]
---

# description

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/_SchemaSpec/description)

Custom description of the schema.

If not provided, will use the model's docstring.

## Signature

```python
description: str = description or (schema.get('description', '') if isinstance(schema, dict) else getattr(schema, '__doc__', None) or '')
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/agents/structured_output.py#L168)
