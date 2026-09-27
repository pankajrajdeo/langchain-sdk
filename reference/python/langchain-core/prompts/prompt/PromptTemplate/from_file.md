---
title: "from_file"
description: "Load a prompt from a file."
source: "https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/from_file"
category: "reference"
tags: [reference, langchain-core, prompts, prompt, prompttemplate, from_file]
---

# from_file

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/from_file)

Load a prompt from a file.

## Signature

```python
from_file(
    cls,
    template_file: str | Path,
    encoding: str | None = None,
    **kwargs: Any = {},
) -> PromptTemplate
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template_file` | `str \| Path` | Yes | The path to the file containing the prompt template. |
| `encoding` | `str \| None` | No | The encoding system for opening the template file.  If not provided, will use the OS default. (default: `None`) |

## Returns

`PromptTemplate`

The prompt loaded from the file.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/prompts/prompt.py#L235)
