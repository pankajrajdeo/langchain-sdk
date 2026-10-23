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
    preview_has_truncation_marker: bool = False,
)
```

## Constructors

```python
__init__(
    self,
    offloaded: bool,
    response: ExecuteResponse,
    preview_has_truncation_marker: bool = False,
) -> None
```

| Name | Type |
|------|------|
| `offloaded` | `bool` |
| `response` | `ExecuteResponse` |
| `preview_has_truncation_marker` | `bool` |

## Properties

- `offloaded`
- `response`
- `preview_has_truncation_marker`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/protocol.py#L850)
