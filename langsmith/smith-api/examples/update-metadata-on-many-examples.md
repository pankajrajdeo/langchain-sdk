---
title: "Update metadata on many examples"
description: "Applies the same metadata changes, in order, to every listed example in a dataset. Examples that are not in the dataset or were deleted are skipped; the rest are updated together, so if the update..."
source: "https://docs.langchain.com/langsmith/smith-api/examples/update-metadata-on-many-examples"
category: "docs"
tags: [docs, langsmith, smith-api, examples, update-metadata-on-many-examples]
---

# Update metadata on many examples

> Applies the same metadata changes, in order, to every listed example in
a dataset. Examples that are not in the dataset or were deleted are
skipped; the rest are updated together, so if the update fails none of
them change. Answers 207 with one status per submitted example ID:
UPDATED, or NOT_FOUND for a skipped example. Metadata keys the
operations do not name keep their values. To add examples to a split or
remove them from one, use ARRAY_ADD or ARRAY_REMOVE on the dataset_split
key. Requires permission to update datasets.

## OpenAPI

**/langsmith/langsmith-platform-openapi.json patch /api/v1/platform/datasets/{dataset_id}/examples/metadata**

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
  /api/v1/platform/datasets/{dataset_id}/examples/metadata:
    patch:
      tags:
        - examples
      summary: Update metadata on many examples
      description: |-
        Applies the same metadata changes, in order, to every listed example in
        a dataset. Examples that are not in the dataset or were deleted are
        skipped; the rest are updated together, so if the update fails none of
        them change. Answers 207 with one status per submitted example ID:
        UPDATED, or NOT_FOUND for a skipped example. Metadata keys the
        operations do not name keep their values. To add examples to a split or
        remove them from one, use ARRAY_ADD or ARRAY_REMOVE on the dataset_split
        key. Requires permission to update datasets.
      parameters:
        - description: Dataset ID
          name: dataset_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/examples.BulkUpdateMetadataRequest'
      responses:
        '207':
          description: Multi-Status
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/examples.BulkUpdateMetadataResponse'
        '400':
          description: >-
            Malformed body, or more example_ids, operations or values than
            allowed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
        '403':
          description: Forbidden
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
        '422':
          description: Invalid example ID, operation, key or value
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/shared.ProblemDetails'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    examples.BulkUpdateMetadataRequest:
      type: object
      required:
        - example_ids
        - operations
      properties:
        example_ids:
          description: >-
            The IDs of the examples to change; at most 10000. IDs of examples
            that are not in

            the dataset, or were deleted, are skipped and reported as NOT_FOUND.
          type: array
          items:
            type: string
            format: uuid
        operations:
          description: >-
            The metadata changes to apply, in order; at most 50, of which at
            most 10 are

            array operations.
          type: array
          items:
            $ref: '#/components/schemas/examples.MetadataOperation'
    examples.BulkUpdateMetadataResponse:
      type: object
      required:
        - statuses
      properties:
        statuses:
          description: One entry per submitted example ID, in request order.
          type: array
          items:
            $ref: '#/components/schemas/examples.BulkUpdateMetadataStatus'
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
    examples.MetadataOperation:
      type: object
      required:
        - key
        - operation
      properties:
        key:
          description: >-
            The top-level metadata key to change, at most 255 bytes. Use
            dataset_split with

            ARRAY_ADD or ARRAY_REMOVE to change which splits the examples belong
            to.
          type: string
        operation:
          description: >-
            The change to make: SET replaces the value at key; ARRAY_ADD adds
            values to the

            list at key; ARRAY_REMOVE removes values from it. For array
            operations, a missing

            or non-list value starts as an empty list, except for dataset_split,
            where it

            starts as the base split.
          type: string
          enum:
            - SET
            - ARRAY_ADD
            - ARRAY_REMOVE
        value:
          description: >-
            The new value for a SET operation; any JSON value, at most 64 KB.
            Ignored by

            array operations.
        values:
          description: >-
            The values to add or remove for an array operation; at most 1000
            values of at

            most 255 bytes each. Ignored by SET.
          type: array
          items:
            type: string
    examples.BulkUpdateMetadataStatus:
      type: object
      required:
        - id
        - status
      properties:
        description:
          description: Why the example was not updated. Omitted when it was.
          type: string
        id:
          description: The example ID, as submitted.
          type: string
          format: uuid
        status:
          description: >-
            UPDATED if the example's metadata was changed; NOT_FOUND if the
            example is not in

            the dataset or was deleted.
          type: string
          enum:
            - UPDATED
            - NOT_FOUND
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
