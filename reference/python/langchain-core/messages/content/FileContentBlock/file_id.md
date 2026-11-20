---
title: "file_id"
description: "Reference to the file in an external file storage system."
source: "https://reference.langchain.com/python/langchain-core/messages/content/FileContentBlock/file_id"
category: "reference"
tags: [reference, langchain-core, messages, content, filecontentblock, file_id]
---

# file_id

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/FileContentBlock/file_id)

Reference to the file in an external file storage system.

For example, a file ID from OpenAI's Files API or another cloud storage provider.
This is distinct from `id`, which identifies the content block itself.

## Signature

```python
file_id: NotRequired[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/messages/content.py#L784)
