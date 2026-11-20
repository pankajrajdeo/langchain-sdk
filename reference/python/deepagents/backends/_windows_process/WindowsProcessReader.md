---
title: "WindowsProcessReader"
description: "Read both captured pipes by polling instead of with reader threads."
source: "https://reference.langchain.com/python/deepagents/backends/_windows_process/WindowsProcessReader"
category: "reference"
tags: [reference, deepagents, backends, windows_process, windowsprocessreader]
---

# WindowsProcessReader

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/_windows_process/WindowsProcessReader)

Read both captured pipes by polling instead of with reader threads.

`subprocess.communicate` starts a thread for each pipe on Windows. Those
threads hold the pipe until the write end closes, so a caller cannot close
the pipes to stop waiting for a descendant that inherited them. This reader
polls instead, which leaves the caller free to close the pipes at any time.

The process must be in text mode, because the reader takes the encoding and
error handler from each pipe. Nothing may read the pipes before this reader
is created. Each pipe is decoded incrementally as it is read, so repeated
calls to `communicate` keep the text already decoded, and an encoded
character split across two reads is held until the rest of it arrives.

The caller owns termination and pipe cleanup if `communicate` raises.

## Signature

```python
WindowsProcessReader(
    self,
    process: subprocess.Popen[str],
)
```

## Constructors

```python
__init__(
    self,
    process: subprocess.Popen[str],
) -> None
```

| Name | Type |
|------|------|
| `process` | `subprocess.Popen[str]` |

## Methods

- [`snapshot()`](https://reference.langchain.com/python/deepagents/backends/_windows_process/WindowsProcessReader/snapshot)
- [`communicate()`](https://reference.langchain.com/python/deepagents/backends/_windows_process/WindowsProcessReader/communicate)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/5568767515b7edc6b106e92d3de4cc65886c1eca/libs/deepagents/deepagents/backends/_windows_process.py#L68)
