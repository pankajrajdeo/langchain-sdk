---
title: "RunnableSeq"
description: "Sequence of Runnable, where the output of each is the input of the next."
source: "https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableSeq"
category: "reference"
tags: [reference, langgraph, internal, runnable, runnableseq]
---

# RunnableSeq

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableSeq)

Sequence of `Runnable`, where the output of each is the input of the next.

`RunnableSeq` is a simpler version of `RunnableSequence` that is internal to
LangGraph.

## Signature

```python
RunnableSeq(
    self,
    steps: RunnableLike = (),
    *,
    name: str | None = None,
    trace_inputs: Callable[[Any], Any] | None = None,
    trace_policy: TracePolicy | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `steps` | `RunnableLike` | No | The steps to include in the sequence. (default: `()`) |
| `name` | `str \| None` | No | The name of the `Runnable`. (default: `None`) |
| `trace_inputs` | `Callable[[Any], Any] \| None` | No | Transforms the input every callback handler receives. (default: `None`) |
| `trace_policy` | `TracePolicy \| None` | No | Processes what tracers record, after `trace_inputs`. (default: `None`) |

## Extends

- `Runnable`

## Constructors

```python
__init__(
    self,
    steps: RunnableLike = (),
    *,
    name: str | None = None,
    trace_inputs: Callable[[Any], Any] | None = None,
    trace_policy: TracePolicy | None = None,
) -> None
```

| Name | Type |
|------|------|
| `steps` | `RunnableLike` |
| `name` | `str \| None` |
| `trace_inputs` | `Callable[[Any], Any] \| None` |
| `trace_policy` | `TracePolicy \| None` |

## Properties

- `steps`
- `name`
- `trace_inputs`
- `trace_policy`

## Methods

- [`invoke()`](https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableSeq/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableSeq/ainvoke)
- [`stream()`](https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableSeq/stream)
- [`astream()`](https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableSeq/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/_internal/_runnable.py#L616)
