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
auto-approve. The predicate is called during `after_model` before the tool
call is added to the batched human-in-the-loop request.

The request is constructed with `tool=None` and a new `ToolRuntime`. The
`ToolRuntime` copies `context`, `store`, `stream_writer`, `execution_info`,
and `server_info` from the node-level `Runtime`, while `tool_call_id` is
populated from the current tool call. The `tools` argument is not supplied,
so it uses its default empty list.

In `per_call` mode the predicate runs in `wrap_tool_call` and receives the real
`ToolCallRequest`, with `tool` and the tool's `ToolRuntime` set.

In both modes the predicate runs again when the run resumes, so it must return the
same answer for the same call. If it returns `False` on resume, the reviewer's
answer is skipped and the tool runs, even if they rejected it. In `batched` mode,
if it flips for only some of the reviewed calls, the decisions no longer line up
with the calls and resuming raises a `ValueError`.

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/fbb8a35da7023ac0382c3b22f047337861bd3486/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L356)
