---
title: "FakeStreamingListLLM"
description: "Fake streaming list LLM for testing purposes."
source: "https://reference.langchain.com/python/langchain-core/language_models/fake/FakeStreamingListLLM"
category: "reference"
tags: [reference, langchain-core, language_models, fake, fakestreaminglistllm]
---

# FakeStreamingListLLM

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/fake/FakeStreamingListLLM)

Fake streaming list LLM for testing purposes.

An LLM that will return responses from a list in order.

This model also supports optionally sleeping between successive
chunks in a streaming implementation.

## Signature

```python
FakeStreamingListLLM(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `FakeListLLM`

## Properties

- `error_on_chunk_number`

## Methods

- [`stream()`](https://reference.langchain.com/python/langchain-core/language_models/fake/FakeStreamingListLLM/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/language_models/fake/FakeStreamingListLLM/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/language_models/fake.py#L85)
