---
title: "upload_files"
description: "Upload text files in one commit; non-UTF-8 inputs rejected per file."
source: "https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/upload_files"
category: "reference"
tags: [reference, deepagents, backends, context_hub, contexthubbackend, upload_files]
---

# upload_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/upload_files)

Upload text files in one commit; non-UTF-8 inputs rejected per file.

## Signature

```python
upload_files(
    self,
    files: list[tuple[str, bytes]],
) -> list[FileUploadResponse]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/backends/context_hub.py#L662)
