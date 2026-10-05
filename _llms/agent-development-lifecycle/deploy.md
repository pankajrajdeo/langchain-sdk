---
title: "Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE Deploy"
description: "Documentation for LangSmith, Fleet, and our open source packages."
source: "https://docs.langchain.com/_llms/agent-development-lifecycle/deploy"
category: "docs"
tags: [docs, llms, agent-development-lifecycle, deploy]
---

# Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE Deploy

> Documentation for LangSmith, Fleet, and our open source packages.

## Deploy

- [AGENT DEVELOPMENT LIFECYCLE / Deploy / Get started (150 pages)](deploy/get-started.md): Documentation for AGENT DEVELOPMENT LIFECYCLE / Deploy / Get started.

### Agent Server

- [Agent Server](../../langsmith/agent-server-overview.md): Configure and operate the LangSmith Agent Server runtime, including capabilities, application structure, auth, and customization.

#### Develop your application

- [Application structure](../../langsmith/application-structure.md)

##### Set up dependencies

- [How to set up an application with requirements.txt](../../langsmith/setup-app-requirements-txt.md)
- [How to set up an application with pyproject.toml](../../langsmith/setup-pyproject.md)
- [How to set up a JavaScript application](../../langsmith/setup-javascript.md)
- [How to customize the Dockerfile](../../langsmith/custom-docker.md)
- [Monorepo support](../../langsmith/monorepo-support.md)

##### Persistence

- [Configure checkpointer backend](../../langsmith/configure-checkpointer.md): Configure Agent Server to use PostgreSQL, MongoDB, or a custom implementation for checkpoint storage.
- [How to add TTLs to your application](../../langsmith/configure-ttl.md)
- [How to add semantic search to your agent deployment](../../langsmith/semantic-search.md)

#### Capabilities

- [Agent Server](../../langsmith/agent-server.md)
- [Use threads](../../langsmith/use-threads.md)
- [How to interact with a deployment using RemoteGraph](../../langsmith/use-remote-graph.md)
- [Use cron jobs](../../langsmith/cron-jobs.md)
- [Streaming API](../../langsmith/streaming.md)
- [Human-in-the-loop using server API](../../langsmith/add-human-in-the-loop.md)
- [Time travel using the server API](../../langsmith/human-in-the-loop-time-travel.md)
- [Use webhooks](../../langsmith/use-webhooks.md)
- [Distributed tracing with Agent Server](../../langsmith/agent-server-distributed-tracing.md): Unify traces when calling your deployed Agent Server from another service using RemoteGraph or the SDK.
- [MCP endpoint in Agent Server](../../langsmith/server-mcp.md)
- [A2A endpoint in Agent Server](../../langsmith/server-a2a.md): Use the A2A protocol to enable agent-to-agent communication with distributed tracing in LangSmith.
- [Agent Server changelog](../../langsmith/agent-server-changelog-link.md)

##### Assistants

- [Assistants](../../langsmith/assistants.md)
- [Manage assistants](../../langsmith/configuration-cloud.md)

##### Runs

- [Runs](../../langsmith/runs.md): An overview of runs in Agent Server, including how to kick off background runs, stateless runs, and cancel runs.
- [How to kick off background runs](../../langsmith/background-run.md)
- [How to run multiple assistants on the same thread](../../langsmith/same-thread.md)
- [Stateless runs](../../langsmith/stateless-runs.md)
- [How to cancel a run](../../langsmith/cancel-run.md): Cancel a single run or multiple runs via the API, and choose between interrupt and rollback actions.

##### Double-texting

- [Double texting](../../langsmith/double-texting.md)
- [Interrupt concurrent](../../langsmith/interrupt-concurrent.md)
- [Rollback Concurrent](../../langsmith/rollback-concurrent.md)
- [Reject Concurrent](../../langsmith/reject-concurrent.md)
- [Enqueue concurrent](../../langsmith/enqueue-concurrent.md)

#### How to build

- [How to collect user feedback for Agent Server runs](../../langsmith/agent-server-feedback.md)
- [How to implement generative user interfaces with LangGraph](../../langsmith/generative-ui-react.md)
- [Implement a CI/CD pipeline using LangSmith Deployment and Evaluation](../../langsmith/cicd-pipeline-example.md)

#### Auth & access control

- [Authentication & access control](../../langsmith/auth.md)
- [Add custom authentication](../../langsmith/custom-auth.md)
- [Document API authentication in OpenAPI](../../langsmith/openapi-security.md)
- [Set up Agent Auth](../../langsmith/agent-auth.md): Enable secure access from agents to any system using OAuth 2.0 credentials with Agent Auth.

