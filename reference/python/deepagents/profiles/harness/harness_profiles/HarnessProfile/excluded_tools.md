---
title: "excluded_tools"
description: "Tool names to remove from the tool set for this profile."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/excluded_tools"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofile, excluded_tools]
---

# excluded_tools

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/excluded_tools)

Tool names to remove from the tool set for this profile.

Applied via a tool-exclusion middleware after tool-injecting middleware
has run, so it can remove both user-supplied tools and tools added by
Deep Agents middleware from the visible tool set.

When profiles are merged, exclusions are additive rather than replacing
each other. For example, if a provider profile excludes `execute` and an
exact-model profile excludes `grep`, the resolved profile excludes both
tools.

Exclusions are model-facing calibration resolved per model; they are not a
security surface.

## Signature

```python
excluded_tools: frozenset[str] = frozenset()
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L613)
