---
title: "Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE Deploy Get started"
description: "Documentation for LangSmith, Fleet, and our open source packages."
source: "https://docs.langchain.com/_llms/agent-development-lifecycle/deploy/get-started"
category: "docs"
tags: [docs, llms, agent-development-lifecycle, deploy, get-started]
---

# Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE Deploy Get started

> Documentation for LangSmith, Fleet, and our open source packages.

## Get started

- [LangSmith Deployment](../../../langsmith/deployment.md): Deploy and manage agents with durable execution, real-time streaming, and horizontal scaling.
- [Deploy your app to cloud](../../../langsmith/deployment-quickstart.md): Deploy your first application to LangSmith Cloud in GCP using the LangGraph CLI.

### Deployment components

- [LangSmith Deployment components](../../../langsmith/components.md): Overview of Agent Server, LangGraph CLI, Studio, SDKs, RemoteGraph, control plane, and data plane components.
- [LangSmith data plane](../../../langsmith/data-plane.md)
- [LangSmith control plane](../../../langsmith/control-plane.md)

### Develop & test

- [Local development & testing](../../../langsmith/local-dev-testing.md): Compare langgraph dev and langgraph up for local development and production-like testing of Agent Server applications.
- [Studio](../../../langsmith/studio-deploy.md): Develop, run, and debug agents in an interactive environment with LangSmith Studio.

### Frameworks and platforms

- [Deploy Google ADK agents](../../../langsmith/deploy-google-adk.md): Deploy Google Agent Development Kit (ADK) agents to LangSmith Agent Server using the deployments-wrap-sdk package.
- [Deploy other frameworks](../../../langsmith/deploy-other-frameworks.md): Deploy agents built with Claude Agent SDK, Strands, CrewAI, AutoGen, and other frameworks to LangSmith Deployment.

#### Full-stack web apps

- [Deploy full-stack web apps](../../../langsmith/deploy-frameworks-and-platforms.md): Deploy LangChain agents as full-stack web apps on Next.js, SvelteKit, Nuxt, Cloudflare Workers, Deno Deploy, and Vite with streaming UI and thread history.
- [Deploy with LangSmith and Vite](../../../langsmith/deploy-vite-langsmith.md): Deploy a LangChain deep agent to LangSmith Deployment and stream from a Vite React chat UI on Vercel, Netlify, or Cloudflare Pages.
- [Deploy with Next.js](../../../langsmith/deploy-nextjs.md): Deploy a LangChain deep agent in a Next.js App Router project with streaming chat, subagents, and thread history.
- [Deploy with SvelteKit](../../../langsmith/deploy-sveltekit.md): Deploy a LangChain deep agent in a SvelteKit project on Cloudflare Workers with streaming chat and thread history.
- [Deploy with Nuxt](../../../langsmith/deploy-nuxt.md): Deploy a LangChain deep agent in a Nuxt 4 app with Nitro server routes, Vue composables, and subagent-aware chat UI.
- [Deploy with Cloudflare Workers](../../../langsmith/deploy-cloudflare-workers.md): Deploy a LangChain deep agent on Cloudflare Workers with Vite, React, Hono, and Durable Objects for SSE replay.
- [Deploy with Deno Deploy](../../../langsmith/deploy-deno.md): Deploy a LangChain deep agent on Deno Deploy with Hono route handlers and a Vite React SPA served from one entrypoint.

### Reference

- [Reference](../../../langsmith/deploy-reference-overview.md): Reference for the LangSmith Deployment SDKs, CLI, and APIs for deploying and interacting with agents.
- [LangSmith Deployment SDK](../../../langsmith/smith-deployments-sdk.md)
- [LangGraph CLI](../../../langsmith/cli.md)
- [RemoteGraph](../../../langsmith/remote-graph.md)
- [Agent Server changelog](../../../langsmith/agent-server-changelog.md)

#### Agent Server API

