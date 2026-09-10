---
title: "name"
description: "Name of the schema, used for tool calling."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/_SchemaSpec/name"
category: "reference"
tags: [reference, langchain, agents, structured_output, schemaspec, name]
---

# name

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/_SchemaSpec/name)

Name of the schema, used for tool calling.

If not provided, the name will be the class name for models/dataclasses/TypedDicts,
or the `title` field for JSON schemas.

Falls back to a generated name if unavailable.

## Signature

```python
name: str
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/structured_output.py#L115)
