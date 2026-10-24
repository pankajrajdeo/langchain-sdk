---
title: "prepare_push_task_send"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_algo/prepare_push_task_send"
category: "reference"
tags: [reference, langgraph, pregel, algo, prepare_push_task_send]
---

# prepare_push_task_send

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_algo/prepare_push_task_send)

## Signature

```python
prepare_push_task_send(
    task_path: tuple[str, tuple],
    task_id_checksum: str | None,
    *,
    checkpoint: Checkpoint,
    checkpoint_id_bytes: bytes,
    pending_writes: list[PendingWrite],
    channels: Mapping[str, BaseChannel],
    managed: ManagedValueMapping,
    config: RunnableConfig,
    step: int,
    stop: int,
    for_execution: bool,
    store: BaseStore | None = None,
    checkpointer: BaseCheckpointSaver | None = None,
    manager: None | ParentRunManager | AsyncParentRunManager = None,
    cache_policy: CachePolicy | None = None,
    retry_policy: Sequence[RetryPolicy] = (),
    parent_ns: str,
    task_id_func: _TaskIDFn,
    processes: Mapping[str, PregelNode],
) -> PregelTask | PregelExecutableTask | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_algo.py#L937)
