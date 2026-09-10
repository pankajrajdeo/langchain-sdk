---
title: "transformers"
description: "Keeps the summarization model call's tokens out of run.messages."
source: "https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware/transformers"
category: "reference"
tags: [reference, langchain, agents, middleware, summarization, summarizationmiddleware, transformers]
---

# transformers

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware/transformers)

Keeps the summarization model call's tokens out of `run.messages`.

Registered only when this middleware is used — see
`InternalCallTransformer` for why the call needs tagging and filtering.

## Signature

```python
transformers = (InternalCallTransformer,)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/summarization.py#L245)