##### Custom auth tutorial

- [Set up custom authentication](../../langsmith/set-up-custom-auth.md)
- [Make conversations private](../../langsmith/resource-auth.md)
- [Isolate store data per user](../../langsmith/store-auth.md): Scope long-term store data to each authenticated user in LangSmith Deployment using auth handlers.
- [Connect an authentication provider](../../langsmith/add-auth-server.md)

#### Server customization

- [Use server-side caching](../../langsmith/caching.md): Cache values server-side in your agent deployment using stale-while-revalidate and key-value cache APIs.
- [Configure IAM authentication for data stores](../../langsmith/configure-iam-auth.md): Configure Agent Server to use cloud workload identities for PostgreSQL and Redis authentication.
- [Add encryption at rest](../../langsmith/encryption.md)
- [Rebuild graph at runtime](../../langsmith/graph-rebuild.md): Rebuild your graph with different configurations for each run using ServerRuntime.

##### Replace built-in backends

- [How to use a custom store](../../langsmith/custom-store.md): Replace the built-in Postgres store with a custom BaseStore implementation in your agent deployment.
- [How to use a custom checkpointer](../../langsmith/custom-checkpointer.md): Replace the built-in Postgres checkpointer with a custom BaseCheckpointSaver implementation in your agent deployment.

##### Extend the HTTP server

- [How to add custom routes](../../langsmith/custom-routes.md)
- [How to add custom middleware](../../langsmith/custom-middleware.md)
- [How to add custom lifespan events](../../langsmith/custom-lifespan.md)

##### Headers and logging

- [Use HTTP headers for runtime configuration](../../langsmith/configurable-headers.md)
- [Include HTTP headers in server logs](../../langsmith/configurable-logs.md)

### Deploy to Cloud

- [Deploy to Cloud](../../langsmith/deploy-to-cloud-overview.md): Deploy LangSmith agents to LangChain-managed Cloud infrastructure on AWS and GCP.
- [Cloud platform features](../../langsmith/cloud-platform-features.md): Cloud-only platform features for LangSmith Deployment, including data regions, static IP addresses, payload limits, and deployment types.

#### Deployment guide

- [Create a deployment](../../langsmith/deploy-to-cloud.md): Create a LangSmith Cloud deployment from the LangSmith UI or LangGraph CLI.
- [Revisions](../../langsmith/deployment-revisions.md): Create and manage revisions for a LangSmith Cloud deployment.
- [Monitor a deployment](../../langsmith/monitor-deployment.md): View build logs, server logs, and metrics for a LangSmith Cloud deployment.
- [Preview builds](../../langsmith/preview-builds.md): Create temporary preview deployments for pull requests to test Agent Server changes before merging.
- [Manage a deployment](../../langsmith/manage-deployment.md): Configure branch updates and delete a LangSmith Cloud deployment.

#### Reference

- [Cloud Agent Server environment variables](../../langsmith/env-var-cloud.md): Environment variables supported by the LangSmith Agent Server when deployed on Cloud.

### Deploy to Self-hosted

- [Deploy to self-hosted](../../langsmith/deploy-to-self-hosted-overview.md): Run the LangSmith Deployment platform on your own infrastructure with full control over data, networking, and resources.
- [Deploy with control plane](../../langsmith/deploy-with-control-plane.md): Build Docker images and deploy applications to a self-hosted LangSmith instance using the control plane UI.
- [Hybrid](../../langsmith/hybrid.md): A LangSmith Deployment setup where you self-host Agent Servers in your infrastructure and send traces to LangSmith Cloud or a self-hosted LangSmith instance.
- [Self-host standalone servers](../../langsmith/deploy-standalone-server.md): Deploy standalone Agent Servers using Docker, Docker Compose, or Kubernetes without the LangSmith control plane.

#### Configure

- [Self-hosted platform features](../../langsmith/self-hosted-platform-features.md): Self-hosted-only platform features for LangSmith Deployment, including custom databases, listeners, and resource customization.
- [Agent Server metrics](../../langsmith/self-hosted-agent-server-metrics.md): Reference for Agent Server OpenTelemetry metrics on self-hosted deployments, including Deployment UI metrics, internal metrics, and Datadog export.
- [Configure Agent Server for scale](../../langsmith/agent-server-scale.md): Tune the Agent Server for self-hosted deployments—write load, read load, and example Helm configurations for different load patterns.
- [Troubleshooting for self-hosted deployments](../../langsmith/diagnostics-self-hosted.md): Diagnostic steps for troubleshooting self-hosted LangSmith Deployment issues before contacting support.

