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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/_async/runs.py#L615)
