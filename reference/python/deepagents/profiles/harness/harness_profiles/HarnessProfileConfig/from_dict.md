---
title: "from_dict"
description: "Construct a config object from a plain dict."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/from_dict"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig, from_dict]
---

# from_dict

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/from_dict)

Construct a config object from a plain dict.

## Signature

```python
from_dict(
    cls,
    data: Mapping[str, Any],
) -> HarnessProfileConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `data` | `Mapping[str, Any]` | Yes | A mapping with any subset of the serializable `HarnessProfileConfig` fields. Unknown keys raise `TypeError`. |

## Returns

`HarnessProfileConfig`

A new `HarnessProfileConfig` populated from `data`.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L373)
