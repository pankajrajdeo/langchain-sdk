---
title: "langsmith/tool-gateway-api/calling-tools"
description: "Index of 7 pages and 0 subdirectories under langsmith/tool-gateway-api/calling-tools."
category: "index"
tags: [index, langsmith, tool-gateway-api, calling-tools]
---

# langsmith/tool-gateway-api/calling-tools

7 pages here.

## Files

- [End an MCP session with a server](end-an-mcp-session-with-a-server.md) - Proxies MCP Streamable HTTP requests to one MCP server or built-in. Requires mcp-servers:invoke. Prefer a tool kit for agents and MCP clients. If you aren't connected, you get 428 or an MCP URL...
- [Get the linked identity provider](get-the-linked-identity-provider.md) - Returns the identity provider whose access tokens can authenticate MCP calls to this workspace. Requires workspaces:integrations:read. Call as yourself.
- [Link your identity provider](link-your-identity-provider.md) - Links an enabled identity provider in this workspace so its access tokens can authenticate MCP calls, replacing any current link. Requires workspaces:integrations:manage. Call as yourself.
- [Open an MCP event stream from a server](open-an-mcp-event-stream-from-a-server.md) - Proxies MCP Streamable HTTP requests to one MCP server or built-in. Requires mcp-servers:invoke. Prefer a tool kit for agents and MCP clients. If you aren't connected, you get 428 or an MCP URL...
- [Send an MCP message to a server](send-an-mcp-message-to-a-server.md) - Proxies MCP Streamable HTTP requests to one MCP server or built-in. Requires mcp-servers:invoke. Prefer a tool kit for agents and MCP clients. If you aren't connected, you get 428 or an MCP URL...
- [Send an MCP message to a tool kit](send-an-mcp-message-to-a-tool-kit.md) - Serves a tool kit as one stateless MCP endpoint: initialize, server/discover, ping, tools/list, and tools/call. Requires mcp-servers:invoke. Tool lists are cached for 2 hours and served stale for up...
- [Unlink your identity provider](unlink-your-identity-provider.md) - Unlinks the identity provider so its access tokens no longer authenticate MCP calls; the integration is kept. Requires workspaces:integrations:manage. Call as yourself. Returns 204 if no provider is...
