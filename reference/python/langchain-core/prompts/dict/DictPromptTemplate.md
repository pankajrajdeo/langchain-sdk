---
title: "DictPromptTemplate"
description: "Template represented by a dictionary."
source: "https://reference.langchain.com/python/langchain-core/prompts/dict/DictPromptTemplate"
category: "reference"
tags: [reference, langchain-core, prompts, dict, dictprompttemplate]
---

# DictPromptTemplate

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/dict/DictPromptTemplate)

Template represented by a dictionary.

Recognizes variables in f-string or mustache formatted string dict values.

Does NOT recognize variables in dict keys. Applies recursively.

## Signature

```python
DictPromptTemplate(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
prompt = DictPromptTemplate(
    template={
        "type": "text",
        "text": "Hello {name}",
        "metadata": {"source": "{source}"},
    },
    template_format="f-string",
)
prompt.format(name="Alice", source="docs")
# {
#     "type": "text",
#     "text": "Hello Alice",
#     "metadata": {"source": "docs"},
# }
```

## Extends

- `RunnableSerializable[dict[str, Any], dict[str, Any]]`

## Properties

- `template`
- `template_format`
- `input_variables`

## Methods

- [`validate_template()`](https://reference.langchain.com/python/langchain-core/prompts/dict/DictPromptTemplate/validate_template)
- [`format()`](https://reference.langchain.com/python/langchain-core/prompts/dict/DictPromptTemplate/format)
- [`aformat()`](https://reference.langchain.com/python/langchain-core/prompts/dict/DictPromptTemplate/aformat)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/prompts/dict/DictPromptTemplate/invoke)
- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/prompts/dict/DictPromptTemplate/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/prompts/dict/DictPromptTemplate/get_lc_namespace)
- [`pretty_repr()`](https://reference.langchain.com/python/langchain-core/prompts/dict/DictPromptTemplate/pretty_repr)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/dict.py#L19)
