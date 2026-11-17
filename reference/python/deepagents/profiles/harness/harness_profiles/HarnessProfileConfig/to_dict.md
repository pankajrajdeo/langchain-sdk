---
title: "to_dict"
description: "Dump this config to plain dict/list/scalar values."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/to_dict"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofileconfig, to_dict]
---

# to_dict

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfileConfig/to_dict)

Dump this config to plain dict/list/scalar values.

Suitable for `json.dumps` or `yaml.safe_dump`. Fields at their
default are omitted so the output stays minimal and round-trips
cleanly through `from_dict`.

## Signature

```python
to_dict(
    self,
) -> dict[str, Any]
```

## Returns

`dict[str, Any]`

A plain dict containing only the fields set on this config.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L338)
