---
title: "astream_events"
description: "Async variant of stream_events."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/astream_events"
category: "reference"
tags: [reference, langgraph, pregel, main, astream_events]
---

# astream_events

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/astream_events)

Async variant of `stream_events`.

For `version="v3"`, returns an `AsyncGraphRunStream` whose
projections can be awaited concurrently; each subscribed cursor
drives the pump when its buffer is empty. The same nesting
limitation as the sync path applies — see `stream_events` for
details.

!!! warning

    The `version="v3"` API is experimental and may change.

See `stream_events` for full argument and return documentation.

## Signature

```python
astream_events(
    self,
    input: InputT | Command | None,
    config: RunnableConfig | None = None,
    *,
    version: Literal['v1', 'v2', 'v3'] = 'v2',
    transformers: Sequence[Callable[[tuple[str, ...]], Any]] | None = None,
    kwargs: Any = {},
) -> AsyncIterator[StreamEvent] | Awaitable[Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/main.py#L3837)
