---
title: "Add an MCP server"
description: "Registers an HTTPS MCP server that is public or uses OAuth or per-user header credentials. Requires mcp-servers:create for a workspace server (the default, visible to the workspace), or..."
source: "https://docs.langchain.com/langsmith/tool-gateway-api/adding-tools/add-an-mcp-server"
category: "docs"
tags: [docs, langsmith, tool-gateway-api, adding-tools, add-an-mcp-server]
---

# Add an MCP server

> Registers an HTTPS MCP server that is public or uses OAuth or per-user header credentials. Requires mcp-servers:create for a workspace server (the default, visible to the workspace), or mcp-servers:create-personal or mcp-servers:create for a personal server (visible only to you). Call as yourself. Selecting a shared OAuth connection also requires workspaces:integrations:manage. A workspace secret server can include a workspace credential, which every caller then uses and which blocks other credentials; this requires workspaces:credentials:manage. Credential values are never returned.

## OpenAPI

**/langsmith/tool-gateway-openapi.json post /v1/managed-tools/servers**

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
  /v1/managed-tools/servers:
    post:
      tags:
        - Adding tools
      summary: Add an MCP server
      description: >-
        Registers an HTTPS MCP server that is public or uses OAuth or per-user
        header credentials. Requires mcp-servers:create for a workspace server
        (the default, visible to the workspace), or mcp-servers:create-personal
        or mcp-servers:create for a personal server (visible only to you). Call
        as yourself. Selecting a shared OAuth connection also requires
        workspaces:integrations:manage. A workspace secret server can include a
        workspace credential, which every caller then uses and which blocks
        other credentials; this requires workspaces:credentials:manage.
        Credential values are never returned.
      operationId: createManagedToolsServer
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateServerRequest'
      responses:
        '201':
          description: Created
          headers:
            Location:
              description: Path of the created server
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Server'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/Server'
        '400':
          description: >-
            Invalid request, OAuth discovery rejected the server, a public
            server needs authentication, or the credential doesn't fit the
            server.
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
          description: OAuth connection not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ToolGatewayProblem'
        '409':
          description: >-
            The name or URL is taken, or another server manages the OAuth
            connection.
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
          description: Personal servers are temporarily unavailable.
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
      x-codeSamples:
        - label: Register a public server
          lang: Shell
          source: >-
            curl --request POST
            'https://api.smith.langchain.com/v1/managed-tools/servers' \
              --header 'X-Api-Key: <personal-api-key>' \
              --header 'X-Tenant-Id: <workspace-id>' \
              --header 'Content-Type: application/json' \
              --data '{"name":"Documentation","upstream_url":"https://mcp.example.com/mcp","connection":{"type":"none"}}'
        - label: Register a secret server with a workspace credential
          lang: Shell
          source: >-
            curl --request POST
            'https://api.smith.langchain.com/v1/managed-tools/servers' \
              --header 'X-Api-Key: <personal-api-key>' \
              --header 'X-Tenant-Id: <workspace-id>' \
              --header 'Content-Type: application/json' \
              --data '{"name":"Search","upstream_url":"https://mcp.example.com/mcp","connection":{"type":"secret","fields":[{"name":"X-Api-Key","injection":{"type":"header","name":"X-Api-Key"}}]},"credential":{"owner_type":"workspace","fields":{"X-Api-Key":"<upstream-api-key>"}}}'
