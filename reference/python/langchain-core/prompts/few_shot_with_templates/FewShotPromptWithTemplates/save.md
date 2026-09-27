---
title: "save"
description: "Save the prompt to a file."
source: "https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates/save"
category: "reference"
tags: [reference, langchain-core, prompts, few_shot_with_templates, fewshotpromptwithtemplates, save]
---

# save

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/few_shot_with_templates/FewShotPromptWithTemplates/save)

Save the prompt to a file.

## Signature

```python
save(
    self,
    file_path: Path | str,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `Path \| str` | Yes | The path to save the prompt to. |

## ⚠️ Deprecated

Deprecated since version 1.2.21. Use Use `dumpd`/`dumps` from `langchain_core.load` to serialize prompts and `load`/`loads` to deserialize them. instead. Will be removed in version 2.0.0.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/prompts/few_shot_with_templates.py#L221)
