---
title: "interrupt"
description: "Interrupt the graph with a resumable exception from within a node."
source: "https://reference.langchain.com/python/langgraph/types/interrupt"
category: "reference"
tags: [reference, langgraph, types, interrupt]
---

# interrupt

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/interrupt)

Interrupt the graph with a resumable exception from within a node.

The `interrupt` function enables human-in-the-loop workflows by pausing graph
execution and surfacing a value to the client. This value can communicate context
or request input required to resume execution.

In a given node, the first invocation of this function raises a `GraphInterrupt`
exception, halting execution. The provided `value` is included with the exception
and sent to the client executing the graph.

A client resuming the graph must use the [`Command`][langgraph.types.Command]
primitive to specify a value for the interrupt and continue execution.
The graph resumes from the start of the node, **re-executing** all logic.

If a node contains multiple `interrupt` calls, LangGraph matches resume values
to interrupts based on their order in the node. This list of resume values
is scoped to the specific task executing the node and is not shared across tasks.

To use an `interrupt`, you must enable a checkpointer, as the feature relies
on persisting the graph state.

!!! example

```python
    import uuid
    from typing import Optional
    from typing_extensions import TypedDict

    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.constants import START
    from langgraph.graph import StateGraph
    from langgraph.types import interrupt, Command

    class State(TypedDict):
        """The graph state."""

        foo: str
        human_value: Optional[str]
        """Human value will be updated using an interrupt."""

    def node(state: State):
        answer = interrupt(
            # This value will be sent to the client
            # as part of the interrupt information.
            "what is your age?"
        )
        print(f"> Received an input from the interrupt: {answer}")
        return {"human_value": answer}

    builder = StateGraph(State)
    builder.add_node("node", node)
    builder.add_edge(START, "node")

    # A checkpointer must be enabled for interrupts to work!
    checkpointer = InMemorySaver()
    graph = builder.compile(checkpointer=checkpointer)

    config = {
        "configurable": {
            "thread_id": uuid.uuid4(),
        }
    }

    for chunk in graph.stream({"foo": "abc"}, config):
        print(chunk)

    # > {'__interrupt__': (Interrupt(value='what is your age?', id='45fda8478b2ef754419799e10992af06'),)}

    command = Command(resume="some input from a human!!!")

    for chunk in graph.stream(Command(resume="some input from a human!!!"), config):
        print(chunk)

    # > Received an input from the interrupt: some input from a human!!!
    # > {'node': {'human_value': 'some input from a human!!!'}}
```

## Signature

```python
interrupt(
    value: Any,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `value` | `Any` | Yes | The value to surface to the client when the graph is interrupted. |

## Returns

`Any`

On subsequent invocations within the same node (same task to be precise), returns the value provided during the first invocation

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L851)
