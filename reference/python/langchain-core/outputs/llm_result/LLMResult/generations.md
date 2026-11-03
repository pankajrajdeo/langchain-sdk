---
title: "generations"
description: "Generated outputs."
source: "https://reference.langchain.com/python/langchain-core/outputs/llm_result/LLMResult/generations"
category: "reference"
tags: [reference, langchain-core, outputs, llm_result, llmresult, generations]
---

# generations

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs/llm_result/LLMResult/generations)

Generated outputs.

The first dimension of the list represents completions for different input prompts.

The second dimension of the list represents different candidate generations for a
given prompt.

- When returned from **an LLM**, the type is `list[list[Generation]]`.
- When returned from a **chat model**, the type is `list[list[ChatGeneration]]`.

`ChatGeneration` is a subclass of `Generation` that has a field for a structured
chat message.

## Signature

```python
generations: list[list[Generation | ChatGeneration | GenerationChunk | ChatGenerationChunk]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/outputs/llm_result.py#L23)
