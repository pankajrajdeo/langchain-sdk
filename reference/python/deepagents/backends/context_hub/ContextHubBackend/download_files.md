---
title: "download_files"
description: "Download files as raw bytes. Missing paths return file_not_found."
source: "https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/download_files"
category: "reference"
tags: [reference, deepagents, backends, context_hub, contexthubbackend, download_files]
---

# download_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/download_files)

Download files as raw bytes. Missing paths return `file_not_found`.

## Signature

```python
download_files(
    self,
    paths: list[str],
) -> list[FileDownloadResponse]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/context_hub.py#L710)
