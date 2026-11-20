---
title: "List organization roles"
description: "/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/roles"
source: "https://docs.langchain.com/langsmith/smith-api/orgs/list-organization-roles"
category: "docs"
tags: [docs, langsmith, smith-api, orgs, list-organization-roles]
---

# List organization roles

## OpenAPI

**/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/roles**

````yaml
openapi: 3.1.0
info:
  title: LangSmith
  description: >+
    The LangSmith API is used to programmatically create and manage LangSmith
    resources.

    ## Host

    https://api.smith.langchain.com

    ## Authentication

    To authenticate with the LangSmith API, set the `X-Api-Key` header

    to a valid [LangSmith API
    key](https://docs.langchain.com/langsmith/create-account-api-key#create-an-api-key).

  version: 0.1.0
servers:
  - url: /
security: []
tags:
  - name: run
    x-group: Tracing
  - name: runs
    x-group: Tracing
  - name: sessions
    x-group: Tracing
  - name: tracer-sessions
    x-group: Tracing
  - name: threads
    x-group: Threads
  - name: datasets
    x-group: Datasets
  - name: examples
    x-group: Datasets
  - name: evaluators
    x-group: Evaluation
  - name: experiment-view-overrides
    x-group: Evaluation
  - name: experiments
    x-group: Evaluation
  - name: annotation-queues
    x-group: Feedback & Annotation
  - name: annotation_queues
    x-group: Feedback & Annotation
  - name: feedback
    x-group: Feedback & Annotation
  - name: feedback-configs
    x-group: Feedback & Annotation
  - name: alert_rules
    x-group: Monitoring
  - name: bulk-exports
    x-group: Monitoring
  - name: charts
    x-group: Monitoring
  - name: commits
    x-group: Prompts & Playground
  - name: directories
    x-group: Prompts & Playground
  - name: hub_environments
    x-group: Prompts & Playground
  - name: playground-settings
    x-group: Prompts & Playground
  - name: prompt-webhooks
    x-group: Prompts & Playground
  - name: prompts
    x-group: Prompts & Playground
  - name: tag-transitions
    x-group: Prompts & Playground
  - name: comments
    x-group: Prompt Hub
  - name: likes
    x-group: Prompt Hub
  - name: optimization-jobs
    x-group: Prompt Hub
  - name: ownerships
    x-group: Prompt Hub
  - name: repos
    x-group: Prompt Hub
  - name: settings
    x-group: Prompt Hub
  - name: tags
    x-group: Prompt Hub
  - name: integrations
    x-group: Integrations & Tools
  - name: mcp
    x-group: Integrations & Tools
  - name: mcp_vendors
    x-group: Integrations & Tools
  - name: oauth
    x-group: Integrations & Tools
  - name: tools
    x-group: Integrations & Tools
  - name: gateway-policies
    x-group: LLM Gateway
  - name: sandboxes
    x-group: Sandboxes
  - name: issues
    x-group: Issues
  - name: issues-agent
    x-group: Issues
  - name: Organizations
    x-group: Administration
  - name: SCIM Tokens
    x-group: Administration
  - name: TTL Settings
    x-group: Administration
  - name: access_policies
    x-group: Administration
  - name: api-key
    x-group: Administration
  - name: audit-logs
    x-group: Administration
  - name: auth
    x-group: Administration
  - name: aws_marketplace
    x-group: Administration
  - name: data_planes
    x-group: Administration
  - name: me
    x-group: Administration
  - name: orgs
    x-group: Administration
  - name: service-accounts
    x-group: Administration
  - name: tenant
    x-group: Administration
  - name: ttl-settings
    x-group: Administration
  - name: usage-limits
    x-group: Administration
  - name: workspaces
    x-group: Administration
  - name: ace
    x-group: System
  - name: backfills
    x-group: System
  - name: features
    x-group: System
  - name: info
    x-group: System
  - name: model-price-map
    x-group: System
  - name: public
    x-group: System
  - name: agents
    x-hidden: true
  - name: fleet orgs
  - name: fleet secrets
  - name: fleet tenants
  - name: fleet threads
    x-hidden: true
  - name: fleet users
  - name: productfeedback
    x-hidden: true
  - name: rules
  - name: runsanalytics
  - name: sql
  - name: usage
  - name: user-groups
  - name: users
paths:
  /api/v1/orgs/current/roles:
    get:
      tags:
        - orgs
      summary: List organization roles
      operationId: list_organization_roles_api_v1_orgs_current_roles_get
      parameters:
        - name: sort_by
          in: query
          required: false
          schema:
            anyOf:
              - type: array
                items:
                  enum:
                    - display_name
                    - created_at
                  type: string
              - type: 'null'
            description: >-
              Fields to sort by, applied in the order supplied within existing
              scope and built-in role priorities. Repeat this parameter for
              multiple fields. Omit to preserve the default ordering.
            title: Sort By
          description: >-
            Fields to sort by, applied in the order supplied within existing
            scope and built-in role priorities. Repeat this parameter for
            multiple fields. Omit to preserve the default ordering.
        - name: sort_order
          in: query
          required: false
          schema:
            anyOf:
              - type: array
                items:
                  enum:
                    - asc
                    - desc
                  type: string
              - type: 'null'
            description: >-
              Sort directions corresponding positionally to sort_by fields.
              Supply one direction for all fields, or repeat this parameter once
              per field. Omit to sort all requested fields ascending. Ignored
              when sort_by is omitted. Scope and built-in role priorities are
              unchanged.
            title: Sort Order
          description: >-
            Sort directions corresponding positionally to sort_by fields. Supply
            one direction for all fields, or repeat this parameter once per
            field. Omit to sort all requested fields ascending. Ignored when
            sort_by is omitted. Scope and built-in role priorities are
            unchanged.
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Role'
                title: Response List Organization Roles Api V1 Orgs Current Roles Get
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - API Key: []
        - Organization ID: []
        - Bearer Auth: []
components:
  schemas:
    Role:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        name:
          type: string
          title: Name
        display_name:
          type: string
          title: Display Name
        description:
          type: string
          title: Description
        organization_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Organization Id
        permissions:
          items:
            type: string
          type: array
          title: Permissions
        access_scope:
          anyOf:
            - $ref: '#/components/schemas/AccessScope'
            - type: 'null'
        is_restricted:
          type: boolean
          title: Is Restricted
          default: false
      type: object
      required:
        - id
        - name
        - display_name
        - description
        - permissions
      title: Role
    HTTPValidationError:
      properties:
        detail:
          items:
            type: string
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AccessScope:
      type: string
      enum:
        - organization
        - workspace
      title: AccessScope
  securitySchemes:
    API Key:
      type: apiKey
      in: header
      name: X-API-Key
    Organization ID:
      type: apiKey
      in: header
      name: X-Organization-Id
    Bearer Auth:
      type: http
      description: >-
        Bearer tokens are used to authenticate from the UI. Must also specify
        x-tenant-id or x-organization-id (for org scoped apis).
      scheme: bearer

````
