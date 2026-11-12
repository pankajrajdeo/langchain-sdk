---
title: "BaseDecisionModel"
description: "Answer typed questions about text, messages, or structured state."
source: "https://reference.langchain.com/python/langchain-core/decisions/base/BaseDecisionModel"
category: "reference"
tags: [reference, langchain-core, decisions, base, basedecisionmodel]
---

# BaseDecisionModel

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/base/BaseDecisionModel)

Answer typed questions about text, messages, or structured state.

A decision model evaluates shared state against one or more questions and returns
typed answers: a probability for a `Noul`, a selected label for a `Choice`, an
expected level for a `Score`, and a location for a `Box`. Answers keep their
probability distributions and confidence so applications can choose their own
thresholds.

Subclasses implement `_classify`, and optionally `_aclassify`, to call a provider.
This class handles callbacks, tracing metadata, and
token-usage reporting.

??? example "Implement a decision model"

```python
    from langchain_core.decisions import BaseDecisionModel, ClassifierResponse

    class MyDecisionModel(BaseDecisionModel):
        model: str = "my-model"

        @property
        def _provider(self) -> str:
            return "my_provider"

        def _classify(self, state, questions):
            body = my_client.classify(state=state, questions=questions)
            return ClassifierResponse.model_validate(body)
```

## Signature

```python
BaseDecisionModel(
    self,
    args: Any = (),
    kwargs: Any = {},
)
```

## Extends

- `RunnableSerializable[ClassifierRequest, ClassifierResponse]`
- `ABC`

## Properties

- `model`

## Methods

- [`invoke()`](https://reference.langchain.com/python/langchain-core/decisions/base/BaseDecisionModel/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/decisions/base/BaseDecisionModel/ainvoke)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/decisions/base.py#L24)
