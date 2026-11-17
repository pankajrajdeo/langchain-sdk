---
title: "List run rules"
description: "List workspace rules in descending updated_at and id order. Filters combine with AND. Pass next_cursor unchanged with the same filters to continue; concurrent changes can affect later pages."
source: "https://docs.langchain.com/langsmith/smith-api/rules/list-run-rules"
category: "docs"
tags: [docs, langsmith, smith-api, rules, list-run-rules]
---

# List run rules

> List workspace rules in descending updated_at and id order. Filters combine with AND. Pass next_cursor unchanged with the same filters to continue; concurrent changes can affect later pages.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json get /api/v2/runs/rules**

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
  - name: sql
  - name: teams
  - name: usage
  - name: user-groups
paths:
  /api/v2/runs/rules:
    get:
      tags:
        - rules
      summary: List run rules
      description: >-
        List workspace rules in descending updated_at and id order. Filters
        combine with AND. Pass next_cursor unchanged with the same filters to
        continue; concurrent changes can affect later pages.
      operationId: listRunRules
      parameters:
        - description: Page size
          name: page_size
          in: query
          schema:
            type: integer
            maximum: 100
            minimum: 1
            title: Page Size
            default: 20
        - description: Cursor from the previous page
          name: cursor
          in: query
          schema:
            type: string
            title: Cursor
        - description: Source project UUID
          name: project_id
          in: query
          schema:
            type: string
            format: uuid
            title: Project Id
        - description: Source dataset UUID
          name: dataset_id
          in: query
          schema:
            type: string
            format: uuid
            title: Dataset Id
        - description: Rule source type
          name: type
          in: query
          schema:
            enum:
              - PROJECT
              - DATASET
            type: string
            title: Type
        - description: Case-insensitive display-name pattern
          name: name_contains
          in: query
          schema:
            type: string
            title: Name Contains
        - description: Rule UUIDs
          name: id
          in: query
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
              format: uuid
            title: Id
        - description: Linked evaluator UUID
          name: evaluator_id
          in: query
          schema:
            type: string
            format: uuid
            title: Evaluator Id
        - description: Source must have every tag UUID
          name: tag_value_id
          in: query
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
              format: uuid
            title: Tag Value Id
        - description: Include backfill progress
          name: include_backfill_progress
          in: query
          schema:
            type: boolean
            default: false
            title: Include Backfill Progress
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rules.ListResponse'
        '400':
          description: Bad Request
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/rules.ProblemDetails'
        '401':
          description: Unauthorized
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/rules.ProblemDetails'
        '403':
          description: Forbidden
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/rules.ProblemDetails'
        '429':
          description: Too Many Requests
          headers:
            Retry-After:
              description: Retry delay in seconds or an HTTP-date, when provided
              schema:
                type: string
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/rules.ProblemDetails'
        '500':
          description: Internal Server Error
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/rules.ProblemDetails'
        '502':
          description: Bad Gateway
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/rules.ProblemDetails'
        '503':
          description: Service Unavailable
          headers:
            Retry-After:
              description: Retry delay in seconds or an HTTP-date, when provided
              schema:
                type: string
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/rules.ProblemDetails'
        '504':
          description: Gateway Timeout
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/rules.ProblemDetails'
      security:
        - API Key: []
          Tenant ID: []
        - Bearer Auth: []
          Tenant ID: []
