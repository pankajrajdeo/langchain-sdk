---
title: "Priority"
description: "Decide the priority settings of your LangGraph application's threads."
source: "https://reference.langchain.com/python/langgraph-sdk/priority/Priority"
category: "reference"
tags: [reference, langgraph-sdk, priority]
---

# Priority

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/priority/Priority)

Decide the priority settings of your LangGraph application's threads.

.. warning::
    This API is in beta and may change in future versions.

To use, create a separate Python file and add the path to the file to your
LangGraph API configuration file (`langgraph.json`). Within that file, create
an instance of the Priority class and register an assign function with
`@priority.assign`.

Example `langgraph.json` file:

```json
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./my_agent/agent.py:graph"
  },
  "env": ".env",
  "priority": {
    "path": "./priority.py:priority"
  }
}
```

The server calls the assign function at the first run on a thread with no
settings, which can come long after the thread was created, and stores the
settings it returns on the thread. Later runs on the thread use the stored
settings. The function can be called more than once for one thread, for
example after it raises, and only one result is stored, so keep it free of
side effects.

???+ example "Basic Usage"

```python
    from langgraph_sdk import Priority, PriorityContext, PrioritySettings

    priority = Priority()

    @priority.assign
    async def assign(ctx: PriorityContext) -> PrioritySettings | None:
        return {
            "priority": 3 if "premium" in ctx.permissions else 0,
            # Stored unencrypted, so an opaque ID rather than personal data.
            "fairness_group": ctx.user["org_id"],
        }
```

## Signature

```python
Priority(
    self,
)
```

## Constructors

```python
__init__(
    self,
) -> None
```

## Properties

- `types`

## Methods

- [`assign()`](https://reference.langchain.com/python/langgraph-sdk/priority/Priority/assign)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/priority/__init__.py#L62)
