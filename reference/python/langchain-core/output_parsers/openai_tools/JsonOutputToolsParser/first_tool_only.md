---
title: "first_tool_only"
description: "Whether to return only the first tool call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/JsonOutputToolsParser/first_tool_only"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_tools, jsonoutputtoolsparser, first_tool_only]
---

# first_tool_only

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/JsonOutputToolsParser/first_tool_only)

Whether to return only the first tool call.

If `False`, the result will be a list of tool calls, or an empty list if no tool
calls are found.

If `True`, and multiple tool calls are found, only the first one will be returned,
and the other tool calls will be ignored.

If no tool calls are found, `None` will be returned.

## Signature

```python
first_tool_only: bool = False
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/output_parsers/openai_tools.py#L153)
