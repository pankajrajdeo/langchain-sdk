---
title: "Translate an ai search into query filters"
description: "Translates a natural-language search into the scope, filters, semantic criterion and time bounds for the runs, traces or threads query API, without running the search. No resources are created. Send..."
source: "https://docs.langchain.com/langsmith/smith-api/runs/translate-an-ai-search-into-query-filters"
category: "docs"
tags: [docs, langsmith, smith-api, runs, translate-an-ai-search-into-query-filters]
---

# Translate an ai search into query filters

> Translates a natural-language search into the scope, filters, semantic criterion and time bounds for the runs, traces or threads query API, without running the search. No resources are created. Send the returned fields to the query API named by scope, with the same projects.
When scope is omitted, it is inferred from the search and defaults to traces. A time period in the search sets min_start_time or max_start_time; bounds the search does not mention are omitted so you can keep your own time range.
Requires AI search to be enabled for the organization and read access to every project. Returns a single JSON response.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json post /api/v2/ai-search/parse**

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
  /api/v2/ai-search/parse:
    post:
      tags:
        - runs
      summary: Translate an ai search into query filters
      description: >-
        Translates a natural-language search into the scope, filters, semantic
        criterion and time bounds for the runs, traces or threads query API,
        without running the search. No resources are created. Send the returned
        fields to the query API named by scope, with the same projects.

        When scope is omitted, it is inferred from the search and defaults to
        traces. A time period in the search sets min_start_time or
        max_start_time; bounds the search does not mention are omitted so you
        can keep your own time range.

        Requires AI search to be enabled for the organization and read access to
        every project. Returns a single JSON response.
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/query.AISearchParseRequestBody'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/query.AISearchParseResponse'
        '400':
          description: Malformed JSON or invalid parameters
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '401':
          description: Missing or invalid authentication
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '403':
          description: Missing project access or AI search consent
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '404':
          description: Full AI search is disabled or a project does not exist
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '429':
          description: AI search request quota exceeded
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '500':
          description: Internal server error
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '501':
          description: AI search is unavailable for this deployment
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '502':
          description: Invalid AI search plan
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '503':
          description: AI search is temporarily unavailable
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '504':
          description: AI search planning deadline exceeded
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
      security:
        - API Key: []
          Tenant ID: []
        - Bearer Auth: []
          Tenant ID: []
