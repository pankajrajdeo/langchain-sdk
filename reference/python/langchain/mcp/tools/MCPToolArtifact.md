---
title: "MCPToolArtifact"
description: "Artifact attached to the ToolMessage produced by an MCP tool call."
source: "https://reference.langchain.com/python/langchain/mcp/tools/MCPToolArtifact"
category: "reference"
tags: [reference, langchain, mcp, tools, mcptoolartifact]
---

# MCPToolArtifact

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/tools/MCPToolArtifact)

Artifact attached to the `ToolMessage` produced by an MCP tool call.

Wrapping the structured content in a `TypedDict` leaves room for further
MCP result fields without changing the artifact's shape.

## Signature

```python
MCPToolArtifact()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    structured_content: Any,
)
```

| Name | Type |
|------|------|
| `structured_content` | `Any` |

## Properties

- `structured_content`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/fbb8a35da7023ac0382c3b22f047337861bd3486/libs/langchain_v1/langchain/mcp/tools.py#L59)
