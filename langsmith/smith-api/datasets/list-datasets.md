---
title: "List datasets"
description: "Returns one page of the datasets in the workspace, filtered and sorted by the query parameters. Pass the next_cursor of a response as cursor, with the same filters and sort, to get the next page..."
source: "https://docs.langchain.com/langsmith/smith-api/datasets/list-datasets"
category: "docs"
tags: [docs, langsmith, smith-api, datasets, list-datasets]
---

# List datasets

> Returns one page of the datasets in the workspace, filtered and sorted by the query parameters.
Pass the next_cursor of a response as cursor, with the same filters and sort, to get the next page. next_cursor is null on the last page.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json get /api/v2/datasets**

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
  /api/v2/datasets:
    get:
      tags:
        - datasets
      summary: List datasets
      description: >-
        Returns one page of the datasets in the workspace, filtered and sorted
        by the query parameters.

        Pass the next_cursor of a response as cursor, with the same filters and
        sort, to get the next page. next_cursor is null on the last page.
      parameters:
        - description: >-
            Return only the datasets with these IDs. Repeat the parameter for
            several IDs.
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
        - description: >-
            Return only datasets of these data types. Repeat the parameter for
            several types.
          name: data_type
          in: query
          style: form
          explode: true
          schema:
            type: array
            items:
              $ref: '#/components/schemas/DataType'
            title: Data Type
        - description: Return only the dataset with exactly this name.
          name: name
          in: query
          schema:
            type: string
            title: Name
        - description: Return only datasets whose name contains this text, ignoring case.
          name: name_contains
          in: query
          schema:
            type: string
            title: Name Contains
        - description: >-
            A JSON object. Return only datasets whose metadata contains every
            key and value in it.
          name: metadata
          in: query
          schema:
            type: string
            title: Metadata
        - description: Return only datasets tagged with all of these tag value IDs.
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
        - description: Leave out datasets that store corrections for an evaluator.
          name: exclude_corrections_datasets
          in: query
          schema:
            type: boolean
            default: false
            title: Exclude Corrections Datasets
        - description: >-
            Fields to leave out of each dataset. An excluded example_count is
            returned as null and makes the response faster.
          name: exclude
          in: query
          style: form
          explode: true
          schema:
            type: array
            items:
              $ref: '#/components/schemas/GetDatasetsSelect'
            title: Exclude
        - description: >-
            Field to sort by. last_session_start_time is the start time of the
            most recent experiment on the dataset. Datasets without a value come
            last in both orders. While a sort value changes, for example when an
            experiment starts, a dataset can be skipped or listed twice across
            pages. Sort by created_at for a stable walk.
          name: sort_by
          in: query
          schema:
            $ref: '#/components/schemas/SortByDatasetColumn'
            default: last_session_start_time
        - description: Sort direction.
          name: sort_order
          in: query
          schema:
            enum:
              - asc
              - desc
            type: string
            default: desc
            title: Sort Order
        - description: Maximum number of datasets to return.
          name: page_size
          in: query
          schema:
            type: integer
            maximum: 100
            minimum: 1
            title: Page Size
            default: 20
        - description: >-
            The next_cursor of the previous response. Omit it for the first
            page.
          name: cursor
          in: query
          schema:
            type: string
            title: Cursor
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/datasets.ListDatasetsV2Response'
        '400':
          description: Invalid query parameter or cursor
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
          description: >-
            No permission to read datasets, or to read one of the requested
            datasets
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
      security:
        - API Key: []
          Tenant ID: []
        - Bearer Auth: []
          Tenant ID: []
components:
  schemas:
    DataType:
      type: string
      enum:
        - kv
        - llm
        - chat
      title: DataType
      description: Enum for dataset data types.
    GetDatasetsSelect:
      type: string
      enum:
        - example_count
      title: GetDatasetsSelect
    SortByDatasetColumn:
      type: string
      enum:
        - name
        - created_at
        - last_session_start_time
        - example_count
        - session_count
        - modified_at
      title: SortByDatasetColumn
      description: Enum for available dataset columns to sort by.
    datasets.ListDatasetsV2Response:
      type: object
      required:
        - items
        - next_cursor
      properties:
        items:
          description: Datasets on this page.
          type: array
          items:
            $ref: '#/components/schemas/Dataset'
        next_cursor:
          description: Cursor for the next page. Null when this is the last page.
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
    Dataset:
      properties:
        name:
          type: string
          title: Name
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        created_at:
          type: string
          format: date-time
          title: Created At
        inputs_schema_definition:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Inputs Schema Definition
        outputs_schema_definition:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Outputs Schema Definition
        externally_managed:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Externally Managed
          default: false
        transformations:
          anyOf:
            - items:
                $ref: '#/components/schemas/DatasetTransformation'
              type: array
            - type: 'null'
          title: Transformations
        data_type:
          anyOf:
            - $ref: '#/components/schemas/DataType'
            - type: 'null'
          default: kv
        id:
          type: string
          format: uuid
          title: Id
        tenant_id:
          type: string
          format: uuid
          title: Tenant Id
        example_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Example Count
        session_count:
          type: integer
          title: Session Count
        modified_at:
          type: string
          format: date-time
          title: Modified At
        last_session_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Session Start Time
        metadata:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Metadata
        baseline_experiment_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Baseline Experiment Id
      type: object
      required:
        - name
        - id
        - tenant_id
        - session_count
        - modified_at
      title: Dataset
      description: Dataset schema.
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
    DatasetTransformation:
      properties:
        path:
          items:
            type: string
          type: array
          title: Path
        transformation_type:
          $ref: '#/components/schemas/DatasetTransformationType'
      type: object
      required:
        - path
        - transformation_type
      title: DatasetTransformation
    DatasetTransformationType:
      type: string
      enum:
        - convert_to_openai_message
        - convert_to_openai_tool
        - remove_system_messages
        - remove_extra_fields
        - extract_tools_from_run
      title: DatasetTransformationType
      description: >-
        Enum for dataset transformation types.

        Ordering determines the order in which transformations are applied if
        there are multiple transformations on the same path.
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