- [Agent Server API reference for LangSmith Deployment](../../../langsmith/server-api-ref.md): Browse the Agent Server API reference for LangSmith Deployment, available within each deployment at the /docs endpoint.

##### Assistants

- [Create Assistant](../../../langsmith/agent-server-api/assistants/create-assistant.md): Create an assistant.
- [Search Assistants](../../../langsmith/agent-server-api/assistants/search-assistants.md): Search for assistants.
- [Count Assistants](../../../langsmith/agent-server-api/assistants/count-assistants.md): Get the count of assistants matching the specified criteria.
- [Get Assistant](../../../langsmith/agent-server-api/assistants/get-assistant.md): Get an assistant by ID.
- [Delete Assistant](../../../langsmith/agent-server-api/assistants/delete-assistant.md): Delete an assistant by ID.
- [Patch Assistant](../../../langsmith/agent-server-api/assistants/patch-assistant.md): Update an assistant.
- [Get Assistant Graph](../../../langsmith/agent-server-api/assistants/get-assistant-graph.md): Get an assistant by ID.
- [Get Assistant Subgraphs](../../../langsmith/agent-server-api/assistants/get-assistant-subgraphs.md): Get an assistant's subgraphs.
- [Get Assistant Subgraphs by Namespace](../../../langsmith/agent-server-api/assistants/get-assistant-subgraphs-by-namespace.md): Get an assistant's subgraphs filtered by namespace.
- [Get Assistant Schemas](../../../langsmith/agent-server-api/assistants/get-assistant-schemas.md): Get an assistant by ID.
- [Get Assistant Versions](../../../langsmith/agent-server-api/assistants/get-assistant-versions.md): Get all versions of an assistant.
- [Set Latest Assistant Version](../../../langsmith/agent-server-api/assistants/set-latest-assistant-version.md): Set the latest version for an assistant.

##### Threads

- [Create Thread](../../../langsmith/agent-server-api/threads/create-thread.md): Create a thread.
- [Search Threads](../../../langsmith/agent-server-api/threads/search-threads.md): Search for threads.
- [Count Threads](../../../langsmith/agent-server-api/threads/count-threads.md): Get the count of threads matching the specified criteria.
- [Prune Threads](../../../langsmith/agent-server-api/threads/prune-threads.md): Prune threads by ID. The 'delete' strategy removes threads entirely. The 'keep_latest' strategy prunes old checkpoints but keeps threads and their latest state.
- [Get Thread Storage](../../../langsmith/agent-server-api/threads/get-thread-storage.md): Bytes the thread's checkpoints occupy in the built-in checkpointer, as stored: checkpoints, channel values (per channel) and pending writes. Returns 501 when a custom checkpointer is configured.
- [Get Thread State](../../../langsmith/agent-server-api/threads/get-thread-state.md): Get state for a thread.
- [Update Thread State](../../../langsmith/agent-server-api/threads/update-thread-state.md): Add state to a thread.
- [Get Thread State At Checkpoint](../../../langsmith/agent-server-api/threads/get-thread-state-at-checkpoint.md): Get state for a thread at a specific checkpoint.
- [Get Thread State At Checkpoint](../../../langsmith/agent-server-api/threads/get-thread-state-at-checkpoint-1.md): Get state for a thread at a specific checkpoint.
- [Get Thread History](../../../langsmith/agent-server-api/threads/get-thread-history.md): Get all past states for a thread.
- [Get Thread History Post](../../../langsmith/agent-server-api/threads/get-thread-history-post.md): Get all past states for a thread.
- [Copy Thread](../../../langsmith/agent-server-api/threads/copy-thread.md): Create a new thread with a copy of the state and checkpoints from an existing thread.
- [Get Thread](../../../langsmith/agent-server-api/threads/get-thread.md): Get a thread by ID.
- [Delete Thread](../../../langsmith/agent-server-api/threads/delete-thread.md): Delete a thread by ID.
- [Patch Thread](../../../langsmith/agent-server-api/threads/patch-thread.md): Update a thread.
- [Join Thread Stream](../../../langsmith/agent-server-api/threads/join-thread-stream.md): This endpoint streams output in real-time from a thread. The stream will include the output of each run executed sequentially on the thread and will remain open indefinitely. It is the responsibility of the calling client to close the connection.