components:
  schemas:
    CreateServerRequest:
      description: An upstream MCP server to register.
      type: object
      required:
        - name
        - upstream_url
      properties:
        connection:
          description: >-
            Upstream authentication mode: public, OAuth, or user-provided
            headers.
          allOf:
            - $ref: '#/components/schemas/ServerConnection'
        credential:
          description: |-
            Header values to store as the server is registered. Requires
            connection.type secret. Omit it to register the server without a
            credential.
          allOf:
            - $ref: '#/components/schemas/CreateServerCredential'
        name:
          description: Name you give the MCP server in Tool Gateway.
          type: string
          example: Linear
        scope:
          description: |-
            Who can see the server. Defaults to workspace, which requires
            mcp-servers:create; personal requires mcp-servers:create-personal or
            mcp-servers:create.
          enum:
            - personal
            - workspace
          allOf:
            - $ref: '#/components/schemas/ServerScope'
        upstream_url:
          description: HTTPS Streamable HTTP endpoint of the MCP server.
          type: string
          example: https://mcp.linear.app/mcp
    Server:
      description: An MCP server or built-in integration available to the workspace.
      type: object
      properties:
        connected:
          description: >-
            Whether the current user's upstream credential is currently usable.
            Public

            servers are always connected.
          type: boolean
        connection:
          description: Authentication the upstream server requires from each user.
          allOf:
            - $ref: '#/components/schemas/ServerConnection'
        credential_source:
          description: >-
            Whose credential calls to the server use: workspace when a workspace

            admin stored one for every caller, caller when the current user's
            own

            credential is used, and none otherwise. Omitted where credential
            state is

            not reported.
          enum:
            - workspace
            - caller
            - none
          allOf:
            - $ref: '#/components/schemas/CredentialSource'
        credential_status:
          description: |-
            The current user's credential state. connected matches Connected;
            unavailable means the state could not be checked, not that the user
            must connect.
          allOf:
            - $ref: '#/components/schemas/CredentialStatus'
        enabled:
          description: >-
            Whether workspace members can use the server. A workspace admin can
            turn

            a server off for the whole workspace.
          type: boolean
        has_credential:
          description: |-
            Whether the current user has stored a credential. The credential may
            still require renewal or correction.
          type: boolean
        icon_dark_url:
          description: >-
            HTTPS URL of a drawing of the icon for dark backgrounds, set only
            when

            there is one: a built-in logo that does not read on a dark
            background,

            or an icon a registered server marks as designed for a dark theme.
          type: string
        icon_url:
          description: >-
            HTTPS URL of the server's icon, for an image element. For a built-in
            it

            is the LangSmith logo; for a registered server it is the icon the
            server

            advertises, on the server's own domain. Omitted when there is none,
            or

            the server has not been reached yet.
          type: string
        id:
          description: Registered server UUID, or the integration key for a built-in.
          type: string
        key:
          description: Stable built-in integration key. Empty for registered servers.
          type: string
        name:
          description: MCP server or built-in name.
          type: string
          example: Linear
        owned_by:
          description: >-
            The member who owns a personal server. Set only when a workspace
            admin

            lists every member's personal servers with owned_by=any.
          allOf:
            - $ref: '#/components/schemas/ServerOwner'
        owner:
          description: >-
            Whether the server is a LangSmith built-in or registered by the
            workspace.
          allOf:
            - $ref: '#/components/schemas/ServerOwnerType'
        scope:
          description: >-
            Who can see a registered server: the whole workspace, or only the
            user

            who registered it. Empty for built-ins.
          enum:
            - personal
            - workspace
          allOf:
            - $ref: '#/components/schemas/ServerScope'
        tools:
          description: Known tools for built-in integrations.
          type: array
          items:
            $ref: '#/components/schemas/BuiltinTool'
        upstream_url:
          description: Registered upstream MCP server URL.
          type: string
        url:
          description: Tool Gateway MCP endpoint that clients connect to.
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
    ServerConnection:
      description: >-
        How the upstream MCP server authenticates you. Credential values are
        never returned.
      type: object
      properties:
        agent_auth_connection_slug:
          description: Manually configured OAuth connection slug.
          type: string
        fields:
          description: Headers a user must supply for a secret connection.
          type: array
          items:
            $ref: '#/components/schemas/SecretField'
        oauth_setup:
          description: >-
            Settings you use to register your workspace's own OAuth app; set
            only for built-ins that need one.
          allOf:
            - $ref: '#/components/schemas/OAuthSetup'
        scopes:
          description: OAuth scopes requested from the upstream provider.
          type: array
          items:
            type: string
        type:
          description: 'Upstream authentication method: none, oauth, or secret.'
          allOf:
            - $ref: '#/components/schemas/ConnectionType'
          example: oauth
    CreateServerCredential:
      description: >-
        A credential to store when a secret server is registered. Its values are
        never returned.
      type: object
      required:
        - fields
        - owner_type
      properties:
        fields:
          description: >-
            Declared header names mapped to complete values, including prefixes
            such

            as "Bearer " when required.
          type: object
          additionalProperties:
            type: string
        owner_type:
          description: >-
            Whose credential to store. workspace stores the workspace
            credential,

            which every caller of the server then uses, including agents in the

            workspace, and while it is stored no other owner can add one. It

            requires a workspace server and workspaces:credentials:manage.
          type: string
          enum:
            - workspace
    ServerScope:
      description: >-
        Who can see a registered server. workspace: the whole workspace.
        personal: only the user who registered it.
      type: string
      enum:
        - workspace
        - personal
    CredentialSource:
      description: >-
        Whose credential calls to a server use. workspace: the credential a
        workspace admin stored for every caller. caller: the current user's own
        credential. none: no stored credential.
      type: string
      enum:
        - workspace
        - caller
        - none
    CredentialStatus:
      description: >-
        The current user's credential state for a server. Clients must tolerate
        values added later. connected: the credential is usable; public servers
        are always connected. needs_connect: the user has no credential.
        needs_reconnect: the stored credential must be authorized again.
        unavailable: the state could not be checked; it says nothing about the
        credential itself.
      type: string
      enum:
        - connected
        - needs_connect
        - needs_reconnect
        - unavailable
    ServerOwner:
      description: The member who owns a personal server.
      type: object
      properties:
        id:
          description: Agent Auth principal that owns the server.
          type: string
          format: uuid
        ls_user_id:
          description: LangSmith user bound to the principal, when there is one.
          type: string
          format: uuid
    ServerOwnerType:
      description: >-
        Who registered the server. langsmith: a LangSmith built-in integration.
        workspace: an MCP server the workspace registered.
      type: string
      enum:
        - langsmith
        - workspace
    BuiltinTool:
      description: A tool a built-in integration offers.
      type: object
      properties:
        display_name:
          description: User-facing tool name.
          type: string
        name:
          description: Tool name on the integration.
          type: string
        scopes:
          description: OAuth scopes the tool needs.
          type: array
          items:
            type: string
    SecretField:
      description: One header value you supply for a secret connection.
      type: object
      properties:
        injection:
          description: Header destination for this value.
          allOf:
            - $ref: '#/components/schemas/SecretInjection'
        name:
          description: Name clients use in the credential fields object.
          type: string
    OAuthSetup:
      description: >-
        Settings a workspace admin uses to register an OAuth app with the
        provider of a built-in integration.
      type: object
      properties:
        authorization_url:
          description: Provider's OAuth authorization endpoint.
          type: string
        callback_url:
          description: Redirect URL you enter in the provider's app settings.
          type: string
        oauth_provider_id:
          description: The workspace's registered app. Absent until an admin registers one.
          type: string
          format: uuid
        pkce:
          description: Whether the flow uses PKCE.
          type: boolean
        provider_slug:
          description: OAuth provider slug for the app.
          type: string
        revocation_url:
          description: Provider's OAuth token revocation endpoint, when it has one.
          type: string
        scopes:
          description: OAuth scopes the app requests.
          type: array
          items:
            type: string
        token_endpoint_auth_method:
          description: >-
            How the app authenticates to the token endpoint, such as
            client_secret_basic.
          type: string
        token_url:
          description: Provider's OAuth token endpoint.
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
    SecretInjection:
      description: The upstream request header that receives a secret value.
      type: object
      properties:
        name:
          description: Upstream HTTP header name.
          type: string
        prefix:
          description: Reserved; omit when registering a server.
          type: string
        type:
          description: Injection method. Currently always header.
          allOf:
            - $ref: '#/components/schemas/InjectionType'
    InjectionType:
      description: >-
        How a secret value is applied on an upstream request. header: sent as an
        HTTP request header.
      type: string
      enum:
        - header
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
