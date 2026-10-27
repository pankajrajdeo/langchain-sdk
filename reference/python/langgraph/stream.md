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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/stream/__init__.py)
