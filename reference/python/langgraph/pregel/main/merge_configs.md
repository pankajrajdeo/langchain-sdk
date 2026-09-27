---
title: "merge_configs"
description: "Merge multiple configs into one."
source: "https://reference.langchain.com/python/langgraph/pregel/main/merge_configs"
category: "reference"
tags: [reference, langgraph, pregel, main, merge_configs]
---

# merge_configs

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_config/merge_configs)

Merge multiple configs into one.

## Signature

```python
merge_configs(
    *configs: RunnableConfig | None = (),
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*configs` | `RunnableConfig \| None` | No | The configs to merge. (default: `()`) |

## Returns

`RunnableConfig`

The merged config.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/_internal/_config.py#L147)
