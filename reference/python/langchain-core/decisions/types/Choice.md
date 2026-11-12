---
title: "Choice"
description: "Select one label from a fixed set of alternatives."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/Choice"
category: "reference"
tags: [reference, langchain-core, decisions, types, choice]
---

# Choice

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/Choice)

Select one label from a fixed set of alternatives.

Use `Choice` for categorical decisions with no inherent ordering, such as routing a
support request, detecting a document type, or selecting an intent. The answer
includes the selected label, a probability for every supplied label, and a
confidence value.

??? example "Route a support request"

```python
    from langchain_core.decisions import Choice

    response = classifier.invoke(
        {
            "state": "Stripe fails whenever I connect my account.",
            "questions": {
                "department": Choice(
                    instructions="Which team should handle this request?",
                    criteria={
                        "billing": "Payment, invoice, or subscription issues.",
                        "technical": "Product bugs or integration failures.",
                        "sales": "Pricing or purchasing questions.",
                    },
                )
            },
        }
    )
    department = response.choices["department"]

    if department.confidence >= 0.7:
        route_to(department.choice)
    else:
        route_to_human_triage()
```

## Signature

```python
Choice()
```

## Extends

- `BaseModel`

## Properties

- `model_config`
- `type`
- `criteria`
- `instructions`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/decisions/types.py#L107)