##### Streaming

- [Protocol v2 Event Stream (SSE)](../../../langsmith/agent-server-api/streaming/protocol-v2-event-stream-sse.md): Open a connection-scoped SSE event stream for a thread. The request body is a `ProtocolEventStreamRequest` carrying channel and namespace filters; the server replies with `Content-Type: text/event-stream` and pushes matching `ProtocolEvent` frames for the lifetime of the connection. Closing the conn…
- [Protocol v2 Command](../../../langsmith/agent-server-api/streaming/protocol-v2-command.md): Send a single protocol command scoped to a thread. The request body is a `ProtocolCommand` envelope with a `method` (e.g. `run.start`, `input.respond`, `agent.getTree`) and method-specific `params`. The response is either a `ProtocolSuccess` (with method-specific `result`) or a `ProtocolError`.

##### Thread Runs

- [List Runs](../../../langsmith/agent-server-api/thread-runs/list-runs.md): List runs for a thread.
- [Create Background Run](../../../langsmith/agent-server-api/thread-runs/create-background-run.md): Create a run in existing thread, return the run ID immediately. Don't wait for the final run output.
- [Create Run, Stream Output](../../../langsmith/agent-server-api/thread-runs/create-run-stream-output.md): Create a run in existing thread. Stream the output.
- [Create Run, Wait for Output](../../../langsmith/agent-server-api/thread-runs/create-run-wait-for-output.md): Create a run in existing thread. Wait for the final output and then return it.
- [Get Run](../../../langsmith/agent-server-api/thread-runs/get-run.md): Get a run by ID.
- [Delete Run](../../../langsmith/agent-server-api/thread-runs/delete-run.md): Delete a run by ID.
- [Join Run](../../../langsmith/agent-server-api/thread-runs/join-run.md): Wait for a run to finish.
- [Join Run Stream](../../../langsmith/agent-server-api/thread-runs/join-run-stream.md): Join a run stream. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. If the run has been created with `stream_resumable=true`, the stream can be resumed from the last seen event ID.
- [Cancel Run](../../../langsmith/agent-server-api/thread-runs/cancel-run.md)
- [Cancel Runs](../../../langsmith/agent-server-api/thread-runs/cancel-runs.md): Cancel one or more runs. Can cancel runs by thread ID and run IDs, or by status filter.

##### Crons

- [Create Thread Cron](../../../langsmith/agent-server-api/crons/create-thread-cron.md): Create a cron to schedule runs on a thread.
- [Create Cron](../../../langsmith/agent-server-api/crons/create-cron.md): Create a cron to schedule runs on new threads.
- [Search Crons](../../../langsmith/agent-server-api/crons/search-crons.md): Search all active crons
- [Count Crons](../../../langsmith/agent-server-api/crons/count-crons.md): Get the count of crons matching the specified criteria.
- [Get Cron](../../../langsmith/agent-server-api/crons/get-cron.md): Get a cron by ID.
- [Delete Cron](../../../langsmith/agent-server-api/crons/delete-cron.md): Delete a cron by ID.
- [Update Cron](../../../langsmith/agent-server-api/crons/update-cron.md): Update a cron job by ID.

##### Stateless Runs

- [Create Run, Stream Output](../../../langsmith/agent-server-api/stateless-runs/create-run-stream-output.md): Create a run and stream the output.
- [Create Run, Wait for Output](../../../langsmith/agent-server-api/stateless-runs/create-run-wait-for-output.md): Create a run, wait for the final output and then return it.
- [Create Background Run](../../../langsmith/agent-server-api/stateless-runs/create-background-run.md): Create a run and return the run ID immediately. Don't wait for the final run output.
- [Create Run Batch](../../../langsmith/agent-server-api/stateless-runs/create-run-batch.md): Create a batch of runs and return immediately.

