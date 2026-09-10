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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/_execution.py#L314)
