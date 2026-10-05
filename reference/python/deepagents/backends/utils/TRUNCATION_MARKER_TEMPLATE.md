---
title: "TRUNCATION_MARKER_TEMPLATE"
description: "Marker standing in for lines dropped from the middle of a head/tail preview."
source: "https://reference.langchain.com/python/deepagents/backends/utils/TRUNCATION_MARKER_TEMPLATE"
category: "reference"
tags: [reference, deepagents, backends, utils, truncation_marker_template]
---

# TRUNCATION_MARKER_TEMPLATE

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/TRUNCATION_MARKER_TEMPLATE)

Marker standing in for lines dropped from the middle of a head/tail preview.

Shared by `_message_eviction._create_content_preview` and the capture wrapper
in `backends.sandbox` so both emit identical marker text.

Never scan preview text for this marker to detect truncation: output can
contain a literal marker line. Producers report marker presence out of band
instead (see `ExecuteOffloadResult.preview_has_truncation_marker`).

Note: `middleware.filesystem._LEGACY_TOO_LARGE_TOOL_MSG` keeps a frozen copy of
the old wording for a deprecated import and deliberately does not use this
template.

## Signature

```python
TRUNCATION_MARKER_TEMPLATE: Final = '... [{omitted_lines} lines truncated] ...'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/backends/utils.py#L180)
