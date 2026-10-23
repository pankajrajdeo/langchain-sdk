---
title: "artifact"
description: "Artifact of the Tool execution which is not meant to be sent to the model."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage/artifact"
category: "reference"
tags: [reference, langchain-core, messages, tool, toolmessage, artifact]
---

# artifact

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage/artifact)

Artifact of the Tool execution which is not meant to be sent to the model.

Should only be specified if it is different from the message content, e.g. if only
a subset of the full tool output is being passed as message content but the full
output is needed in other parts of the code.

## Signature

```python
artifact: Any = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/messages/tool.py#L73)
