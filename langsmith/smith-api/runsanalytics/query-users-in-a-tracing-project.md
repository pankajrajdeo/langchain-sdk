---
title: "Query users in a tracing project"
description: "GET with body payload — no resources created. Returns users ordered by their most recent matching finished root run, with cursor pagination. Costs and token usage aggregate the window's runs that..."
source: "https://docs.langchain.com/langsmith/smith-api/runsanalytics/query-users-in-a-tracing-project"
category: "docs"
tags: [docs, langsmith, smith-api, runsanalytics, query-users-in-a-tracing-project]
---

# Query users in a tracing project

> GET with body payload — no resources created. Returns users ordered by their most recent matching finished root run, with cursor pagination. Costs and token usage aggregate the window's runs that carry the user's metadata.user_id. The activity window defaults to seven days and must not exceed 31 days. Continuation keeps a fixed activity window but does not provide a snapshot; concurrent activity changes can cause skipped or repeated users.
Users whose statistics are not yet available have stats_status=pending and null trace_count and error_count. Query again to retrieve statistics; stats_status=ready means statistics were returned, but they may still lag recent activity. Other unavailable metrics are omitted. Backend query failures still return an error.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json post /api/v2/runs/users/query**

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
  /api/v2/runs/users/query:
    post:
      tags:
        - runsanalytics
      summary: Query users in a tracing project
      description: >-
        GET with body payload — no resources created. Returns users ordered by
        their most recent matching finished root run, with cursor pagination.
        Costs and token usage aggregate the window's runs that carry the user's
        metadata.user_id. The activity window defaults to seven days and must
        not exceed 31 days. Continuation keeps a fixed activity window but does
        not provide a snapshot; concurrent activity changes can cause skipped or
        repeated users.

        Users whose statistics are not yet available have stats_status=pending
        and null trace_count and error_count. Query again to retrieve
        statistics; stats_status=ready means statistics were returned, but they
        may still lag recent activity. Other unavailable metrics are omitted.
        Backend query failures still return an error.
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/runsanalytics.QueryUsersRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/runsanalytics.QueryUsersResponse'
        '400':
          description: Invalid query or activity window exceeds 31 days
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '403':
          description: Insufficient permission or reads unavailable for this workspace
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '501':
          description: User activity queries are not enabled for this workspace
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '503':
          description: Service Unavailable
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
      security:
        - API Key: []
          Tenant ID: []
        - Bearer Auth: []
          Tenant ID: []
components:
  schemas:
    runsanalytics.QueryUsersRequest:
      type: object
      required:
        - project_id
      properties:
        cursor:
          description: >-
            Cursor continues recent-user discovery with state independent of the
            number of users already returned.

            The activity window stays fixed, but changes to matching activity
            can cause skipped or repeated users.

            Maximum encoded length is 65536 bytes.
          type: string
          maxLength: 65536
        filter:
          description: >-
            Filter narrows which completed root runs count toward a user, using
            a LangSmith filter expression evaluated

            against each root run; users with no matching root run are not
            returned. For example: eq(status, "error").

            See
            https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language
            for syntax.
          type: string
          example: eq(status, "error")
        max_start_time:
          description: >-
            MaxStartTime is an exclusive upper bound on root start time;
            defaults to the current time on the first page. Continuation
            preserves the original window.
          type: string
          format: date-time
        min_start_time:
          description: >-
            MinStartTime is an inclusive lower bound on root start time;
            defaults to seven days before max_start_time. The window must not
            exceed 31 days.
          type: string
          format: date-time
        page_size:
          description: >-
            Limit sets the page size. Changing it preserves the cursor's
            position and activity window.
          type: integer
          default: 20
          maximum: 100
          minimum: 1
        project_id:
          description: ProjectID identifies the tracing project whose users to query.
          type: string
          format: uuid
        stats_wait_ms:
          description: >-
            StatsWaitMs limits how long the request waits for user statistics.
            When the limit

            passes, users are returned with stats_status=pending; fetch their
            statistics with

            /v2/runs/users/stats. Omit to wait for statistics until the request
            deadline.
          type: integer
          maximum: 60000
          minimum: 1
        trace_filter:
          description: >-
            TraceFilter restricts the traces used to discover users and compute
            their statistics. Project and trace access restrictions always
            apply.
          type: string
    runsanalytics.QueryUsersResponse:
      type: object
      required:
        - is_partial
        - items
        - next_cursor
      properties:
        is_partial:
          description: >-
            IsPartial is true when discovery reaches its work limit before
            filling the requested page.

            A full page can have is_partial=false and a non-null next_cursor.

            Always use next_cursor to determine whether to continue, including
            after an empty partial page.

            Available statistics for returned users cover the entire requested
            window.

            Missing statistics are indicated by each user's stats_status, not
            is_partial.
          type: boolean
        items:
          type: array
          items:
            $ref: '#/components/schemas/runsanalytics.ProjectUser'
        next_cursor:
          anyOf:
            - type: string
            - type: 'null'
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
    runsanalytics.ProjectUser:
      type: object
      required:
        - error_count
        - last_seen
        - stats_status
        - trace_count
        - user_id
      properties:
        error_count:
          description: >-
            ErrorCount counts finished root runs that failed. Null while
            statistics

            are pending, or when SmithDB returns no error rate.
          anyOf:
            - type: integer
            - type: 'null'
        error_rate:
          type: number
        last_seen:
          description: LastSeen is the latest start time among matching root runs.
          type: string
          format: date-time
        latency_p50_seconds:
          type: number
        latency_p99_seconds:
          type: number
        stats_status:
          description: >-
            StatsStatus is pending when no statistics group is available, or
            ready when

            statistics were returned. Ready statistics may still lag recent
            activity.

            Query again to retrieve statistics that were pending.
          type: string
          enum:
            - pending
            - ready
        total_cost:
          type: number
        total_tokens:
          description: >-
            TotalTokens and TotalCost sum the window's runs that carry this
            user's

            metadata.user_id. That is not the total for the user's traces: a run
            tagged

            with a different user is not counted here, and an untagged run
            counts for

            no user at all.
          type: integer
        trace_count:
          description: >-
            TraceCount counts finished root runs; runs that have not finished
            are not

            counted. Null while statistics are pending.
          anyOf:
            - type: integer
            - type: 'null'
        user_id:
          description: >-
            UserID is the application-defined identity from a root run's
            metadata.user_id,

            returned as a string. Values need not be UUIDs.
          type: string
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
