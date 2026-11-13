---
title: "check_openrouter_version"
description: "Raise if the installed langchain-openrouter is below the minimum."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/_openrouter/check_openrouter_version"
category: "reference"
tags: [reference, deepagents, profiles, provider, openrouter, check_openrouter_version]
---

# check_openrouter_version

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/_openrouter/check_openrouter_version)

Raise if the installed `langchain-openrouter` is below the minimum.

If the package is not installed at all the check is skipped;
`init_chat_model` will surface its own missing-dependency error downstream.

## Signature

```python
check_openrouter_version() -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/profiles/provider/_openrouter.py#L89)
