---
title: "PREVIEW_LINE_CHAR_LIMIT"
description: "Per-line character budget for preview lines."
source: "https://reference.langchain.com/python/deepagents/middleware/_message_eviction/PREVIEW_LINE_CHAR_LIMIT"
category: "reference"
tags: [reference, deepagents, middleware, message_eviction, preview_line_char_limit]
---

# PREVIEW_LINE_CHAR_LIMIT

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/_message_eviction/PREVIEW_LINE_CHAR_LIMIT)

Per-line character budget for preview lines.

Bounds previews of few-but-huge lines (a `.jsonl` dump, a minified bundle).
Clipping cuts within a shown line rather than dropping whole lines, so it is
reported separately from `lines_omitted`.

Keep below `backends.utils.MAX_LINE_LENGTH`, or clipped lines also pick up that
renderer's `N.1` continuation gutters and `_CAVEAT_CLIPPED_LINES` no longer
describes what the model sees.

## Signature

```python
PREVIEW_LINE_CHAR_LIMIT: Final = 1000
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/_message_eviction.py#L42)
