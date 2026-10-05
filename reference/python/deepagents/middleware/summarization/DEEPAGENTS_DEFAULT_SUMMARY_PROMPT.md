---
title: "DEEPAGENTS_DEFAULT_SUMMARY_PROMPT"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/DEEPAGENTS_DEFAULT_SUMMARY_PROMPT"
category: "reference"
tags: [reference, deepagents, middleware, summarization, deepagents_default_summary_prompt]
---

# DEEPAGENTS_DEFAULT_SUMMARY_PROMPT

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/DEEPAGENTS_DEFAULT_SUMMARY_PROMPT)

## Signature

```python
DEEPAGENTS_DEFAULT_SUMMARY_PROMPT = DEFAULT_SUMMARY_PROMPT.replace('\n<messages>\n', f'\n{_MEDIA_REFERENCE_SUMMARY_PROMPT}\n\n<messages>\n', 1)
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/middleware/summarization.py#L113)
