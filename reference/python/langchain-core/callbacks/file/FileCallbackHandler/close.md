---
title: "close"
description: "Close the file if it's open."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/close"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler, close]
---

# close

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/close)

Close the file if it's open.

This method is safe to call multiple times and will only close
the file if it's currently open.

## Signature

```python
close(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/callbacks/file.py#L116)
