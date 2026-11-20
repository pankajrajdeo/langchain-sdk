---
title: "Create a project or experiment"
description: "Create a session, or update an existing session with the same name when upsert is true. Returns the refreshed session representation without optional run statistics."
source: "https://docs.langchain.com/langsmith/smith-api/sessions/create-a-project-or-experiment"
category: "docs"
tags: [docs, langsmith, smith-api, sessions, create-a-project-or-experiment]
---

# Create a project or experiment

> Create a session, or update an existing session with the same name when upsert is true. Returns the refreshed session representation without optional run statistics.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json post /api/v2/sessions**

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
  /api/v2/sessions:
    post:
      tags:
        - sessions
      summary: Create a project or experiment
      description: >-
        Create a session, or update an existing session with the same name when
        upsert is true. Returns the refreshed session representation without
        optional run statistics.
      parameters:
        - description: Update an existing session with the same name
          name: upsert
          in: query
          schema:
            type: boolean
            title: Upsert
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/tracer_sessions.CreateSessionRequest'
      responses:
        '200':
          description: Existing session updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Session'
        '201':
          description: Session created
          headers:
            Location:
              description: URL of the created session
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Session'
        '400':
          description: Invalid request
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '401':
          description: Authentication required
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '403':
          description: Permission denied
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '404':
          description: Dataset not found
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '409':
          description: Session conflict
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
      security:
        - API Key: []
          Tenant ID: []
        - Bearer Auth: []
          Tenant ID: []
components:
  schemas:
    tracer_sessions.CreateSessionRequest:
      type: object
      required:
        - type
      properties:
        default_dataset_id:
          type: string
          format: uuid
        description:
          type: string
        end_time:
          type: string
          format: date-time
        evaluator_keys:
          items:
            type: string
          type: array
        extra:
          type: object
          additionalProperties: {}
        id:
          type: string
          format: uuid
        kicked_off_by:
          type: string
        longlived_ttl_days:
          description: >-
            LonglivedTTLDays overrides long-lived trace retention. Null restores
            the workspace default.
          anyOf:
            - type: integer
            - type: 'null'
        name:
          type: string
        num_examples:
          type: integer
        num_repetitions:
          type: integer
        reference_dataset_id:
          type: string
          format: uuid
        start_time:
          type: string
          format: date-time
        tag_value_ids:
          items:
            type: string
          type: array
        trace_tier:
          type: string
          enum:
            - LONG_LIVED
            - SHORT_LIVED
        type:
          description: >-
            Type identifies a tracing project, Agent tracing project, or
            experiment.
          type: string
          enum:
            - PROJECT
            - AGENT
            - EXPERIMENT
    Session:
      properties:
        start_time:
          type: string
          format: date-time
          title: Start Time
        end_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: End Time
        extra:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Extra
        name:
          type: string
          title: Name
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        default_dataset_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Default Dataset Id
        reference_dataset_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Reference Dataset Id
        trace_tier:
          anyOf:
            - type: string
              enum:
                - LONG_LIVED
                - SHORT_LIVED
            - type: 'null'
          default: null
          title: Trace Tier
        longlived_ttl_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Longlived Ttl Days
          description: >-
            Retention in days for traces while trace_tier is longlived. One of
            the deployment's allowed values (allowed_longlived_ttl_days in
            /info), up to the maximum of the deployment. The value is kept while
            trace_tier is shortlived. Null means the project uses the workspace
            retention.
        id:
          type: string
          format: uuid
          title: Id
        run_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Run Count
        latency_p50:
          anyOf:
            - type: number
            - type: 'null'
          title: Latency P50
        latency_p99:
          anyOf:
            - type: number
            - type: 'null'
          title: Latency P99
        first_token_p50:
          anyOf:
            - type: number
            - type: 'null'
          title: First Token P50
        first_token_p99:
          anyOf:
            - type: number
            - type: 'null'
          title: First Token P99
        total_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Total Tokens
        prompt_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Prompt Tokens
        completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Completion Tokens
        total_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Total Cost
        prompt_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Prompt Cost
        completion_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Completion Cost
        tenant_id:
          type: string
          format: uuid
          title: Tenant Id
        last_run_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Run Start Time
        last_run_start_time_live:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Run Start Time Live
        feedback_stats:
          anyOf:
            - type: object
              additionalProperties:
                $ref: '#/components/schemas/SessionFeedbackStat'
            - type: 'null'
          title: Feedback Stats
          description: Feedback on the session's runs, by feedback key.
        session_feedback_stats:
          anyOf:
            - type: object
              additionalProperties:
                $ref: '#/components/schemas/SessionFeedbackStat'
            - type: 'null'
          title: Session Feedback Stats
          description: Feedback on the session itself, by feedback key.
        run_facets:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Run Facets
        error_rate:
          anyOf:
            - type: number
            - type: 'null'
          title: Error Rate
        streaming_rate:
          anyOf:
            - type: number
            - type: 'null'
          title: Streaming Rate
        test_run_number:
          anyOf:
            - type: integer
            - type: 'null'
          title: Test Run Number
        experiment_progress:
          anyOf:
            - $ref: '#/components/schemas/ExperimentProgress'
            - type: 'null'
        type:
          type: string
          enum:
            - PROJECT
            - AGENT
            - EXPERIMENT
          title: Type
          description: >-
            `PROJECT` for a tracing project, `AGENT` for an Agent's tracing
            project, or `EXPERIMENT` for an evaluation run against a dataset.
      type: object
      required:
        - id
        - tenant_id
        - name
        - start_time
        - type
      title: Session
      description: TracerSession schema.
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
    SessionFeedbackStat:
      type: object
      title: SessionFeedbackStat
      description: Aggregate feedback for one feedback key.
      required:
        - 'n'
        - avg
        - median
        - stdev
        - min
        - max
        - errors
        - values
        - type
        - contains_thread_feedback
      properties:
        'n':
          type: integer
          description: Number of feedback scores for this key.
        avg:
          anyOf:
            - type: number
            - type: 'null'
          description: Mean numeric score.
        median:
          anyOf:
            - type: number
            - type: 'null'
          description: Median numeric score.
        stdev:
          anyOf:
            - type: number
            - type: 'null'
          description: Standard deviation of numeric scores.
        min:
          anyOf:
            - type: number
            - type: 'null'
          description: Lowest numeric score.
        max:
          anyOf:
            - type: number
            - type: 'null'
          description: Highest numeric score.
        errors:
          type: integer
          description: Number of feedback entries recorded as errors.
        values:
          type: object
          additionalProperties:
            type: integer
          description: Count of each categorical value.
        type:
          type: string
          enum:
            - PRIMARY
            - COMPOSITE
          description: >-
            `PRIMARY` for recorded feedback, `COMPOSITE` for a score computed
            from other feedback keys.
        contains_thread_feedback:
          type: boolean
          description: Whether any feedback was left on a thread.
    ExperimentProgress:
      properties:
        expected_run_count:
          type: integer
          title: Expected Run Count
        run_progress:
          type: number
          title: Run Progress
        evaluator_progress:
          additionalProperties:
            type: number
          type: object
          title: Evaluator Progress
      type: object
      required:
        - expected_run_count
        - run_progress
        - evaluator_progress
      title: ExperimentProgress
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
