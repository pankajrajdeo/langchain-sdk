---
title: "ExecuteResponse"
description: "Result of code execution."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteResponse"
category: "reference"
tags: [reference, deepagents, backends, protocol, executeresponse]
---

# ExecuteResponse

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteResponse)

Result of code execution.

Simplified schema optimized for LLM consumption.

## Signature

```python
ExecuteResponse(
    self,
    output: str,
    exit_code: int | None = None,
    truncated: bool = False,
)
```

## Constructors

```python
__init__(
    self,
    output: str,
    exit_code: int | None = None,
    truncated: bool = False,
) -> None
```

| Name | Type |
|------|------|
| `output` | `str` |
| `exit_code` | `int \| None` |
| `truncated` | `bool` |

## Properties

- `output`
- `exit_code`
- `truncated`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/protocol.py#L809)
