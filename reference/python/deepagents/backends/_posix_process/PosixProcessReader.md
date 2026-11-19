---
title: "PosixProcessReader"
description: "Collect text-mode output across polling attempts, joining only at EOF."
source: "https://reference.langchain.com/python/deepagents/backends/_posix_process/PosixProcessReader"
category: "reference"
tags: [reference, deepagents, backends, posix_process, posixprocessreader]
---

# PosixProcessReader

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/_posix_process/PosixProcessReader)

Collect text-mode output across polling attempts, joining only at EOF.

Unlike `Popen.communicate`, a timed-out attempt does not build a snapshot of
all output read so far. Chunks stay buffered for the next attempt, including
partial encoded characters and newline sequences. Nothing else may read the
pipes while this reader is in use.

The caller owns termination and pipe cleanup if `communicate` raises.

## Signature

```python
PosixProcessReader(
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

- [`snapshot()`](https://reference.langchain.com/python/deepagents/backends/_posix_process/PosixProcessReader/snapshot)
- [`communicate()`](https://reference.langchain.com/python/deepagents/backends/_posix_process/PosixProcessReader/communicate)
- [`drain()`](https://reference.langchain.com/python/deepagents/backends/_posix_process/PosixProcessReader/drain)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/backends/_posix_process.py#L23)
