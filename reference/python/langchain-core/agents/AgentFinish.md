---
title: "AgentFinish"
description: "Final return value of an ActionAgent."
source: "https://reference.langchain.com/python/langchain-core/agents/AgentFinish"
category: "reference"
tags: [reference, langchain-core, agents, agentfinish]
---

# AgentFinish

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/agents/AgentFinish)

Final return value of an `ActionAgent`.

Agents return an `AgentFinish` when they have reached a stopping condition.

## Signature

```python
AgentFinish(
    self,
    return_values: dict[Any, Any],
    log: str,
    kwargs: Any = {},
)
```

## Extends

- `Serializable`

## Constructors

```python
__init__(
    self,
    return_values: dict[Any, Any],
    log: str,
    kwargs: Any = {},
)
```

| Name | Type |
|------|------|
| `return_values` | `dict[Any, Any]` |
| `log` | `str` |
| `kwargs` | `Any` |

## Properties

- `return_values`
- `log`
- `type`
- `messages`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/agents/AgentFinish/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/agents/AgentFinish/get_lc_namespace)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/agents.py#L148)
