---
title: "when"
description: "Optional predicate controlling whether to interrupt for a given tool call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig/when"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, interruptonconfig, when]
---

# when

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptOnConfig/when)

Optional predicate controlling whether to interrupt for a given tool call.

Receives a `ToolCallRequest` and returns `True` to interrupt or `False` to
auto-approve. Works in both `"batch"` and `"per_call"` modes.

In `"batch"` mode the request is constructed with `tool=None` and
`runtime` set to the node-level `Runtime` (not a `ToolRuntime`), so
`request.runtime.tool_call_id` and `request.runtime.tools` are not available.
In `"per_call"` mode the full `ToolCallRequest` from `wrap_tool_call` is passed.

## Signature

```python
when: NotRequired[Callable[[ToolCallRequest], bool]]
```

## Description

**Example:**

```python
# Only interrupt delete_file calls targeting /etc
config = InterruptOnConfig(
    allowed_decisions=["approve", "reject"],
    when=lambda req: req.tool_call["args"].get("path", "").startswith("/etc"),
)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L195)
