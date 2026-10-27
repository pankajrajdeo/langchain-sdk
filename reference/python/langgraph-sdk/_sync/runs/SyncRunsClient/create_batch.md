---
title: "create_batch"
description: "Create a batch of stateless background runs."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/create_batch"
category: "reference"
tags: [reference, langgraph-sdk, sync, runs, syncrunsclient, create_batch]
---

# create_batch

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/runs/SyncRunsClient/create_batch)

Create a batch of stateless background runs.

## Signature

```python
create_batch(
    self,
    payloads: builtins.list[RunCreate],
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> builtins.list[Run]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/_sync/runs.py#L610)