components:
  schemas:
    rules.ListResponse:
      type: object
      required:
        - items
        - next_cursor
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/rules.Rule'
        next_cursor:
          anyOf:
            - type: string
            - type: 'null'
    rules.ProblemDetails:
      type: object
      required:
        - detail
        - status
        - title
        - type
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
    rules.Rule:
      type: object
      required:
        - add_to_dataset_prefer_correction
        - created_at
        - display_name
        - evaluator_version
        - extend_only
        - id
        - include_extended_stats
        - is_enabled
        - is_managed_evaluator
        - is_tracing_disabled
        - sampling_rate
        - tenant_id
        - transient
        - updated_at
        - use_corrections_dataset
      properties:
        add_to_annotation_queue_id:
          type: string
          format: uuid
        add_to_annotation_queue_name:
          type: string
        add_to_dataset_id:
          type: string
          format: uuid
        add_to_dataset_name:
          type: string
        add_to_dataset_prefer_correction:
          type: boolean
        alerts:
          type: array
          items:
            $ref: '#/components/schemas/rules.Alert'
        alignment_annotation_queue_id:
          type: string
          format: uuid
        backfill_completed_at:
          type: string
          format: date-time
        backfill_error:
          type: string
        backfill_from:
          type: string
          format: date-time
        backfill_id:
          type: string
          format: uuid
        backfill_progress:
          type: number
        backfill_status:
          type: string
        code_evaluators:
          type: array
          items:
            $ref: '#/components/schemas/rules.CodeEvaluator'
        corrections_dataset_id:
          type: string
          format: uuid
        created_at:
          type: string
          format: date-time
        dataset_id:
          type: string
          format: uuid
        dataset_name:
          type: string
        display_name:
          type: string
        effective_spend_limit:
          $ref: '#/components/schemas/rules.SpendLimit'
        evaluator_id:
          type: string
          format: uuid
        evaluator_name:
          type: string
        evaluator_type:
          type: string
        evaluator_version:
          type: integer
        evaluators:
          type: array
          items:
            $ref: '#/components/schemas/rules.Evaluator'
        extend_annotation_queue_trace_retention:
          type: boolean
        extend_dataset_trace_retention:
          type: boolean
        extend_evaluator_trace_retention:
          type: boolean
        extend_only:
          type: boolean
        extend_webhook_trace_retention:
          type: boolean
        filter:
          type: string
        group_by:
          type: string
          enum:
            - THREAD_ID
            - TRAJECTORY_ID
        id:
          type: string
          format: uuid
        include_extended_stats:
          type: boolean
        is_enabled:
          type: boolean
        is_managed_evaluator:
          type: boolean
        is_tracing_disabled:
          type: boolean
        num_few_shot_examples:
          type: integer
        project_id:
          type: string
          format: uuid
        project_name:
          type: string
        sampling_rate:
          type: number
        spend_limit:
          $ref: '#/components/schemas/rules.SpendLimit'
        spend_usd:
          type: number
        tenant_id:
          type: string
          format: uuid
        thread_filter:
          type: string
        trace_count:
          type: integer
        trace_filter:
          type: string
        transient:
          type: boolean
        tree_filter:
          type: string
        updated_at:
          type: string
          format: date-time
        use_corrections_dataset:
          type: boolean
        webhooks:
          type: array
          items:
            $ref: '#/components/schemas/rules.Webhook'
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
    rules.Alert:
      type: object
      required:
        - routing_key
      properties:
        routing_key:
          type: string
        severity:
          type: string
          enum:
            - CRITICAL
            - WARNING
            - ERROR
            - INFO
        summary:
          type: string
        type:
          type: string
          enum:
            - PAGERDUTY
    rules.CodeEvaluator:
      type: object
      required:
        - code
        - require_attachments
      properties:
        advanced_features_enabled:
          type: boolean
        code:
          type: string
        code_evaluator_input:
          type: string
          enum:
            - THREAD
            - ALL_MESSAGES
            - HUMAN_AI_PAIRS
            - FIRST_HUMAN_LAST_AI
            - TRAJECTORY
        language:
          type: string
          enum:
            - PYTHON
            - JAVASCRIPT
        require_attachments:
          type: boolean
    rules.SpendLimit:
      type: object
      required:
        - limit_usd
        - window
      properties:
        limit_usd:
          type: string
        window:
          type: string
          enum:
            - WEEKLY
    rules.Evaluator:
      type: object
      required:
        - structured
      properties:
        structured:
          $ref: '#/components/schemas/rules.StructuredEvaluator'
    rules.Webhook:
      type: object
      required:
        - url
      properties:
        headers:
          type: object
          additionalProperties:
            type: string
        url:
          type: string
    rules.StructuredEvaluator:
      type: object
      properties:
        hub_ref:
          type: string
        model:
          type: object
          additionalProperties: {}
        playground_settings_id:
          type: string
        prompt:
          type: array
          items:
            items:
              type: string
            type: array
        schema:
          type: object
          additionalProperties: {}
        template_format:
          type: string
        variable_mapping:
          type: object
          additionalProperties:
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
