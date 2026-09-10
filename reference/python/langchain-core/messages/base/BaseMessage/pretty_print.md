---
title: "pretty_print"
description: "Print a pretty representation of the message."
source: "https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/pretty_print"
category: "reference"
tags: [reference, langchain-core, messages, base, basemessage, pretty_print]
---

# pretty_print

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/BaseMessage/pretty_print)

Print a pretty representation of the message.

## Signature

```python
pretty_print(
    self,
) -> None
```

## Description

**Example:**

```python
from langchain_core.messages import AIMessage

msg = AIMessage(content="The capital of France is Paris.")
msg.pretty_print()
```

Results in:

```txt
================================== Ai Message ==================================

The capital of France is Paris.
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/base.py#L344)
