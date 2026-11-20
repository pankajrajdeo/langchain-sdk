---
title: "Send an MCP message to a server"
description: "Proxies MCP Streamable HTTP requests to one MCP server or built-in. Requires mcp-servers:invoke. Prefer a tool kit for agents and MCP clients. If you aren't connected, you get 428 or an MCP URL..."
source: "https://docs.langchain.com/langsmith/tool-gateway-api/calling-tools/send-an-mcp-message-to-a-server"
category: "docs"
tags: [docs, langsmith, tool-gateway-api, calling-tools, send-an-mcp-message-to-a-server]
---

# Send an MCP message to a server

> Proxies MCP Streamable HTTP requests to one MCP server or built-in. Requires mcp-servers:invoke. Prefer a tool kit for agents and MCP clients. If you aren't connected, you get 428 or an MCP URL elicitation; the API overview covers both.

## OpenAPI

**/langsmith/tool-gateway-openapi.json post /v1/managed-tools/servers/{id}/mcp**

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
  /v1/managed-tools/servers/{id}/mcp:
    post:
      tags:
        - Calling tools
      summary: Send an MCP message to a server
      description: >-
        Proxies MCP Streamable HTTP requests to one MCP server or built-in.
        Requires mcp-servers:invoke. Prefer a tool kit for agents and MCP
        clients. If you aren't connected, you get 428 or an MCP URL elicitation;
        the API overview covers both.
      operationId: postManagedServerMCP
      parameters:
        - description: Workspace server ID or built-in server key
          name: id
          in: path
          required: true
          schema:
            type: string
        - description: >-
            Advanced alternative to a user OIDC token with a workspace API key.
            Set to the user's Tool Gateway identity UUID or provider:subject.
            Using that user's stored credentials requires
            workspaces:credentials:use or agent-auth-credentials:use. Ignored
            for personal credentials.
          name: X-LangSmith-Identity
          in: header
          schema:
            type: string
        - description: >-
            Profile ID whose admin-connected credentials to use instead of a
            user's. Requires workspaces:credentials:use or
            agent-auth-credentials:use and cannot be combined with
            X-LangSmith-Identity or a user OIDC token.
          name: X-LangSmith-Profile
          in: header
          schema:
            type: string
            format: uuid
        - description: >-
            Session ID returned by the MCP server, when required for an
            established session
          name: MCP-Session-Id
          in: header
          schema:
            type: string
        - description: Negotiated MCP protocol version
          name: MCP-Protocol-Version
          in: header
          schema:
            type: string
        - description: Last received SSE event ID when resuming a stream
          name: Last-Event-ID
          in: header
          schema:
            type: string
      requestBody:
        required: false
        content:
          application/json:
            schema:
              example:
                id: 2
                jsonrpc: '2.0'
                method: tools/call
                params:
                  arguments: {}
                  name: list_issues
      responses:
        '200':
          description: Upstream MCP JSON message or SSE stream.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema: {}
            application/problem+json:
              schema: {}
            text/event-stream:
              schema:
                type: string
        '202':
          description: Upstream accepted the message; the body may be empty.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
        '204':
          description: Upstream returned no body.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
        '400':
          description: Invalid request.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '401':
          description: Missing or invalid authentication.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '403':
          description: >-
            Blocked by a policy, needs approval your client can't show, or
            access denied.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '404':
          description: MCP server or profile not found.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '409':
          description: >-
            An agent or profile isn't connected; an admin must connect it. Also
            returned when the server's OAuth or credential setup isn't
            supported.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '413':
          description: Request body is too large.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '428':
          description: You aren't connected to the server; open the link and retry.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CredentialRequired'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/CredentialRequired'
        '429':
          description: Rate limited; wait for Retry-After seconds.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
            Retry-After:
              description: Seconds to wait before retrying
              schema:
                type: integer
            X-RateLimit-Limit:
              description: Burst size or monthly call limit that was reached
              schema:
                type: integer
            X-RateLimit-Remaining:
              description: Always 0 on a rejected request
              schema:
                type: integer
            X-RateLimit-Reset:
              description: Seconds until a request is allowed again
              schema:
                type: integer
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '500':
          description: Internal server error.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '502':
          description: The upstream server failed.
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        default:
          description: Other upstream status codes and response bodies are passed through
          headers:
            MCP-Protocol-Version:
              description: MCP protocol version, when supplied by the upstream server
              schema:
                type: string
            MCP-Session-Id:
              description: MCP session ID, when supplied by the upstream server
              schema:
                type: string
      security:
        - API Key: []
          Tenant ID: []
        - API Key: []
          Bearer Auth: []
          Tenant ID: []
        - Bearer Auth: []
        - Bearer Auth: []
          Tenant ID: []
components:
  schemas:
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
    CredentialRequired:
      description: >-
        Error returned when you must connect a credential for the MCP server
        first.
      type: object
      required:
        - display_name
        - kind
        - slug
        - status
        - title
        - type
      properties:
        auth_id:
          description: Authorization session ID.
          type: string
          example: 01960000-0000-7000-8000-000000000001
        code:
          description: |-
            LangSmith extension: stable machine-readable error code, such as
            missing_permission or monthly_tool_call_limit.
          type: string
        detail:
          description: Explanation of this occurrence of the problem.
          type: string
        display_name:
          description: User-facing integration name.
          type: string
          example: GitHub
        instance:
          description: URI reference of the request that caused the problem.
          type: string
        kind:
          description: >-
            Authorization flow you must complete: oauth to authorize an account,
            or secret to enter header values such as an API key.
          type: string
          enum:
            - oauth
            - secret
          example: oauth
        permission:
          description: 'LangSmith extension: the permission the operation requires.'
          type: string
        remedy:
          description: 'LangSmith extension: what you can do to fix the error.'
          type: string
        slug:
          description: Credential connection slug.
          type: string
          example: github
        status:
          description: HTTP status code of the response.
          type: integer
        title:
          description: Short summary of the problem type.
          type: string
        tools:
          description: >-
            Only in tools/list result._meta of an ALLOW_PARTIAL tool kit: the
            linked

            tools this credential unlocks, as MCP tool definitions. A linked
            server's

            come from the listing of the user who last saved or refreshed the
            tool

            kit, with their connection, and every user who can invoke the tool
            kit

            sees them. Calling one returns 428 until the credential is
            connected.
          type: array
          items:
            $ref: '#/components/schemas/MissingCredentialTool'
        type:
          description: URI reference that identifies the problem type.
          type: string
        verification_url:
          description: Browser URL where the user completes authorization.
          type: string
          example: https://smith.langchain.com/authorize/example
    MissingCredentialTool:
      description: An MCP tool definition, named as the tool kit exposes it.
      type: object
      required:
        - inputSchema
        - name
      properties:
        _meta:
          description: MCP metadata for the tool.
          type: object
          additionalProperties: {}
        annotations:
          description: MCP tool annotations, such as readOnlyHint.
          type: object
          additionalProperties: {}
        description:
          description: What the tool does.
          type: string
        icons:
          description: MCP icons for the tool.
          type: array
          items: {}
        inputSchema:
          description: JSON Schema of the tool's arguments.
          type: object
          additionalProperties: {}
        name:
          description: Tool name you send in tools/call.
          type: string
          example: github_create_issue
        outputSchema:
          description: JSON Schema of the tool's structured result.
          type: object
          additionalProperties: {}
        title:
          description: Human-readable tool title.
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
