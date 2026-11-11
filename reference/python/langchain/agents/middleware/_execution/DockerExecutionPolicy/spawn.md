---
title: "spawn"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain/agents/middleware/_execution/DockerExecutionPolicy/spawn"
category: "reference"
tags: [reference, langchain, agents, middleware, execution, dockerexecutionpolicy, spawn]
---

# spawn

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_execution/DockerExecutionPolicy/spawn)

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/middleware/_execution.py#L314)
