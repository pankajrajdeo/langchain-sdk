---
title: "deprecation"
description: "Adapter for langchain_core's private deprecation helpers."
source: "https://reference.langchain.com/python/deepagents/_api/deprecation"
category: "reference"
tags: [reference, deepagents, api, deprecation]
---

# deprecation

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/_api/deprecation)

Adapter for `langchain_core`'s private deprecation helpers.

Centralizes the import surface so an upstream rename or move is a one-file
change.

Re-exports:
- `deprecated`: decorator for callables, classes, and properties.
- `warn_deprecated`: helper for parameter/value-level deprecations where the
    callable itself isn't being deprecated. Forwards to the upstream helper
    with caller-controlled stack attribution.
- `suppress_langchain_deprecation_warning`: context manager that silences
    emissions from this module's helpers (use sparingly).
- `LangChainDeprecationWarning`: warning class emitted by the helpers above
    (subclass of `DeprecationWarning`).

## Methods

- [`warn_deprecated()`](https://reference.langchain.com/python/deepagents/_api/deprecation/warn_deprecated)
- [`reset_deprecation_dedupe()`](https://reference.langchain.com/python/deepagents/_api/deprecation/reset_deprecation_dedupe)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/_api/deprecation.py)
