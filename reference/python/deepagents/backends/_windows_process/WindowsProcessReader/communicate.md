---
title: "communicate"
description: "Collect output and reap the direct process within a polling deadline."
source: "https://reference.langchain.com/python/deepagents/backends/_windows_process/WindowsProcessReader/communicate"
category: "reference"
tags: [reference, deepagents, backends, windows_process, windowsprocessreader, communicate]
---

# communicate

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/_windows_process/WindowsProcessReader/communicate)

Collect output and reap the direct process within a polling deadline.

EOF is required on both pipes even if the shell has already exited.
Descendants that inherited the pipes can still write to them, and their
output is kept.

## Signature

```python
communicate(
    self,
    *,
    timeout: float,
) -> tuple[str, str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timeout` | `float` | Yes | Maximum seconds for this communication attempt. |

## Returns

`tuple[str, str]`

Decoded stdout and stderr after both pipes reach EOF and the process exits.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/5568767515b7edc6b106e92d3de4cc65886c1eca/libs/deepagents/deepagents/backends/_windows_process.py#L113)
