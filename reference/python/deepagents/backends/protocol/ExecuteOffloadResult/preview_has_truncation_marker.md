---
title: "preview_has_truncation_marker"
description: "Whether the preview contains a ... [N lines truncated] ... marker."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteOffloadResult/preview_has_truncation_marker"
category: "reference"
tags: [reference, deepagents, backends, protocol, executeoffloadresult, preview_has_truncation_marker]
---

# preview_has_truncation_marker

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteOffloadResult/preview_has_truncation_marker)

Whether the preview contains a `... [N lines truncated] ...` marker.

Set by the code that builds the preview. This is the only reliable way to
know the marker was inserted, as the command output itself can contain
a line that looks the same (scanning the text is unsafe).

This flag covers only the `... [N lines truncated] ...` marker. A preview
may disclose other losses through its own in-band clip notices, which need
no flag because they carry their own explanation; see
`_build_capture_execute_cmd` in `backends.sandbox` for the wording.

When `offloaded` is `False`, this flag is always `False`.

## Signature

```python
preview_has_truncation_marker: bool = False
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/protocol.py#L876)