#### Reference

- [Self-hosted Agent Server environment variables](../../langsmith/env-var-self-hosted.md): Environment variables supported by the LangSmith Agent Server when deployed on self-hosted infrastructure.

### Prompt & Context Hub

- [Prompt & Context Hub](../../langsmith/prompt-context-hub.md): Store, version, and update the prompts and contexts your agents use in production.

#### Prompts

- [Prompt engineering quickstart](../../langsmith/prompt-engineering-quickstart.md)
- [Prompt engineering concepts](../../langsmith/prompt-engineering-concepts.md)
- [LangSmith Chat](../../langsmith/chat-prompt-engineering.md): Use Chat to optimize prompts in the Playground.
- [Model providers](../../langsmith/playground-model-providers.md)
- [Write your prompt with AI](../../langsmith/write-prompt-with-ai.md)

##### Create and manage prompts

- [Create a prompt](../../langsmith/create-a-prompt.md)
- [Manage prompts](../../langsmith/manage-prompts.md): Manage prompt versions, environments, and access controls in LangSmith.
- [Manage prompts programmatically](../../langsmith/manage-prompts-programmatically.md)
- [Configure prompt settings](../../langsmith/managing-model-configurations.md)
- [Prompt template format guide](../../langsmith/prompt-template-format.md)
- [Use tools in a prompt](../../langsmith/use-tools.md)
- [Include multimodal content in a prompt](../../langsmith/multimodal-content.md)

##### Connect to models

- [Connect to an OpenAI compliant model provider/proxy](../../langsmith/custom-openai-compliant-model.md)
- [Connect to a TypeSafe-compatible model provider](../../langsmith/typesafe-compatible-model.md): Point LangSmith decision model evaluators at any server that implements the TypeSafe System One API, such as OpenRouter or a self-hosted model.
- [Connect to a custom model](../../langsmith/custom-endpoint.md)

#### Context Hub

- [Context engineering concepts](../../langsmith/context-engineering-concepts.md): Core concepts for context engineering in LangSmith, including skills, agents, versioning, and sharing.
- [Use the Context Hub](../../langsmith/use-the-context-hub.md): Learn how to create, view, and promote context in the LangSmith Context Hub.
- [Manage contexts with the SDK](../../langsmith/manage-contexts-sdk.md): Use the LangSmith SDK to push, pull, list, and delete agent and skill repos in the Context Hub programmatically.
- [Configure Context Hub commit webhooks](../../langsmith/context-hub-webhooks.md): Send Context Hub commit events to an external HTTPS endpoint and verify that LangSmith signed each request.

#### Tutorials

- [Optimize a classifier](../../langsmith/optimize-classifier.md)
- [How to sync prompts with GitHub](../../langsmith/prompt-commit.md)
- [Test multi-turn conversations](../../langsmith/multiple-messages.md)

### Sandboxes

- [LangSmith Sandboxes](../../langsmith/sandboxes.md): Use LangSmith managed sandboxes to safely execute code and interact with the filesystem in isolated environments.
- [Sandbox snapshots](../../langsmith/sandbox-snapshots.md): Build and capture reusable filesystem images for sandboxes.
- [Sandbox service URLs](../../langsmith/sandbox-service-urls.md): Access HTTP services running inside sandboxes via authenticated URLs, from a browser or programmatically.
- [Sandbox download links](../../langsmith/sandbox-download-links.md): Share a single file from a sandbox as a link that needs no LangSmith credential.
- [Sandbox auth proxy](../../langsmith/sandbox-auth-proxy.md): Inject credentials into outbound requests and control which destinations a sandbox can reach.
- [Sandbox mounts](../../langsmith/sandbox-mounts.md): Mount S3 buckets, GCS buckets, public Git repositories, and Context Hub repos into LangSmith sandboxes.
- [Sandbox access permissions](../../langsmith/sandbox-permissions.md): Control who in your workspace can interact with a sandbox after it has been created.
- [Sandbox CLI](../../langsmith/sandbox-cli.md): Create, inspect, connect to, and tunnel into LangSmith sandboxes from the command line.
- [Sandbox SDK usage](../../langsmith/sandbox-sdk.md): Create and manage sandboxes programmatically with the Python or TypeScript SDK.
- [Harbor integrations](../../langsmith/harbor-integrations.md): Run evaluations, Deep Agents, and sandboxes on LangSmith with Harbor.

## OpenAPI Specs

- [agent-server-openapi](https://docs.langchain.com/langsmith/agent-server-openapi.json)
- [openapi](https://api.host.langchain.com/openapi.json)
