---
title: "checkpoint_ns"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_loop/PregelLoop/checkpoint_ns"
category: "reference"
tags: [reference, langgraph, pregel, loop, pregelloop, checkpoint_ns]
---

# checkpoint_ns

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_loop/PregelLoop/checkpoint_ns)

## Signature

```python
checkpoint_ns: tuple[str, ...] = tuple(cast(str, self.config[CONF][CONFIG_KEY_CHECKPOINT_NS]).split(NS_SEP)) if self.config[CONF].get(CONFIG_KEY_CHECKPOINT_NS) else ()
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/pregel/_loop.py#L405)