##### Store

- [Retrieve a single item.](../../../langsmith/agent-server-api/store/retrieve-a-single-item.md)
- [Store or update an item.](../../../langsmith/agent-server-api/store/store-or-update-an-item.md)
- [Delete an item.](../../../langsmith/agent-server-api/store/delete-an-item.md)
- [Search or list items within a namespace prefix.](../../../langsmith/agent-server-api/store/search-or-list-items-within-a-namespace-prefix.md): Lists items ordered by last updated time. If a `query` is provided, performs a natural language search instead. Supports pagination via `limit` and `offset`, and filtering via `filter`.
- [List namespaces with optional match conditions.](../../../langsmith/agent-server-api/store/list-namespaces-with-optional-match-conditions.md)

##### A2A

- [A2A JSON-RPC](../../../langsmith/agent-server-api/a2a/a2a-json-rpc.md): Communicate with an assistant using the Agent-to-Agent (A2A) Protocol over JSON-RPC 2.0. This endpoint accepts a JSON-RPC envelope and dispatches based on `method`.

##### MCP

- [MCP Get](../../../langsmith/agent-server-api/mcp/mcp-get.md): Implemented according to the Streamable HTTP Transport specification.
- [MCP Post](../../../langsmith/agent-server-api/mcp/mcp-post.md): Implemented according to the Streamable HTTP Transport specification. Sends a JSON-RPC 2.0 message to the server.
- [Terminate Session](../../../langsmith/agent-server-api/mcp/terminate-session.md): Implemented according to the Streamable HTTP Transport specification. Terminate an MCP session. The server implementation is stateless, so this is a no-op.

##### System

- [Server Information](../../../langsmith/agent-server-api/system/server-information.md): Get server version information, feature flags, and metadata.
- [System Metrics](../../../langsmith/agent-server-api/system/system-metrics.md): Get system metrics in Prometheus or JSON format for monitoring and observability.
- [API Documentation](../../../langsmith/agent-server-api/system/api-documentation.md): A local reference to the Agent Server API documentation.
- [Health Check](../../../langsmith/agent-server-api/system/health-check.md): Check the health status of the server. Optionally check database connectivity.

#### Control Plane API

- [Control plane API reference for LangSmith Deployment](../../../langsmith/api-ref-control-plane.md): Use the control plane API to programmatically create, manage, and automate Agent Server deployments in LangSmith Deployment.

##### Integrations (v1)

- [List GitHub Integrations](../../../api-reference/integrations-v1/list-github-integrations.md): List available GitHub integrations for LangGraph Platfom Cloud SaaS.
- [List GitHub Repositories](../../../api-reference/integrations-v1/list-github-repositories.md): List available GitHub repositories for an integration that are available to deploy to LangSmith Deployment.
- [List Forge GitHub Integrations](../../../api-reference/integrations-v1/list-forge-github-integrations.md): List available Forge GitHub integrations.
- [List Forge GitHub Repositories](../../../api-reference/integrations-v1/list-forge-github-repositories.md): List available GitHub repositories for a Forge integration.

##### Deployments (v2)

