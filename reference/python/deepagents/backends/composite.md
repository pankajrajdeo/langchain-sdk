---
title: "composite"
description: "Composite backend that routes file operations by path prefix."
source: "https://reference.langchain.com/python/deepagents/backends/composite"
category: "reference"
tags: [reference, deepagents, backends, composite]
---

# composite

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite)

Composite backend that routes file operations by path prefix.

Routes operations to different backends based on path prefixes. Use this when
you need different storage strategies for different paths (e.g., state for
temp files, persistent store for memories).

## Properties

- `GlobTruncationReason`

## Methods

- [`execute_accepts_timeout()`](https://reference.langchain.com/python/deepagents/backends/composite/execute_accepts_timeout)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/composite.py)
