---
title: "GlobTruncationReason"
description: "Why a GlobResult is incomplete."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/GlobTruncationReason"
category: "reference"
tags: [reference, deepagents, backends, protocol, globtruncationreason]
---

# GlobTruncationReason

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/GlobTruncationReason)

Why a `GlobResult` is incomplete.

The distinction decides what advice is useful to the caller:

- `budget`: the walk hit its time limit or match cap. Narrowing the pattern or
  the path surfaces the rest.
- `unreadable`: a subtree could not be read (e.g. permissions). Narrowing will
  *never* surface those files, so advising it sends the caller in a loop.
- `transport`: the sandbox transport clipped the output.

## Signature

```python
GlobTruncationReason = Literal['budget', 'unreadable', 'transport']
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/protocol.py#L368)
