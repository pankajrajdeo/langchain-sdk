---
title: "NodeError"
description: "Failure context passed to a node-level error handler."
source: "https://reference.langchain.com/python/langgraph/errors/NodeError"
category: "reference"
tags: [reference, langgraph, errors, nodeerror]
---

# NodeError

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/errors/NodeError)

Failure context passed to a node-level error handler.

Inject by adding a parameter typed `NodeError` to a handler registered via
`StateGraph.add_node(..., error_handler=...)`:

```python
def handler(state: State, error: NodeError) -> Command:
    return Command(update={"status": f"recovered from {error.node}: {error.error}"})
```

## Signature

```python
NodeError(
    self,
    node: str,
    error: BaseException,
)
```

## Constructors

```python
__init__(
    self,
    node: str,
    error: BaseException,
) -> None
```

| Name | Type |
|------|------|
| `node` | `str` |
| `error` | `BaseException` |

## Properties

- `node`
- `error`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/errors.py#L190)
