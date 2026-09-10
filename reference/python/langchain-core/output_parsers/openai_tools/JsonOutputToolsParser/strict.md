---
title: "strict"
description: "Whether to allow non-JSON-compliant strings."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/JsonOutputToolsParser/strict"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_tools, jsonoutputtoolsparser, strict]
---

# strict

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/JsonOutputToolsParser/strict)

Whether to allow non-JSON-compliant strings.

See: https://docs.python.org/3/library/json.html#encoders-and-decoders

Useful when the parsed output may include unicode characters or new lines.

## Signature

```python
strict: bool = False
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/output_parsers/openai_tools.py#L142)
