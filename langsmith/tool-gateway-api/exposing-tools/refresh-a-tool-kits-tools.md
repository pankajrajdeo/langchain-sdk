---
title: "Refresh a tool kit's tools"
description: "Refreshes a tool kit's MCP servers and waits for the cache to update. Requires mcp-servers:update and mcp-servers:invoke, and no ABAC deny policy on MCP servers or built-ins. Call as yourself. Also..."
source: "https://docs.langchain.com/langsmith/tool-gateway-api/exposing-tools/refresh-a-tool-kits-tools"
category: "docs"
tags: [docs, langsmith, tool-gateway-api, exposing-tools, refresh-a-tool-kits-tools]
---

# Refresh a tool kit's tools

> Refreshes a tool kit's MCP servers and waits for the cache to update. Requires mcp-servers:update and mcp-servers:invoke, and no ABAC deny policy on MCP servers or built-ins. Call as yourself. Also stores the servers' tool definitions as you list them (not built-ins), so users who aren't connected still see the tools. Returns 200 when every server refreshes or needs a credential; missing_credentials lists the ones you must connect. Other failures return an error but keep other servers' writes. Times out after 90 seconds.

## OpenAPI

**/langsmith/tool-gateway-openapi.json post /v1/managed-tools/kits/{kit_id}/tool-refresh**

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
  /v1/managed-tools/kits/{kit_id}/tool-refresh:
    post:
      tags:
        - Exposing tools
      summary: Refresh a tool kit's tools
      description: >-
        Refreshes a tool kit's MCP servers and waits for the cache to update.
        Requires mcp-servers:update and mcp-servers:invoke, and no ABAC deny
        policy on MCP servers or built-ins. Call as yourself. Also stores the
        servers' tool definitions as you list them (not built-ins), so users who
        aren't connected still see the tools. Returns 200 when every server
        refreshes or needs a credential; missing_credentials lists the ones you
        must connect. Other failures return an error but keep other servers'
        writes. Times out after 90 seconds.
      operationId: refreshManagedToolsKitTools
      parameters:
        - description: Tool kit ID
          name: kit_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RefreshToolKitToolsResponse'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/RefreshToolKitToolsResponse'
        '400':
          description: Invalid request.
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
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '502':
          description: The upstream server failed.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '503':
          description: The tool cache is temporarily unavailable.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '504':
          description: The refresh timed out.
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
    RefreshToolKitToolsResponse:
      description: The result of refreshing a tool kit's tools.
      type: object
      properties:
        missing_credentials:
          description: >-
            Credentials you must connect before the remaining MCP servers can
            refresh.
          type: array
          items:
            $ref: '#/components/schemas/MissingCredential'
        refreshed_server_count:
          description: Number of linked MCP servers whose tools were refreshed.
          type: integer
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
    MissingCredential:
      description: A credential you must connect before the request can continue.
      type: object
      required:
        - display_name
        - kind
        - slug
      properties:
        auth_id:
          description: Authorization session ID.
          type: string
          example: 01960000-0000-7000-8000-000000000001
        display_name:
          description: User-facing integration name.
          type: string
          example: GitHub
        kind:
          description: >-
            Authorization flow you must complete: oauth to authorize an account,
            or secret to enter header values such as an API key.
          type: string
          enum:
            - oauth
            - secret
          example: oauth
        slug:
          description: Credential connection slug.
          type: string
          example: github
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
