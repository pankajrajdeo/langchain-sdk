---
title: "on_llm_new_token"
description: "Run on new LLM token."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_new_token"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_llm_new_token]
---

# on_llm_new_token

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_new_token)

Run on new LLM token.

Only available when streaming is enabled.

## Signature

```python
on_llm_new_token(
    self,
    token: str | list[str | dict[str, Any]],
    *,
    chunk: GenerationChunk | ChatGenerationChunk | None = None,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `token` | `str \| list[str \| dict[str, Any]]` | Yes | The token, or a list of content blocks for structured output. |
| `chunk` | `GenerationChunk \| ChatGenerationChunk \| None` | No | The chunk. (default: `None`) |
| `run_id` | `UUID` | Yes | The run ID. |
| `parent_run_id` | `UUID \| None` | No | The parent run ID. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/base.py#L149)
