---
title: "prepare_node_error_handler_task"
description: "Prepare an immediate node-level error handler task for a failed task."
source: "https://reference.langchain.com/python/langgraph/pregel/_algo/prepare_node_error_handler_task"
category: "reference"
tags: [reference, langgraph, pregel, algo, prepare_node_error_handler_task]
---

# prepare_node_error_handler_task

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_algo/prepare_node_error_handler_task)

Prepare an immediate node-level error handler task for a failed task.

## Signature

```python
prepare_node_error_handler_task(
    failed_task: PregelExecutableTask,
    *,
    handler_node_name: str,
    failed_error: BaseException,
    checkpoint: Checkpoint,
    pending_writes: list[PendingWrite],
    processes: Mapping[str, PregelNode],
    channels: Mapping[str, BaseChannel],
    managed: ManagedValueMapping,
    config: RunnableConfig,
    step: int,
    stop: int,
    store: BaseStore | None = None,
    checkpointer: BaseCheckpointSaver | None = None,
    manager: None | ParentRunManager | AsyncParentRunManager = None,
    cache_policy: CachePolicy | None = None,
    retry_policy: Sequence[RetryPolicy] = (),
) -> PregelExecutableTask | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_algo.py#L1110)
