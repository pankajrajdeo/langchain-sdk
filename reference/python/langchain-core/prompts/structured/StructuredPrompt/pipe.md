---
title: "pipe"
description: "Pipe the structured prompt to a language model."
source: "https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/pipe"
category: "reference"
tags: [reference, langchain-core, prompts, structured, structuredprompt, pipe]
---

# pipe

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/structured/StructuredPrompt/pipe)

Pipe the structured prompt to a language model.

## Signature

```python
pipe(
    self,
    *others: Runnable[Any, Other] | Callable[[Iterator[Any]], Iterator[Other]] | Callable[[AsyncIterator[Any]], AsyncIterator[Other]] | Callable[[Any], Other] | Mapping[str, Runnable[Any, Other] | Callable[[Any], Other] | Any] = (),
    name: str | None = None,
) -> RunnableSerializable[dict[str, Any], Other]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `others` | `Runnable[Any, Other] \| Callable[[Iterator[Any]], Iterator[Other]] \| Callable[[AsyncIterator[Any]], AsyncIterator[Other]] \| Callable[[Any], Other] \| Mapping[str, Runnable[Any, Other] \| Callable[[Any], Other] \| Any]` | No | The language model to pipe the structured prompt to. (default: `()`) |
| `name` | `str \| None` | No | The name of the pipeline. (default: `None`) |

## Returns

`RunnableSerializable[dict[str, Any], Other]`

A `RunnableSequence` object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/prompts/structured.py#L180)
