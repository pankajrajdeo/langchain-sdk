---
title: "MCPAdapterTarget"
description: "Type Alias in langchain"
source: "https://reference.langchain.com/python/langchain/mcp/adapter/MCPAdapterTarget"
category: "reference"
tags: [reference, langchain, mcp, adapter, mcpadaptertarget]
---

# MCPAdapterTarget

> **Type Alias** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/adapter/MCPAdapterTarget)

Anything `MCPAdapter` accepts as its `target`.

Every transport `fastmcp.Client` accepts, plus a pre-built `fastmcp.Client`.

A `str` target is the one member narrowed relative to `fastmcp.Client`: it must
be an `http`/`https` URL. Local servers are reached through `Path`, an explicit
transport, or `MCPConfig` — see `MCPAdapter`.

`ClientGroup` is the one member `fastmcp.Client` does not accept at all, since a
group is a peer of `Client` rather than a transport it could wrap.

## Signature

```python
MCPAdapterTarget: TypeAlias = FastMCPClient[Any] | ClientGroup | ClientTransport | FastMCP | MCPServer | AnyUrl | Path | MCPConfig | dict[str, Any] | str
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/mcp/adapter.py#L47)
