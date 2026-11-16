---
title: "response_format"
description: "The tool response format."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/response_format"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, response_format]
---

# response_format

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/response_format)

The tool response format.

If `'content'` then the output of the tool is interpreted as the contents of a
`ToolMessage`. If `'content_and_artifact'` then the output is expected to be a
two-tuple corresponding to the `(content, artifact)` of a `ToolMessage`.

## Signature

```python
response_format: Literal['content', 'content_and_artifact'] = 'content'
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/tools/base.py#L548)
