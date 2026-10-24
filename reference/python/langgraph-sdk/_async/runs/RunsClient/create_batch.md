---
title: "create_batch"
description: "Create a batch of stateless background runs."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/create_batch"
category: "reference"
tags: [reference, langgraph-sdk, async, runs, runsclient, create_batch]
---

# create_batch

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/create_batch)

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/_async/runs.py#L607)
