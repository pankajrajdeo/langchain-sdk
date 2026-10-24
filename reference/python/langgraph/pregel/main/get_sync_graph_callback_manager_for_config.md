---
title: "get_sync_graph_callback_manager_for_config"
description: "Build a sync graph lifecycle callback manager from a runnable config."
source: "https://reference.langchain.com/python/langgraph/pregel/main/get_sync_graph_callback_manager_for_config"
category: "reference"
tags: [reference, langgraph, pregel, main, get_sync_graph_callback_manager_for_config]
---

# get_sync_graph_callback_manager_for_config

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/get_sync_graph_callback_manager_for_config)

Build a sync graph lifecycle callback manager from a runnable config.

This helper filters `config["callbacks"]` down to handlers that inherit
from `GraphCallbackHandler` and binds the provided `run_id` onto the
returned manager.

## Signature

```python
get_sync_graph_callback_manager_for_config(
    config: RunnableConfig,
    *,
    run_id: UUID | None = None,
) -> _GraphCallbackManager
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/callbacks.py#L363)
