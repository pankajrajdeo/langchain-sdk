---
title: "stream"
description: "Streaming infrastructure for LangGraph."
source: "https://reference.langchain.com/python/langgraph/stream"
category: "reference"
tags: [reference, langgraph, stream]
---

# stream

> **Module** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream)

Streaming infrastructure for LangGraph.

Compile a graph with `transformers=[...]` and call `graph.stream_events(version="v3")` /
`graph.astream_events(version="v3")` to drive a transformer pipeline that projects the
graph's raw events into ergonomic per-channel streams.

## Properties

- `SubgraphStatus`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/stream/__init__.py)
