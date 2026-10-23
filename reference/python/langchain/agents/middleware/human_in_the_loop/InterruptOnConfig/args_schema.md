---
title: "args_schema"
description: "Unused: the middleware doesn't send it to the reviewer in either mode."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig/args_schema"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, interruptonconfig, args_schema]
---

# args_schema

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig/args_schema)

Unused: the middleware doesn't send it to the reviewer in either mode.

In `per_call` mode the interrupt's `response_schema` shows the tool's own argument
schema instead.

## Signature

```python
args_schema: NotRequired[dict[str, Any]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/fbb8a35da7023ac0382c3b22f047337861bd3486/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L349)
