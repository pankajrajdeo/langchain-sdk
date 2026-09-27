---
title: "CompatBlock"
description: "Internal working type for a content block."
source: "https://reference.langchain.com/python/langchain-core/language_models/_compat_bridge/CompatBlock"
category: "reference"
tags: [reference, langchain-core, language_models, compat_bridge, compatblock]
---

# CompatBlock

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/_compat_bridge/CompatBlock)

Internal working type for a content block.

The bridge works with plain dicts internally because two separate but
structurally similar `ContentBlock` Unions exist — one in
`langchain_core.messages.content` (returned by `msg.content_blocks`),
one in `langchain_protocol.protocol` (the wire/event shape).  They are
not mypy-compatible despite being near-isomorphic.  Passing through
`dict[str, Any]` launders between them.  See `_to_protocol_block` for
the single seam where the laundering cast lives.

## Signature

```python
CompatBlock = dict[str, Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/language_models/_compat_bridge.py#L78)
