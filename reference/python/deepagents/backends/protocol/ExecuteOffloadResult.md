---
title: "ExecuteOffloadResult"
description: "Result of [BaseSandbox.execute_with_offload][deepagents.backends.sandbox.BaseSandbox.execute_with_offload]."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteOffloadResult"
category: "reference"
tags: [reference, deepagents, backends, protocol, executeoffloadresult]
---

# ExecuteOffloadResult

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteOffloadResult)

Result of [`BaseSandbox.execute_with_offload`][deepagents.backends.sandbox.BaseSandbox.execute_with_offload].

`offloaded` describes the capture mechanism and is kept off `ExecuteResponse`
(which an ordinary `execute` never sets).

## Signature

```python
ExecuteOffloadResult(
    self,
    offloaded: bool,
    response: ExecuteResponse,
)
```

## Constructors

```python
__init__(
    self,
    offloaded: bool,
    response: ExecuteResponse,
) -> None
```

| Name | Type |
|------|------|
| `offloaded` | `bool` |
| `response` | `ExecuteResponse` |

## Properties

- `offloaded`
- `response`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/protocol.py#L850)
