---
title: "trigger"
description: "Token/message/fraction threshold that activates truncation."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/TruncateArgsSettings/trigger"
category: "reference"
tags: [reference, deepagents, middleware, summarization, truncateargssettings, trigger]
---

# trigger

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/TruncateArgsSettings/trigger)

Token/message/fraction threshold that activates truncation.

Uses the same `ContextSize` format as the summarization trigger.

If `None`, truncation is disabled.

## Signature

```python
trigger: ContextSize | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/summarization.py#L197)
