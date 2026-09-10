---
title: "save"
description: "Save the prompt template to a file."
source: "https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate/save"
category: "reference"
tags: [reference, langchain-core, prompts, few_shot, fewshotprompttemplate, save]
---

# save

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/few_shot/FewShotPromptTemplate/save)

Save the prompt template to a file.

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
| `file_path` | `Path \| str` | Yes | The path to save the prompt template to. |

## ⚠️ Deprecated

Deprecated since version 1.2.21. Use Use `dumpd`/`dumps` from `langchain_core.load` to serialize prompts and `load`/`loads` to deserialize them. instead. Will be removed in version 2.0.0.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/few_shot.py#L241)
