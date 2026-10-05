---
title: "Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE Monitor"
description: "Documentation for LangSmith, Fleet, and our open source packages."
source: "https://docs.langchain.com/_llms/agent-development-lifecycle/monitor"
category: "docs"
tags: [docs, llms, agent-development-lifecycle, monitor]
---

# Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE Monitor

> Documentation for LangSmith, Fleet, and our open source packages.

## Monitor

- [AGENT DEVELOPMENT LIFECYCLE / Monitor / Reference (569 pages)](monitor/reference.md): Documentation for AGENT DEVELOPMENT LIFECYCLE / Monitor / Reference.

### Overview

- [LangSmith Observability](../../langsmith/observability.md): Instrument your LLM application, investigate traces, and monitor performance in production with LangSmith.

### Trace

- [Tracing quickstart](../../langsmith/observability-quickstart.md): Add LangSmith tracing to an LLM application in minutes.
- [Trace an LLM application tutorial](../../langsmith/observability-llm-tutorial.md): Add LangSmith observability to an LLM application across prototyping, beta testing, and production.
- [Observability concepts](../../langsmith/observability-concepts.md): How LangSmith structures observability data as runs, traces, threads, and trajectories, and how to send traces.
- [LangSmith Chat](../../langsmith/chat-observability.md): Use Chat to analyze traces and runs.

#### Tracing setup

##### Integrations

- [Integrations](../../langsmith/integrations.md)

###### LLM providers

- [Trace Anthropic applications](../../langsmith/trace-anthropic.md)
- [Trace Amazon Bedrock applications](../../langsmith/trace-bedrock.md)
- [Trace DeepSeek applications](../../langsmith/trace-deepseek.md)
- [Trace Google Gemini applications](../../langsmith/trace-with-google-gemini.md)
- [Trace LiteLLM applications](../../langsmith/trace-litellm.md)
- [Trace Mistral applications](../../langsmith/trace-with-mistral.md)
- [Trace OpenAI applications](../../langsmith/trace-openai.md)
- [Trace OpenAI-compatible providers](../../langsmith/trace-with-openai-compatible.md): Trace LLM calls from any OpenAI-compatible provider to LangSmith.

###### Agent frameworks

- [Trace AutoGen applications](../../langsmith/trace-with-autogen.md)
- [Trace Claude Agent SDK applications](../../langsmith/trace-claude-agent-sdk.md)
- [Trace Claude Managed Agents](../../langsmith/trace-with-claude-managed-agents.md): Automatically trace Claude Managed Agent sessions and events with LangSmith.
- [Trace CrewAI applications](../../langsmith/trace-with-crewai.md)
- [Trace Deep Agents applications](../../langsmith/trace-deep-agents.md)
- [Trace Google ADK applications](../../langsmith/trace-with-google-adk.md)
- [Trace LangChain applications (Python and JS/TS)](../../langsmith/trace-with-langchain.md)
- [Trace LangGraph applications](../../langsmith/trace-with-langgraph.md)
- [Trace Mastra applications](../../langsmith/trace-with-mastra.md)
- [Trace Microsoft Agent Framework applications](../../langsmith/trace-with-microsoft-agent-framework.md)
- [Trace OpenAI Agents SDK applications](../../langsmith/trace-with-openai-agents-sdk.md): Trace OpenAI Agents SDK Python and JavaScript applications with LangSmith.
- [Trace with OpenTelemetry](../../langsmith/trace-with-opentelemetry.md): Configure OpenTelemetry tracing in LangSmith, including LANGSMITH_OTEL_ENABLED and OTEL fanout with the OpenTelemetry Collector.
- [Trace PydanticAI applications](../../langsmith/trace-with-pydantic-ai.md)
- [Trace Semantic Kernel applications](../../langsmith/trace-with-semantic-kernel.md)
- [Trace Strands Agents applications](../../langsmith/trace-with-strands-agents.md): Trace Strands Agents applications with LangSmith.
- [Trace Vercel AI SDK applications (JS/TS only)](../../langsmith/trace-with-vercel-ai-sdk.md): Trace Vercel AI SDK applications with LangSmith for AI SDK v5, v6, and v7.

###### Voice AI frameworks

- [Voice tracing fundamentals](../../langsmith/trace-voice-fundamentals.md): Best practices for tracing voice and audio agents in LangSmith, including conversation audio, single-trace conversations, and the audio modality flag.
- [Trace OpenAI Realtime applications](../../langsmith/trace-openai-realtime.md): Trace OpenAI Realtime voice agents in LangSmith using the LangSmith SDK.
- [Trace Gemini Live applications](../../langsmith/trace-gemini-live.md): Trace Gemini Live voice agents in LangSmith using the LangSmith SDK.
- [Trace LiveKit applications](../../langsmith/trace-with-livekit.md)
- [Trace Pipecat applications](../../langsmith/trace-with-pipecat.md)

