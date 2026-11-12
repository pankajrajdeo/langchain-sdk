---
title: "Score"
description: "Evaluate state against an ordered rubric."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/Score"
category: "reference"
tags: [reference, langchain-core, decisions, types, score]
---

# Score

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/Score)

Evaluate state against an ordered rubric.

Use `Score` when the answer lies on a spectrum whose levels can be described, such
as severity, urgency, or customer frustration. Criteria are numbered from zero in
their supplied order. The returned score is an expected value and may fall between
integer levels; the full probability distribution remains available for custom
decision logic.

??? example "Score customer frustration"

```python
    from langchain_core.decisions import Score

    response = classifier.invoke(
        {
            "state": "This has failed three times. Fix it now.",
            "questions": {
                "frustration": Score(
                    instructions="How frustrated does the customer appear?",
                    criteria=[
                        "Calm and neutral.",
                        "Concerned but civil.",
                        "Very angry or using strong language.",
                    ],
                )
            },
        }
    )
    frustration = response.scores["frustration"]

    print(frustration.score)  # May be fractional, for example 1.35.
    print(frustration.legend)  # The original zero-based rubric.
    print(frustration.probabilities)  # Probability for each rubric level.
```

## Signature

```python
Score()
```

## Extends

- `BaseModel`

## Properties

- `model_config`
- `type`
- `criteria`
- `instructions`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/decisions/types.py#L160)
