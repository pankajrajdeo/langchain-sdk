---
title: "get_sync_graph_callback_manager_for_config"
description: "Build a sync graph lifecycle callback manager from a runnable config."
source: "https://reference.langchain.com/python/langgraph/callbacks/get_sync_graph_callback_manager_for_config"
category: "reference"
tags: [reference, langgraph, callbacks, get_sync_graph_callback_manager_for_config]
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/callbacks.py#L363)
