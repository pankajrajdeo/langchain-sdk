---
title: "BaseGenerationOutputParser"
description: "Base class to parse the output of an LLM call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseGenerationOutputParser"
category: "reference"
tags: [reference, langchain-core, output_parsers, base, basegenerationoutputparser]
---

# BaseGenerationOutputParser

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseGenerationOutputParser)

Base class to parse the output of an LLM call.

## Signature

```python
BaseGenerationOutputParser(
    self,
    args: Any = (),
    kwargs: Any = {},
)
```

## Extends

- `BaseLLMOutputParser[T]`
- `RunnableSerializable[LanguageModelOutput, T]`

## Properties

- `InputType`
- `OutputType`

## Methods

- [`invoke()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseGenerationOutputParser/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseGenerationOutputParser/ainvoke)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/output_parsers/base.py#L74)
