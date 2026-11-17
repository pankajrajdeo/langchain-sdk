---
title: "List Deployment Namespaces"
description: "Return all allowed Kubernetes namespaces for the deployment namespace selector."
source: "https://docs.langchain.com/api-reference/deployments-v2/list-deployment-namespaces"
category: "docs"
tags: [docs, api-reference, deployments-v2, list-deployment-namespaces]
---

# List Deployment Namespaces

> Return all allowed Kubernetes namespaces for the deployment namespace selector.

## OpenAPI

**https://api.host.langchain.com/openapi.json get /v2/deployments/namespaces**

````yaml
openapi: 3.1.0
info:
  title: LangSmith Deployment Control Plane API
  description: >
    The LangSmith Deployment Control Plane API is used to programmatically
    create and manage

    Agent Server deployments. For example, the APIs can be orchestrated to

    create custom CI/CD workflows.

    ## Host

    https://api.host.langchain.com

    ## Authentication

    To authenticate with the LangSmith Deployment Control Plane API, set the
    `X-Api-Key` header

    to a valid [LangSmith API
    key](https://docs.langchain.com/langsmith/create-account-api-key#create-an-api-key).

    ## Versioning

    Each endpoint path is prefixed with a version (e.g. `v1`, `v2`).

    ## Quick Start

    1. Call `POST /v2/deployments` to create a new Deployment. The response body
    contains the Deployment ID (`id`) and the ID of the latest (and first)
    revision (`latest_revision_id`).

    1. Call `GET /v2/deployments/{deployment_id}` to retrieve the Deployment.
    Set `deployment_id` in the URL to the value of Deployment ID (`id`).

    1. Poll for revision `status` until `status` is `DEPLOYED` by calling `GET
    /v2/deployments/{deployment_id}/revisions/{latest_revision_id}`.

    1. Call `PATCH /v2/deployments/{deployment_id}` to update the deployment.
  version: 0.1.0
servers: []
security: []
paths:
  /v2/deployments/namespaces:
    get:
      tags:
        - Deployments (v2)
      summary: List Deployment Namespaces
      description: >-
        Return all allowed Kubernetes namespaces for the deployment namespace
        selector.
      operationId: list_deployment_namespaces_v2_deployments_namespaces_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentNamespacesResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    DeploymentNamespacesResponse:
      properties:
        items:
          items:
            $ref: '#/components/schemas/DeploymentNamespace'
          type: array
          title: Items
          description: >-
            Namespaces the data-plane administrator has allowed for the caller's
            workspace, sorted by name. Empty on SaaS, outside BYOC data planes,
            or when none are allowed.
      type: object
      required:
        - items
      title: DeploymentNamespacesResponse
      description: Response body for the deployment namespaces endpoint.
    DeploymentNamespace:
      properties:
        name:
          type: string
          title: Name
          description: >-
            Namespace name, accepted as `source_config.k8s_namespace` when
            creating a deployment.
      type: object
      required:
        - name
      title: DeploymentNamespace
      description: A Kubernetes namespace new deployments may be placed in.

````
