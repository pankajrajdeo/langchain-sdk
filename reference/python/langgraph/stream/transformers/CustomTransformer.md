---
title: "CustomTransformer"
description: "Capture custom events as a drainable stream of arbitrary payloads."
source: "https://reference.langchain.com/python/langgraph/stream/transformers/CustomTransformer"
category: "reference"
tags: [reference, langgraph, stream, transformers, customtransformer]
---

# CustomTransformer

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/transformers/CustomTransformer)

Capture custom events as a drainable stream of arbitrary payloads.

Nodes emit custom data via `get_stream_writer()`. This transformer
surfaces those events on `run.custom` as a `StreamChannel[Any]`,
preserving payloads in arrival order.

Only events at the run's own scope are captured; custom data from
deeper subgraphs is available on the respective subgraph handle's
`.custom` projection.

Native transformer — `run.custom` is a direct attribute.

## Signature

```python
CustomTransformer(
    self,
    scope: tuple[str, ...] = (),
)
```

## Extends

- `StreamTransformer`

## Constructors

```python
__init__(
    self,
    scope: tuple[str, ...] = (),
) -> None
```

| Name | Type |
|------|------|
| `scope` | `tuple[str, ...]` |

## Properties

- `required_stream_modes`

## Methods

- [`init()`](https://reference.langchain.com/python/langgraph/stream/transformers/CustomTransformer/init)
- [`process()`](https://reference.langchain.com/python/langgraph/stream/transformers/CustomTransformer/process)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/stream/transformers.py#L85)
