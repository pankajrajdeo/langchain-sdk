---
title: "langsmith/tool-gateway-api/exposing-tools"
description: "Index of 6 pages and 0 subdirectories under langsmith/tool-gateway-api/exposing-tools."
category: "index"
tags: [index, langsmith, tool-gateway-api, exposing-tools]
---

# langsmith/tool-gateway-api/exposing-tools

6 pages here.

## Files

- [Create a tool kit](create-a-tool-kit.md) - Creates a tool kit, a named set of tools served through one MCP endpoint. Requires mcp-servers:invoke, plus mcp-servers:create for a workspace kit (the default), or mcp-servers:create-personal or...
- [Delete a tool kit](delete-a-tool-kit.md) - Deletes a tool kit; its MCP servers and user credentials are kept. Requires mcp-servers:delete for a workspace kit. Only the owner can delete a personal kit, with mcp-servers:create-personal or...
- [Get a tool kit](get-a-tool-kit.md) - Returns a workspace tool kit or one of your personal tool kits, with its tools. Requires mcp-servers:read. Call as yourself.
- [List tool kits](list-tool-kits.md) - Lists the workspace's tool kits and your personal tool kits in creation order. Requires mcp-servers:read. Call as yourself. Items omit tools; get a kit to see its tools.
- [Refresh a tool kit's tools](refresh-a-tool-kits-tools.md) - Refreshes a tool kit's MCP servers and waits for the cache to update. Requires mcp-servers:update and mcp-servers:invoke, and no ABAC deny policy on MCP servers or built-ins. Call as yourself. Also...
- [Update a tool kit](update-a-tool-kit.md) - Updates the fields you send and returns the tool kit. Requires mcp-servers:invoke, plus mcp-servers:update for a workspace kit, or mcp-servers:create-personal or mcp-servers:create for a personal...
