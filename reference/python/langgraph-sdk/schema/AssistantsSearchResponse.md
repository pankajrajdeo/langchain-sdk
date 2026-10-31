---
title: "AssistantsSearchResponse"
description: "Paginated response for assistant search results."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/AssistantsSearchResponse"
category: "reference"
tags: [reference, langgraph-sdk, schema, assistantssearchresponse]
---

# AssistantsSearchResponse

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/AssistantsSearchResponse)

Paginated response for assistant search results.

## Signature

```python
AssistantsSearchResponse()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    assistants: list[Assistant],
    next: str | None,
)
```

| Name | Type |
|------|------|
| `assistants` | `list[Assistant]` |
| `next` | `str \| None` |

## Properties

- `assistants`
- `next`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/schema.py#L282)
