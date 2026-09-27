---
title: "save"
description: "Save the LLM."
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/save"
category: "reference"
tags: [reference, langchain-core, language_models, llms, basellm, save]
---

# save

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/BaseLLM/save)

Save the LLM.

## Signature

```python
save(
    self,
    file_path: Path | str,
) -> None
```

## Description

**Example:**

```python
llm.save(file_path="path/llm.yaml")
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `Path \| str` | Yes | Path to file to save the LLM to. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/language_models/llms.py#L1408)
