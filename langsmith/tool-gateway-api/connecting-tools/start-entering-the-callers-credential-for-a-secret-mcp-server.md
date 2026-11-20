---
title: "Start entering the caller's credential for a secret MCP server"
description: "Returns a link where you enter the values a workspace or built-in secret MCP server needs, to connect without calling the server first. Requires mcp-servers:invoke for the server. Choose who you call..."
source: "https://docs.langchain.com/langsmith/tool-gateway-api/connecting-tools/start-entering-the-callers-credential-for-a-secret-mcp-server"
category: "docs"
tags: [docs, langsmith, tool-gateway-api, connecting-tools, start-entering-the-callers-credential-for-a-secret-mcp-server]
---

# Start entering the caller's credential for a secret MCP server

> Returns a link where you enter the values a workspace or built-in secret MCP server needs, to connect without calling the server first. Requires mcp-servers:invoke for the server. Choose who you call as the same way as for MCP calls. The link is single-use, expires in 10 minutes, and its token is returned only once; stored values stay in use until you submit. Other servers return 409. With credential_owner_type, you as an admin get a link to connect that agent; this requires workspaces:credentials:manage and projects:update on the agent's tracing project.

## OpenAPI

**/langsmith/tool-gateway-openapi.json post /v1/managed-tools/servers/{id}/credential-sessions**

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
  /v1/managed-tools/servers/{id}/credential-sessions:
    post:
      tags:
        - Connecting tools
      summary: Start entering the caller's credential for a secret MCP server
      description: >-
        Returns a link where you enter the values a workspace or built-in secret
        MCP server needs, to connect without calling the server first. Requires
        mcp-servers:invoke for the server. Choose who you call as the same way
        as for MCP calls. The link is single-use, expires in 10 minutes, and its
        token is returned only once; stored values stay in use until you submit.
        Other servers return 409. With credential_owner_type, you as an admin
        get a link to connect that agent; this requires
        workspaces:credentials:manage and projects:update on the agent's tracing
        project.
      operationId: createManagedToolsCredentialSession
      parameters:
        - description: Workspace server ID or built-in catalog key
          name: id
          in: path
          required: true
          schema:
            type: string
        - description: >-
            Advanced alternative to a user OIDC token with a workspace API key.
            Set to the user's Tool Gateway identity UUID or provider:subject.
            Selecting another user requires workspaces:credentials:use or
            agent-auth-credentials:use. Ignored for personal credentials.
          name: X-LangSmith-Identity
          in: header
          schema:
            type: string
        - description: >-
            Owner whose credential to connect instead of the caller's. Requires
            a user credential; tool calls cannot name an owner.
          name: credential_owner_type
          in: query
          schema:
            type: string
            enum:
              - agent_identity
            title: Credential Owner Type
        - description: >-
            Agent environment ID, from GET /api/v1/agents/{agent_id}. Sent with
            credential_owner_type.
          name: credential_owner_id
          in: query
          schema:
            format: uuid
            type: string
            title: Credential Owner Id
      responses:
        '201':
          description: Created
          headers:
            Location:
              description: Agent Auth secret input session status path
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CredentialSession'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/CredentialSession'
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
          description: MCP server or agent not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '409':
          description: The server doesn't use secret credentials.
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
    CredentialSession:
      description: >-
        A link where you enter an MCP server's credential, or a credential
        already stored.
      type: object
      required:
        - auth_id
        - display_name
        - kind
        - slug
        - status
      properties:
        auth_id:
          description: Authorization session ID.
          type: string
        display_name:
          description: User-facing integration name.
          type: string
        kind:
          description: 'Authorization flow on the page: oauth or secret.'
          enum:
            - oauth
            - secret
          allOf:
            - $ref: '#/components/schemas/ConnectionType'
        slug:
          description: Credential connection slug.
          type: string
        status:
          description: >-
            Status is pending until the owner completes the page at
            VerificationURL,

            or completed when the credential was stored while starting the
            session,

            as for an OAuth connection that uses client credentials.
          type: string
          enum:
            - pending
            - completed
        verification_url:
          description: VerificationURL is absent for a completed session.
          type: string
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
    ConnectionType:
      description: >-
        How Tool Gateway authenticates to the upstream server. none: a public
        server that needs no credential. oauth: each user's OAuth access token.
        secret: header values, such as an API key, that each user stores.
      type: string
      enum:
        - none
        - oauth
        - secret
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