###### Developer tools

- [Coding agent metadata contract](../../langsmith/coding-agent-metadata-contract.md): The metadata schema that standardizes what trace metadata coding agents must emit when sending runs to LangSmith.
- [Trace Claude Code applications](../../langsmith/trace-claude-code.md)
- [Trace OpenAI Codex sessions](../../langsmith/trace-with-codex.md): Capture OpenAI Codex agent turns, tool calls, model metadata, and subagent threads in LangSmith.
- [Trace OpenCode sessions](../../langsmith/trace-with-opencode.md): Capture OpenCode sessions, assistant turns, tool calls, and subagent activity in LangSmith.
- [Trace Cursor sessions](../../langsmith/trace-with-cursor.md): Capture Cursor agent turns, tool calls, model metadata, token usage, attachments, and subagents in LangSmith.
- [Trace Pi coding agent sessions](../../langsmith/trace-with-pi.md): Trace Pi coding agent invocations to LangSmith to observe turns, debug tool calls, track token usage, and inspect individual LLM invocations.
- [Trace Instructor applications](../../langsmith/trace-with-instructor.md)
- [Trace n8n workflows](../../langsmith/trace-with-n8n.md): Learn how to trace n8n AI workflows in LangSmith.
- [Trace with Temporal](../../langsmith/trace-with-temporal.md): Learn how to trace Temporal workflows and activities in LangSmith using OpenTelemetry.
- [Trace Visual Studio Code Copilot Chat sessions](../../langsmith/trace-with-vscode-copilot.md): Capture VS Code Copilot Chat agent interactions, LLM calls, tool executions, and token usage in LangSmith via OpenTelemetry.

##### Manual instrumentation

- [Custom instrumentation](../../langsmith/annotate-code.md): Instrument your code directly to control which functions are traced and how they appear in LangSmith.
- [Trace with API](../../langsmith/trace-with-api.md): Learn how to trace LLM applications using the LangSmith REST API directly.
- [Log LLM calls](../../langsmith/log-llm-trace.md)
- [Log retriever traces](../../langsmith/log-retriever-trace.md): Log retrieval steps in LangSmith traces for document-level visibility into your RAG pipeline.
- [Metadata parameters reference](../../langsmith/ls-metadata-parameters.md)
- [Upload files with traces](../../langsmith/upload-files-with-traces.md)

#### Configuration & troubleshooting

- [Cost tracking](../../langsmith/cost-tracking.md)
- [Usage and billing](../../langsmith/usage-and-billing.md): Understand LangSmith trace data retention tiers, pricing, rate limits, and usage limits.

##### Project & environment settings

- [Log traces to a specific project](../../langsmith/log-traces-to-project.md): Route LangSmith traces to a named project instead of the default project using environment variables or the SDK.
- [Log traces to an agent](../../langsmith/log-traces-to-agent.md): How agent addressing sends traces to an agent and an environment, which variables carry it, and why it cannot be combined with project addressing.
- [Write traces to multiple destinations with replicas](../../langsmith/trace-replicas.md): Send every trace to multiple projects or workspaces at the same time using replicas, configured by environment variable or at runtime.
- [Trace without setting environment variables](../../langsmith/trace-without-env-vars.md)
- [Conditional tracing](../../langsmith/conditional-tracing.md)
- [Set a sampling rate for traces](../../langsmith/sample-traces.md)

##### Advanced tracing techniques

- [Implement distributed tracing](../../langsmith/distributed-tracing.md)
- [Access the current run (span) within a traced function](../../langsmith/access-current-span.md)
- [Trace JS functions in serverless environments](../../langsmith/serverless-environments.md)
- [Log multimodal traces](../../langsmith/log-multimodal-traces.md)
- [Trace generator functions](../../langsmith/trace-generator-functions.md)

##### Data & privacy

- [Add metadata and tags to traces](../../langsmith/add-metadata-tags.md)
- [Prevent logging of sensitive data in traces](../../langsmith/mask-inputs-outputs.md)
- [Redact secrets from traces](../../langsmith/redact-secrets.md): Prevent API keys, tokens, and other secrets from appearing in LangSmith traces using the SDK anonymizer.
- [Redact sensitive data with the OpenTelemetry Gateway architecture](../../langsmith/otel-gateway-trace-redaction.md): Use an OpenTelemetry collector to redact sensitive data from traces before they land in LangSmith.

##### Troubleshooting guides

