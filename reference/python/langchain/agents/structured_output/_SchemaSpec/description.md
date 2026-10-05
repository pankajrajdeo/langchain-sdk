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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/structured_output.py#L167)
