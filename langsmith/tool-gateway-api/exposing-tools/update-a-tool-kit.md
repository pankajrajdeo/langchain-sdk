---
title: "Update a tool kit"
description: "Updates the fields you send and returns the tool kit. Requires mcp-servers:invoke, plus mcp-servers:update for a workspace kit, or mcp-servers:create-personal or mcp-servers:create for a personal..."
source: "https://docs.langchain.com/langsmith/tool-gateway-api/exposing-tools/update-a-tool-kit"
category: "docs"
tags: [docs, langsmith, tool-gateway-api, exposing-tools, update-a-tool-kit]
---

# Update a tool kit

> Updates the fields you send and returns the tool kit. Requires mcp-servers:invoke, plus mcp-servers:update for a workspace kit, or mcp-servers:create-personal or mcp-servers:create for a personal kit. Call as yourself. Sending tools replaces the selection (an empty array or null removes all) and stores tool definitions as you list them; a listing failure doesn't fail the write. A kit keeps its scope: only a personal kit can link personal servers.

## OpenAPI

**/langsmith/tool-gateway-openapi.json patch /v1/managed-tools/kits/{kit_id}**

````yaml
openapi: 3.1.0
info:
  description: >-
    LangSmith Tool Gateway lets your applications, agents, and MCP clients call
    MCP tools with each caller's own credentials.

    ## Start here

    1. Register an MCP server or select a built-in integration.

    2. Connect each user's OAuth account or API key when the integration
    requires one.

    3. Optionally create a tool kit containing selected tools.

    4. Call the server or tool kit MCP endpoint from your application, agent, or
    development environment.

    ## API surfaces

    **Management APIs** configure Tool Gateway: `/servers` registers and lists
    MCP servers, `/servers/{id}/credential` manages the current user's
    credential, `/kits` manages curated tool kits, and `/oidc-connection` links
    your identity provider.

    **MCP APIs** discover and invoke tools through standard MCP methods such as
    `tools/list` and `tools/call`: `/servers/{id}/mcp` exposes one server and
    `/kits/{kit_id}/mcp` exposes a tool kit.

    ## Choose who you're calling as

    | You call as | Send |

    | --- | --- |

    | Yourself | A personal `X-Api-Key`, or `Authorization: Bearer
    {langsmith_token}`, plus `X-Tenant-Id` |

    | A user, from your trusted backend | A workspace `X-Api-Key`, the user's
    `Authorization: Bearer {oidc_token}` (or `X-LangSmith-Identity`), and
    `X-Tenant-Id`. Listing servers and MCP calls only |

    | An agent | An API key bound to the agent's environment as `X-Api-Key`,
    plus `X-Tenant-Id` |

    | A profile | `X-Api-Key`, `X-LangSmith-Profile`, and `X-Tenant-Id`.
    Requires workspaces:credentials:use or agent-auth-credentials:use |

    | A user, with your identity provider | The user's `Authorization: Bearer
    {oidc_token}` alone. MCP calls only; built-ins also need `X-Tenant-Id` |

    `X-Tenant-Id` selects a workspace; it does not authenticate you. Service
    keys are not supported, except LangSmith's internal Agent Builder service
    key, which may list servers and make MCP calls.

    ## When you're not connected yet

    An MCP call that needs your credential returns 428 with a
    `verification_url`. Open it, connect, and retry. If your client declares
    `elicitation.url`, you get an MCP URL elicitation instead: a -32042 error on
    a 2025-11-25 `initialize`, or an `input_required` result on a 2026-07-28
    `tools/call`. Each names its connection in
    `_meta["com.langchain.langsmith/credential"]`, with `auth_id`, the session
    to check for completion. An agent or profile gets 409 instead; an admin
    connects it.

    ## When a call needs approval

    An approval policy can require your OK before a tool runs. Tool Gateway asks
    through an MCP form elicitation on protocol 2026-07-28 or later and runs the
    call when you accept it on retry. A client that can't show the form gets
    403.

    ## Search mode

    `/kits/{kit_id}/mcp?mode=search` lists three tools, `search_tools`,
    `get_tool`, and `call_tool`, instead of every tool. Use it when your host
    puts every listed tool in the model prompt, for example with the me kit
    (`kit_id` = `me`). Calling a tool by name works in both modes.

    Tool Gateway must be enabled for the organization. Endpoint descriptions
    list the required workspace permissions.
  title: LangSmith Tool Gateway API
  contact: {}
  version: v1
servers:
  - url: https://api.smith.langchain.com
    description: GCP US
  - url: https://eu.api.smith.langchain.com
    description: GCP EU
  - url: https://apac.api.smith.langchain.com
    description: GCP APAC
  - url: https://aws.api.smith.langchain.com
    description: AWS US
security: []
tags:
  - description: Register your own MCP servers (public, OAuth or API key) or use built-ins.
    name: Adding tools
  - description: >-
      Store credentials for yourself, an agent, a profile or the whole
      workspace.
    name: Connecting tools
  - description: Serve tools through tool kits, the me kit or a single server.
    name: Exposing tools
  - description: >-
      List and call tools, choose who you act as, and handle connect and
      approval prompts.
    name: Calling tools
paths:
  /v1/managed-tools/kits/{kit_id}:
    patch:
      tags:
        - Exposing tools
      summary: Update a tool kit
      description: >-
        Updates the fields you send and returns the tool kit. Requires
        mcp-servers:invoke, plus mcp-servers:update for a workspace kit, or
        mcp-servers:create-personal or mcp-servers:create for a personal kit.
        Call as yourself. Sending tools replaces the selection (an empty array
        or null removes all) and stores tool definitions as you list them; a
        listing failure doesn't fail the write. A kit keeps its scope: only a
        personal kit can link personal servers.
      operationId: updateManagedToolsKit
      parameters:
        - description: Tool kit ID
          name: kit_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateToolKitRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolKit'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolKit'
        '400':
          description: Invalid request or tool link.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '401':
          description: Missing or invalid authentication.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '403':
          description: >-
            Tool Gateway isn't enabled for your organization, or you lack the
            required permission.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '404':
          description: Tool kit not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '409':
          description: The name is taken.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '413':
          description: Request body is too large.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '503':
          description: Built-ins are temporarily unavailable.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
      security:
        - API Key: []
          Tenant ID: []
        - Bearer Auth: []
          Tenant ID: []
components:
  schemas:
    UpdateToolKitRequest:
      description: Changes to a tool kit. Omitted fields are unchanged.
      type: object
      properties:
        connection_policy:
          description: >-
            ALLOW_PARTIAL, the only supported policy, lists the kit's tools,
            including

            those of servers the caller has not connected when their definitions
            are

            known; calling one asks the caller to connect it.
          enum:
            - ALLOW_PARTIAL
          allOf:
            - $ref: '#/components/schemas/ConnectionPolicy'
        description:
          description: New description, up to 4096 characters. Null clears it.
          anyOf:
            - type: string
              maxLength: 4096
            - type: 'null'
        name:
          description: New tool kit name, up to 256 characters.
          type: string
          maxLength: 256
          example: Support agent
        tools:
          description: >-
            Replacement tool selection. Null or an empty array removes all
            tools.
          type: array
          maxItems: 10000
          items:
            $ref: '#/components/schemas/ToolKitToolLink'
    ToolKit:
      description: >-
        A tool kit: selected tools from one or more servers, exposed through one
        MCP endpoint.
      type: object
      properties:
        connection_policy:
          description: >-
            ALLOW_PARTIAL lists the kit's tools, including those of servers the
            caller

            has not connected when their definitions are known; calling one asks
            the

            caller to connect it.
          enum:
            - ALLOW_PARTIAL
          allOf:
            - $ref: '#/components/schemas/ConnectionPolicy'
        created_at:
          description: When the tool kit was created.
          type: string
        created_by:
          description: LangSmith user who created the tool kit.
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
        description:
          description: What the tool kit is for.
          type: string
        id:
          description: Tool kit ID.
          type: string
          format: uuid
        mcp_path:
          description: Streamable HTTP endpoint for this tool kit.
          type: string
        name:
          description: Tool kit name.
          type: string
          example: Support agent
        scope:
          description: 'Who can see the tool kit: the whole workspace, or only its owner.'
          enum:
            - personal
            - workspace
          allOf:
            - $ref: '#/components/schemas/ToolKitScope'
        server_count:
          description: Number of MCP servers and built-ins the selected tools come from.
          type: integer
        tool_count:
          description: Number of selected tools.
          type: integer
        tools:
          description: Selected tools. Omitted from list responses.
          type: array
          items:
            $ref: '#/components/schemas/ToolKitTool'
        updated_at:
          description: When the tool kit last changed.
          type: string
        updated_by:
          description: LangSmith user who last changed the tool kit.
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
    ToolGatewayProblem:
      description: An RFC 7807 problem details error, with LangSmith extensions.
      type: object
      required:
        - status
        - title
        - type
      properties:
        code:
          description: |-
            LangSmith extension: stable machine-readable error code, such as
            missing_permission or monthly_tool_call_limit.
          type: string
        detail:
          description: Explanation of this occurrence of the problem.
          type: string
        instance:
          description: URI reference of the request that caused the problem.
          type: string
        permission:
          description: 'LangSmith extension: the permission the operation requires.'
          type: string
        remedy:
          description: 'LangSmith extension: what you can do to fix the error.'
          type: string
        status:
          description: HTTP status code of the response.
          type: integer
        title:
          description: Short summary of the problem type.
          type: string
        type:
          description: URI reference that identifies the problem type.
          type: string
    ConnectionPolicy:
      description: >-
        How a tool kit handles servers the caller has not connected.
        ALLOW_PARTIAL, the only policy: the tool kit lists all of its tools, and
        calling one that needs a credential asks the caller to connect it.
      type: string
      enum:
        - ALLOW_PARTIAL
    ToolKitToolLink:
      description: >-
        One tool to add to a tool kit, from a registered server or a built-in
        integration. Set exactly one of server_id and builtin_server_key.
      type: object
      required:
        - tool_name
      properties:
        builtin_server_key:
          description: LangSmith built-in integration to select from.
          type: string
          example: parallel
        exposed_name:
          description: Display title you give the tool. It does not change the tool's name.
          type: string
          maxLength: 128
          example: List Linear issues
        server_id:
          description: >-
            Registered server to select from: a workspace server, or, in a
            personal

            tool kit, one of the caller's personal servers.
          type: string
        tool_name:
          description: Original tool name on the source server.
          type: string
          maxLength: 128
          example: list_issues
    ToolKitScope:
      description: >-
        Who can see a tool kit. workspace: the whole workspace; links only
        workspace servers and built-ins. personal: only its owner; may also link
        the owner's personal servers.
      type: string
      enum:
        - workspace
        - personal
    ToolKitTool:
      description: One tool selected in a tool kit.
      type: object
      required:
        - mcp_name
      properties:
        builtin_server_key:
          description: Built-in the tool comes from.
          type: string
        exposed_name:
          description: Display title for the tool. It does not change mcp_name.
          type: string
        mcp_name:
          description: >-
            Name you send in tools/call: <server>_<tool>, or
            langsmith_<key>_<tool> for a built-in, fixed when the tool is added.
          type: string
          example: linear_list_issues
        server_id:
          description: MCP server the tool comes from.
          type: string
        tool_name:
          description: Original tool name on the source server.
          type: string
  securitySchemes:
    API Key:
      description: >-
        Personal or workspace LangSmith API key. Personal keys identify the
        user. Workspace keys are limited to server listing and MCP calls and
        must also supply the end user's OIDC token or X-LangSmith-Identity.
      type: apiKey
      name: X-Api-Key
      in: header
    Tenant ID:
      description: >-
        Workspace UUID. This header selects a workspace; it does not
        authenticate the caller.
      type: apiKey
      name: X-Tenant-Id
      in: header
    Bearer Auth:
      description: >-
        Send `Bearer {token}`. The token may be issued by LangSmith or by the
        workspace's linked identity provider. A linked-provider token can
        authenticate MCP calls by itself, or identify the end user when paired
        with a workspace API key.
      type: apiKey
      name: Authorization
      in: header

````