- [List Deployments](../../../api-reference/deployments-v2/list-deployments.md): List all deployments.
- [Create Deployment](../../../api-reference/deployments-v2/create-deployment.md): Create a new deployment.
- [Delete Deployments](../../../api-reference/deployments-v2/delete-deployments.md): Delete multiple deployments with partial success support.
- [Get Free Deployment Count](../../../api-reference/deployments-v2/get-free-deployment-count.md): Return the number of free deployments used by the caller's organization.
- [Get Deployment](../../../api-reference/deployments-v2/get-deployment.md): Get a deployment by ID.
- [Delete Deployment](../../../api-reference/deployments-v2/delete-deployment.md): Delete a deployment by ID.
- [Patch Deployment](../../../api-reference/deployments-v2/patch-deployment.md): Patch a deployment by ID.
- [Patch Deployment Tier](../../../api-reference/deployments-v2/patch-deployment-tier.md): Patch a deployment's fixed resource tier.
- [Patch Deployment Resource Tiers](../../../api-reference/deployments-v2/patch-deployment-resource-tiers.md): Patch a deployment's compute and database resource tiers independently.
- [List Revisions](../../../api-reference/deployments-v2/list-revisions.md): List all revisions for a deployment.
- [Create Deployment Revision](../../../api-reference/deployments-v2/create-deployment-revision.md): Create a new revision for a deployment.
- [Get Revision](../../../api-reference/deployments-v2/get-revision.md): Get a revision by ID for a deployment.
- [Redeploy Revision](../../../api-reference/deployments-v2/redeploy-revision.md): Redeploy a specific revision ID.
- [List Deployment Logs](../../../api-reference/deployments-v2/list-deployment-logs.md): List deploy logs for a deployment (across all revisions).
- [List Revision Logs](../../../api-reference/deployments-v2/list-revision-logs.md): List build or deploy logs for a specific revision of a deployment.
- [Interrupt Deployment Revision](../../../api-reference/deployments-v2/interrupt-deployment-revision.md): Interrupt an in-progress revision build/deploy.
- [List Deployment Log Entries](../../../api-reference/deployments-v2/list-deployment-log-entries.md): List build or deploy log entries for a deployment.

##### Listeners (v2)

- [List Listeners](../../../api-reference/listeners-v2/list-listeners.md): List all listeners.
- [Create Listener](../../../api-reference/listeners-v2/create-listener.md): Create a listener.<br> <br> Creating a listener is only allowed for LangSmith organizations with self-hosted enterprise plans.
- [Get Listener](../../../api-reference/listeners-v2/get-listener.md): Get a listener by ID.
- [Delete Listener](../../../api-reference/listeners-v2/delete-listener.md): Delete a listener by ID.
- [Patch Listener](../../../api-reference/listeners-v2/patch-listener.md): Patch a listener by ID.

##### Integrations (v2)

- [List Github Installations](../../../api-reference/integrations-v2/list-github-installations.md): List GitHub App installations available to the workspace.
- [List Github Installation Repositories](../../../api-reference/integrations-v2/list-github-installation-repositories.md): List repositories available through a GitHub App installation.
- [Get Github Install Link Endpoint](../../../api-reference/integrations-v2/get-github-install-link-endpoint.md): Create a GitHub App installation link.
- [List Forge Github Installations](../../../api-reference/integrations-v2/list-forge-github-installations.md): List Forge GitHub App installations available to the workspace.
- [List Forge Github Installation Repositories](../../../api-reference/integrations-v2/list-forge-github-installation-repositories.md): List repositories available through a Forge GitHub App installation.
- [Get Forge Github Install Link Endpoint](../../../api-reference/integrations-v2/get-forge-github-install-link-endpoint.md): Create a Forge GitHub App installation link.
- [Get Engine Picker Session Endpoint](../../../api-reference/integrations-v2/get-engine-picker-session-endpoint.md): Get a Forge GitHub App installation picker session.
- [Create Engine Picker Session Selection](../../../api-reference/integrations-v2/create-engine-picker-session-selection.md): Select an installation or begin a new GitHub App installation.

##### Auth Service (v2)

