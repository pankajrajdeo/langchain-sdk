---
title: "Noul"
description: "Ask a binary question and receive the probability that its answer is yes."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/Noul"
category: "reference"
tags: [reference, langchain-core, decisions, types, noul]
---

# Noul

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/Noul)

Ask a binary question and receive the probability that its answer is yes.

Use `Noul` when the probability itself is useful to application code, such as
deciding whether a message reports a bug or requests a refund. A value near `1`
indicates strong support for yes, a value near `0` indicates strong support for no,
and a value near `0.5` indicates uncertainty. Noul answers do not include a separate
confidence value.

??? example "Detect an urgent support request"

```python
    from langchain_core.decisions import Noul

    response = classifier.invoke(
        {
            "state": "Production is down. Please help immediately.",
            "questions": {
                "urgent": Noul(
                    instructions="Does this message require an urgent response?"
                )
            },
        }
    )
    urgency = response.nouls["urgent"].noul

    if urgency >= 0.8:
        page_on_call_engineer()
```

## Signature

```python
Noul()
```

## Extends

- `BaseModel`

## Properties

- `model_config`
- `type`
- `instructions`
- `criteria`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/decisions/types.py#L60)
