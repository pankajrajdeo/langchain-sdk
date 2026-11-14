---
title: "to_dict"
description: "Dump this sub-profile to a plain dict."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/to_dict"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, generalpurposesubagentprofile, to_dict]
---

# to_dict

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/GeneralPurposeSubagentProfile/to_dict)

Dump this sub-profile to a plain dict.

Only fields with non-`None` values are emitted so the serialized form
round-trips cleanly without forcing `None` defaults into the config.

## Signature

```python
to_dict(
    self,
) -> dict[str, Any]
```

## Returns

`dict[str, Any]`

A plain dict with at most `enabled`, `description`, and
`system_prompt` keys.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L138)
