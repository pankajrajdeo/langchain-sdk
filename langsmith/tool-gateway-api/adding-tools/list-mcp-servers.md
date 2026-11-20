---
title: "List MCP servers"
description: "Lists the workspace's MCP servers, your personal servers, and the built-ins available to the workspace, with your connection status. Requires mcp-servers:read. credential_source says whose credential..."
source: "https://docs.langchain.com/langsmith/tool-gateway-api/adding-tools/list-mcp-servers"
category: "docs"
tags: [docs, langsmith, tool-gateway-api, adding-tools, list-mcp-servers]
---

# List MCP servers

> Lists the workspace's MCP servers, your personal servers, and the built-ins available to the workspace, with your connection status. Requires mcp-servers:read. credential_source says whose credential calls use; a workspace credential shows as connected for everyone. With credential_owner_type, shows status for that owner: an agent requires workspaces:credentials:read-metadata and projects:read on the agent's tracing project; the workspace (credential_owner_id = workspace ID) requires workspaces:credentials:read-metadata.

## OpenAPI

**/langsmith/tool-gateway-openapi.json get /v1/managed-tools/servers**

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
    get:
      tags:
        - Adding tools
      summary: List MCP servers
      description: >-
        Lists the workspace's MCP servers, your personal servers, and the
        built-ins available to the workspace, with your connection status.
        Requires mcp-servers:read. credential_source says whose credential calls
        use; a workspace credential shows as connected for everyone. With
        credential_owner_type, shows status for that owner: an agent requires
        workspaces:credentials:read-metadata and projects:read on the agent's
        tracing project; the workspace (credential_owner_id = workspace ID)
        requires workspaces:credentials:read-metadata.
      operationId: listManagedToolsServers
      parameters:
        - description: Items per page
          name: page_size
          in: query
          schema:
            default: 20
            maximum: 100
            minimum: 1
            type: integer
            title: Page Size
        - description: Opaque pagination cursor
          name: cursor
          in: query
          schema:
            type: string
            title: Cursor
        - description: >-
            any lists only the personal servers of every workspace member, with
            owned_by set and without upstream URLs, connection fields, or
            credential status. Requires workspaces:integrations:read or
            workspaces:manage.
          name: owned_by
          in: query
          schema:
            type: string
            enum:
              - any
            title: Owned By
        - description: >-
            Advanced alternative to a user OIDC token with a workspace API key.
            Set to the user's Tool Gateway identity UUID or provider:subject.
            Ignored for personal credentials.
          name: X-LangSmith-Identity
          in: header
          schema:
            type: string
        - description: >-
            Owner whose credential to show connection status for instead of the
            caller's. Requires a user credential; tool calls cannot name an
            owner.
          name: credential_owner_type
          in: query
          schema:
            type: string
            enum:
              - agent_identity
              - workspace
            title: Credential Owner Type
        - description: >-
            Agent environment ID, from GET /api/v1/agents/{agent_id}, or the
            workspace ID for workspace. Sent with credential_owner_type.
          name: credential_owner_id
          in: query
          schema:
            format: uuid
            type: string
            title: Credential Owner Id
        - description: >-
            Profile ID whose connection status to show. Accepts
            workspaces:credentials:read-metadata, workspaces:credentials:use,
            agent-auth-credentials:use, or legacy workspaces:manage. This reads
            metadata only and does not grant runtime credential use. Cannot be
            combined with X-LangSmith-Identity or a user OIDC token.
          name: X-LangSmith-Profile
          in: header
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListServersResponse'
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ListServersResponse'
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
          description: Agent not found.
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
      security:
        - API Key: []
          Tenant ID: []
        - API Key: []
          Bearer Auth: []
          Tenant ID: []
        - Bearer Auth: []
          Tenant ID: []
components:
  schemas:
    ListServersResponse:
      description: A page of the MCP servers and built-ins you can use.
      type: object
      properties:
        items:
          description: MCP servers and built-ins on this page.
          type: array
          items:
            $ref: '#/components/schemas/Server'
        next_cursor:
          description: Cursor for the next page. Null on the last page.
          anyOf:
            - type: string
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
    ServerScope:
      description: >-
        Who can see a registered server. workspace: the whole workspace.
        personal: only the user who registered it.
      type: string
      enum:
        - workspace
        - personal
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