components:
  schemas:
    query.AISearchParseRequestBody:
      type: object
      required:
        - ai_search
        - project_ids
      properties:
        ai_search:
          description: >-
            Natural-language description of the runs, traces or threads to find,
            at most 2000 UTF-8 bytes.
          type: string
          maxLength: 2000
          minLength: 1
          example: >-
            threads where the agent did not complete the task and spent more
            than $1
        allow_clarification:
          description: >-
            When true, an ambiguous search returns clarification options instead
            of a single plan. Defaults to false.
          type: boolean
        project_ids:
          description: >-
            Tracing project UUIDs used to interpret the search. Send the same
            projects to the query API.
          type: array
          minItems: 1
          items:
            type: string
            format: uuid
          example:
            - 018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327
        scope:
          description: >-
            Query API to plan for: runs, traces or threads. When omitted, it is
            inferred from the search and defaults to traces.
          type: string
          enum:
            - runs
            - traces
            - threads
    query.AISearchParseResponse:
      type: object
      properties:
        clarification:
          description: >-
            Interpretations to choose from. Returned only when
            allow_clarification is true and the search is ambiguous; no other
            fields are set.
          allOf:
            - $ref: '#/components/schemas/query.AISearchClarification'
        filter:
          description: >-
            Filter expression for the query API's filter parameter. Omitted when
            there is none.
          type: string
        max_start_time:
          description: >-
            Upper bound on start time (RFC 3339, UTC) for the query API's
            max_start_time parameter. Omitted when the search names no end; keep
            your own time range.
          type: string
          format: date-time
        min_start_time:
          description: >-
            Lower bound on start time (RFC 3339, UTC) for the query API's
            min_start_time parameter. Omitted when the search names no start;
            keep your own time range.
          type: string
          format: date-time
        scope:
          description: 'Query API to send the plan to: runs, traces or threads.'
          type: string
          enum:
            - runs
            - traces
            - threads
        sem_filter:
          description: >-
            Plain-language criterion for the query API's sem_filter parameter,
            matched against conversation messages. Null when the search has no
            conversational criterion.
          anyOf:
            - type: string
            - type: 'null'
        thread_filter:
          description: >-
            Filter expression for the threads query API's thread_filter
            parameter. Omitted when there is none.
          type: string
        trace_filter:
          description: >-
            Filter expression for the query API's trace_filter parameter.
            Omitted when there is none.
          type: string
        tree_filter:
          description: >-
            Filter expression for the query API's tree_filter parameter. Omitted
            when there is none.
          type: string
    shared.ProblemDetails:
      description: RFC 7807 problem details returned on V2 API errors.
      type: object
      properties:
        detail:
          type: string
        details:
          description: >-
            Details is a LangSmith extension carrying structured fields for
            ErrorClass.
          allOf:
            - $ref: '#/components/schemas/shared.ParseErrorDetails'
        error_class:
          description: |-
            ErrorClass is a LangSmith extension sub-categorizing a status code.
            Additional values require expanding this enum and adding a oneOf
            discriminator on Details to keep the class↔details contract typed.
          type: string
          enum:
            - PARSE_FAILURE
        instance:
          type: string
        remedy:
          description: Remedy is a LangSmith extension for user-recoverable errors.
          type: string
        status:
          type: integer
        title:
          type: string
        type:
          type: string
    query.AISearchClarification:
      type: object
      properties:
        options:
          description: Two or three interpretations of the search.
          type: array
          items:
            $ref: '#/components/schemas/query.AISearchClarificationOption'
    shared.ParseErrorDetails:
      description: Structured fields describing an adapter parse failure.
      type: object
      required:
        - adapter
        - item_type
      properties:
        adapter:
          type: string
        item_type:
          type: string
        run_id:
          type: string
    query.AISearchClarificationOption:
      type: object
      properties:
        filter:
          description: >-
            Filter expression for the query API's filter parameter. Omitted when
            there is none.
          type: string
        label:
          description: Short description of this interpretation to show the user.
          type: string
        max_start_time:
          description: >-
            Upper bound on start time (RFC 3339, UTC) for the query API's
            max_start_time parameter. Omitted when the search names no end; keep
            your own time range.
          type: string
          format: date-time
        min_start_time:
          description: >-
            Lower bound on start time (RFC 3339, UTC) for the query API's
            min_start_time parameter. Omitted when the search names no start;
            keep your own time range.
          type: string
          format: date-time
        scope:
          description: Query API this interpretation is planned for.
          type: string
          enum:
            - runs
            - traces
            - threads
        sem_filter:
          description: >-
            Plain-language criterion for the query API's sem_filter parameter,
            matched against conversation messages. Null when the search has no
            conversational criterion.
          anyOf:
            - type: string
            - type: 'null'
        thread_filter:
          description: >-
            Filter expression for the threads query API's thread_filter
            parameter. Omitted when there is none.
          type: string
        trace_filter:
          description: >-
            Filter expression for the query API's trace_filter parameter.
            Omitted when there is none.
          type: string
        tree_filter:
          description: >-
            Filter expression for the query API's tree_filter parameter. Omitted
            when there is none.
          type: string
  securitySchemes:
    API Key:
      type: apiKey
      in: header
      name: X-API-Key
    Tenant ID:
      type: apiKey
      in: header
      name: X-Tenant-Id
    Bearer Auth:
      type: http
      description: >-
        Bearer tokens are used to authenticate from the UI. Must also specify
        x-tenant-id or x-organization-id (for org scoped apis).
      scheme: bearer

````
