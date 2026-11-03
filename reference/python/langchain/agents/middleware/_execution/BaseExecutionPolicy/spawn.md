---
title: "spawn"
description: "Launch the persistent shell process."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_execution/BaseExecutionPolicy/spawn"
category: "reference"
tags: [reference, langchain, agents, middleware, execution, baseexecutionpolicy, spawn]
---

# spawn

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_execution/BaseExecutionPolicy/spawn)

Launch the persistent shell process.

## Signature

```python
spawn(
    self,
    *,
    workspace: Path,
    env: Mapping[str, str],
    command: Sequence[str],
) -> subprocess.Popen[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/agents/middleware/_execution.py#L80)
