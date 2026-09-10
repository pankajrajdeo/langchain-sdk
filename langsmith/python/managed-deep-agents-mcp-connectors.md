---
title: "Connect to MCP servers"
description: "Add tools from remote MCP servers to Managed Deep Agents."
source: "https://docs.langchain.com/langsmith/python/managed-deep-agents-mcp-connectors"
category: "docs"
tags: [docs, langsmith, managed-deep-agents-mcp-connectors]
---

# Connect to MCP servers

> Add tools from remote MCP servers to Managed Deep Agents.

Connect a managed deep agent to remote [Model Context Protocol (MCP)](../../deepagents/mcp.md) servers to add their tools to the agent. Managed Deep Agents creates the MCP client and loads the tools.

Most remote MCP servers require authentication. A [connection](managed-deep-agents-connections.md) supplies it, and declaring the connection as user-owned makes each caller authorize their own account.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Project structure

Declare MCP servers in a module directly under `tools/`:

```text
my-agent/
  agent.py
  tools/
    mcp.py
```

The module must export a module-level `mcp`.

## Add MCP servers

Use `define_mcp` to declare one or more remote servers:

**tools/mcp.py**

```python
from managed_deepagents import define_mcp

mcp = define_mcp(
    servers={
        "langchainDocs": {
            "transport": "http",
            "url": "https://docs.langchain.com/mcp",
        },
    },
)
```

Managed Deep Agents supports Streamable HTTP (`"http"`) and legacy SSE (`"sse"`) transports. Stdio MCP servers are not supported. Expose a stdio server over HTTP or implement its operation as an [authored tool](managed-deep-agents-tools.md).

## Select tools

By default, Managed Deep Agents exposes every tool from each server. To expose only selected tools, set an allowlist inside that server's configuration:

```python
{
    "transport": "http",
    "url": "https://docs.langchain.com/mcp",
    "include_tools": ["search_docs_by_lang_chain"],
}
```

To expose every tool except selected tools, replace `include_tools` with `exclude_tools`.

You can use both options together. The denylist applies after the allowlist, and the same tool cannot appear in both lists.

Selection uses raw MCP tool names before Managed Deep Agents prefixes them. Tool names are prefixed with the server name by default to avoid collisions. For example, the `search_docs_by_lang_chain` tool from the `langchainDocs` server is exposed as `langchainDocs__search_docs_by_lang_chain`.

## Configure MCP servers

Each server supports the following core options:

| Option                                            | Description                                                                        |
| ------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `transport`                                       | Required. Use `http` for Streamable HTTP or `sse` for legacy SSE.                  |
| `url`                                             | Required. The remote MCP endpoint URL.                                             |
| `headers`                                         | Static headers to send to the server.                                              |
| `include_tools` / `includeTools`                  | Raw MCP tool names to expose.                                                      |
| `exclude_tools` / `excludeTools`                  | Raw MCP tool names to hide.                                                        |
| `default_tool_timeout` / `defaultToolTimeout`     | Timeout for each tool call, in seconds for Python and milliseconds for TypeScript. |
| `automatic_sse_fallback` / `automaticSSEFallback` | For HTTP, allow the client to fall back to SSE.                                    |
| `reconnect`                                       | For SSE, configure reconnection behavior.                                          |

The MCP definition also accepts these options:

| Option                                                               | Default | Description                                               |
| -------------------------------------------------------------------- | ------- | --------------------------------------------------------- |
| `prefix_tool_name_with_server_name` / `prefixToolNameWithServerName` | `true`  | Prefix each tool with `{server}__`.                       |
| `throw_on_load_error` / `throwOnLoadError`                           | `true`  | Fail loading instead of starting with a partial tool set. |

## Compare MCP with other capabilities

* **MCP servers** provide remotely hosted tools.
* **[Authored tools](managed-deep-agents-tools.md)** implement application logic in the project and are passed through the agent definition.
* **[Channels](managed-deep-agents-channels.md)** receive external messages that start agent runs and deliver responses.

## Use MCP servers that require authentication

If an MCP server requires credentials, declare a connection on the server config and create that connection in the workspace.

* **MCP OAuth**: For servers that advertise OAuth and support automatic client registration, create with `mda connections create <slug>` (inferred from the MCP declaration) or `mda connections create <slug> --mcp <url>`. You do not supply a client ID or secret.
* **Opaque secret or general OAuth**: For a static API key, or for a BYOT OAuth app you register yourself, create an opaque secret or general OAuth connection, then set the server's `connection` option to `connections.get(...)`.

For create modes, owners, and runtime authorization, see [Manage connections](managed-deep-agents-connections.md).

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-mcp-connectors.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