- [List Oauth Providers](../../../api-reference/auth-service-v2/list-oauth-providers.md): List OAuth providers.
- [Create Oauth Provider](../../../api-reference/auth-service-v2/create-oauth-provider.md): Create a new OAuth provider manually.
- [List Platform Oauth Providers](../../../api-reference/auth-service-v2/list-platform-oauth-providers.md): List platform-level OAuth providers available to all workspaces.
- [Get Platform Oauth Provider](../../../api-reference/auth-service-v2/get-platform-oauth-provider.md): Get a platform-level OAuth provider available to all workspaces.
- [Oauth Setup Callback](../../../api-reference/auth-service-v2/oauth-setup-callback.md): Handle OAuth setup callback redirect from GitHub Apps.
- [Oauth Callback Get](../../../api-reference/auth-service-v2/oauth-callback-get.md): Handle OAuth callback redirect from OAuth providers.
- [Oauth Callback](../../../api-reference/auth-service-v2/oauth-callback.md): Finalize an OAuth flow.
- [Authenticate](../../../api-reference/auth-service-v2/authenticate.md): Get OAuth token or start authentication flow if needed.
- [Wait For Auth Completion](../../../api-reference/auth-service-v2/wait-for-auth-completion.md): Wait for OAuth authentication completion.
- [Create Mcp Oauth Provider](../../../api-reference/auth-service-v2/create-mcp-oauth-provider.md): Create an OAuth provider via MCP auto-discovery.
- [Get Oauth Provider](../../../api-reference/auth-service-v2/get-oauth-provider.md): Get a specific OAuth provider.
- [Delete Oauth Provider](../../../api-reference/auth-service-v2/delete-oauth-provider.md): Delete an OAuth provider.
- [Update Oauth Provider](../../../api-reference/auth-service-v2/update-oauth-provider.md): Update an OAuth provider.
- [List Oauth Tokens For User](../../../api-reference/auth-service-v2/list-oauth-tokens-for-user.md): List the calling user's tokens for a provider.
- [Delete Oauth Tokens For User](../../../api-reference/auth-service-v2/delete-oauth-tokens-for-user.md): Delete all tokens for the current user for the given provider (across agents).
- [List Token Events For User](../../../api-reference/auth-service-v2/list-token-events-for-user.md): List the calling user's OAuth connection audit events, newest first.
- [Update Token Label](../../../api-reference/auth-service-v2/update-token-label.md): Update a token's provider_account_label. Only the token owner can update.
- [Import Oauth Token](../../../api-reference/auth-service-v2/import-oauth-token.md): Persist a directly-obtained OAuth token (no authorization-code exchange).
- [Delete Single Oauth Token](../../../api-reference/auth-service-v2/delete-single-oauth-token.md): Delete a specific OAuth token, revoking it at the provider first.
- [Check Oauth Token Exists](../../../api-reference/auth-service-v2/check-oauth-token-exists.md): Return whether the current user has any tokens for a given provider (across agents).
- [Check Oauth Tokens Exist Batch](../../../api-reference/auth-service-v2/check-oauth-tokens-exist-batch.md): Batch token-presence check: per requested provider, whether the current user has any token.
- [Check Workspace Slack Tokens Exist](../../../api-reference/auth-service-v2/check-workspace-slack-tokens-exist.md): Check if the workspace has any Slack tokens.
- [Revoke All Slack Tokens For Workspace](../../../api-reference/auth-service-v2/revoke-all-slack-tokens-for-workspace.md): Revoke ALL Slack tokens for the workspace. Admin-only action that disconnects Slack entirely.

##### Agent Connections (v2)

- [List Connections](../../../api-reference/agent-connections-v2/list-connections.md)
- [Create Connection](../../../api-reference/agent-connections-v2/create-connection.md)
- [Remove Connection](../../../api-reference/agent-connections-v2/remove-connection.md)
- [Upsert Agent Provider Token](../../../api-reference/agent-connections-v2/upsert-agent-provider-token.md): Import an OAuth token and bind it to the agent for the given provider.

#### Related

- [LangGraph Python SDK](../../../langsmith/langgraph-python-sdk.md)
- [LangGraph JS/TS SDK](../../../langsmith/langgraph-js-ts-sdk.md)

## OpenAPI Specs

- [agent-server-openapi](https://docs.langchain.com/langsmith/agent-server-openapi.json)
- [openapi](https://api.host.langchain.com/openapi.json)