- [Troubleshoot trace nesting](../../langsmith/nest-traces.md)
- [Troubleshoot variable caching](../../langsmith/troubleshooting-variable-caching.md)

### Debug

- [Configure threads](../../langsmith/threads.md)

#### Viewing & managing traces

- [View traces](../../langsmith/view-traces.md): Inspect agent threads in LangSmith using the Trajectory view or Details view.
- [Filter traces](../../langsmith/filter-traces.md): Find specific threads, traces, and runs in a LangSmith tracing project by writing filter queries in the search bar.
- [Filter traces (ClickHouse)](../../langsmith/filter-traces-in-application.md): Filter threads, traces, and runs in a LangSmith tracing project backed by ClickHouse, using the filter bar, filter shortcuts, and saved filters.
- [Configure run input and output preview](../../langsmith/configure-input-output-preview.md): Customize what appears in the Input and Output columns of the Runs table by configuring custom preview paths for specific trace types.
- [Manage a trace](../../langsmith/manage-trace.md): Share traces publicly, and view server logs from the Details view in LangSmith.
- [Query traces using the SDK](../../langsmith/export-traces.md)
- [Trace query syntax](../../langsmith/trace-query-syntax.md)
- [Query threads using the SDK](../../langsmith/query-threads.md): Programmatically fetch and inspect multi-turn conversation threads from your LangSmith projects.
- [LangSmith Remote MCP](../../langsmith/langsmith-remote-mcp.md): Connect MCP-compatible clients to LangSmith over OAuth, or authenticate programmatic clients with a LangSmith API key.
- [LangSmith MCP Server](../../langsmith/langsmith-mcp-server.md): Use the Model Context Protocol (MCP) server to let language models fetch conversation history, prompts, runs, datasets, experiments, and billing from LangSmith.

#### Bulk export trace data

- [Bulk export trace data](../../langsmith/data-export.md): Export LangSmith trace data to an S3-compatible bucket in Parquet format.
- [Manage bulk export destinations](../../langsmith/data-export-destinations.md): Configure and manage S3-compatible export destinations for LangSmith bulk exports.
- [Monitor and troubleshoot bulk exports](../../langsmith/data-export-monitor.md): Monitor bulk export status, manage running exports, and troubleshoot failures.
- [Import exported data](../../langsmith/data-export-downstream.md): Import LangSmith bulk-exported Parquet data into BigQuery, Snowflake, Redshift, Clickhouse, or DuckDB.
- [Export trace data to BigQuery](../../langsmith/big-query-bulk-export.md): Load LangSmith trace data into BigQuery using bulk export to GCS.

#### Trajectory view

- [Trajectory view integrations](../../langsmith/trajectory-view-integrations.md): Frameworks and SDKs that render in the LangSmith Trajectory view and the metadata each one sets.

#### Data type reference

- [Run (span) data format](../../langsmith/run-data-format.md)
- [Feedback data format](../../langsmith/feedback-data-format.md)

### Observe

#### Monitoring & alerting

- [Monitor projects with dashboards](../../langsmith/dashboards.md)
- [Alerts in LangSmith](../../langsmith/alerts.md)
- [Discover errors and usage patterns with Insights](../../langsmith/insights.md): Use LangSmith Insights to automatically analyze traces, detect usage patterns, identify common agent behaviors, and surface failure modes without manual trace review.
- [Custom Apps](../../langsmith/custom-apps.md): Build custom UIs that run inside LangSmith and call the LangSmith API, either by chatting with LangSmith Chat or locally with the LangSmith CLI.

#### Online evaluators

- [Set up LLM-as-a-judge online evaluators](../../langsmith/online-evaluations-llm-as-judge.md)
- [Set up decision model online evaluators](../../langsmith/online-evaluations-decision-models.md): Evaluate production traces in LangSmith with SemIf or Jev as the judge, and record each question's typed answer as its own feedback key.
- [Set up multi-turn online evaluators](../../langsmith/online-evaluations-multi-turn.md)
- [Set up LangChain Tuned Evaluators](../../langsmith/tuned-evaluators.md): Use specialized LangChain-managed judges to attach quality feedback to traces.
- [Set up online code evaluators](../../langsmith/online-evaluations-code.md)
- [Set up composite online evaluators](../../langsmith/online-evaluations-composite.md)

#### Automations

- [Set up automation rules](../../langsmith/rules.md)
- [Configure webhook notifications for rules](../../langsmith/webhooks.md): Configure webhook notifications to receive POST requests when automation rules match new runs or threads in LangSmith.

## OpenAPI Specs

- [langsmith-platform-openapi](https://docs.langchain.com/langsmith/langsmith-platform-openapi.json)
