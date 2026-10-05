---
title: "Docs by LangChain: PRODUCTS AND SETUP"
description: "Documentation for LangSmith, Fleet, and our open source packages."
source: "https://docs.langchain.com/_llms/products-and-setup"
category: "docs"
tags: [docs, llms, products-and-setup]
---

# Docs by LangChain: PRODUCTS AND SETUP

> Documentation for LangSmith, Fleet, and our open source packages.

## PRODUCTS AND SETUP

- [PRODUCTS AND SETUP / LangSmith setup (132 pages)](products-and-setup/lang-smith-setup.md): Hosting and administration

### LLM Gateway

- [LLM Gateway](../langsmith/llm-gateway.md): Access models across providers with one LangSmith API key while tracing calls and enforcing spend and data-protection policies.
- [LLM Gateway quickstart](../langsmith/llm-gateway-quickstart.md): Call models across providers with one LangSmith API key, then view the trace and set a spend limit.
- [How the gateway works](../langsmith/llm-gateway-how-it-works.md): Understand what the LLM Gateway does to each request, how upstream credentials are resolved, and where the gateway is available.
- [API formats](../langsmith/llm-gateway-api-formats.md): Use OpenAI Chat Completions, Anthropic Messages, or OpenAI Responses requests to call models across providers through the LLM Gateway.

#### Core capabilities

- [Set up coding agents](../langsmith/llm-gateway-coding-agents.md): Configure Claude Code, Codex, Gemini CLI, and Deep Agents Code to route LLM calls through the LLM Gateway.
- [Gateway Credits](../langsmith/llm-gateway-credits.md): Use Gateway Credits to access models without a provider key, just authenticate with LangSmith.
- [Decision models](../langsmith/llm-gateway-decision-models.md): Use SemIf through the LangSmith LLM Gateway for structured classification and scoring with the System One API.
- [Model fallbacks](../langsmith/llm-gateway-fallbacks.md): Automatically retry a request against backup models when the primary model rate-limits, errors, or returns another configured status code.

#### Administration and governance

- [Admin setup](../langsmith/llm-gateway-admin-setup.md): One-time organization setup to enable the LLM Gateway and grant user access.
- [Traces and access control](../langsmith/llm-gateway-access.md): Understand where gateway traces land and who can see and configure what.
- [Monitor LLM Gateway spend](../langsmith/llm-gateway-monitoring.md): View and analyze LLM Gateway costs by user, API key, and model.
- [Spend policies](../langsmith/llm-gateway-spend-policies.md): Set cost limits on LLM usage across your organization and prevent runaway spend before it reaches providers.
- [Rate limit policies](../langsmith/llm-gateway-rate-limit-policies.md): Limit the number of requests or tokens a user, workspace, or API key can send through the LLM Gateway in a rolling time window.
- [Model access policies](../langsmith/llm-gateway-model-access-policies.md): Control which model providers and models are accessible through the LLM Gateway for your organization, workspaces, users, or API keys.
- [Per-customer policies](../langsmith/llm-gateway-header-policies.md): Split gateway spend caps and rate limits by a custom request header so each of your end customers gets its own limit under a single API key.
- [Data policy](../langsmith/llm-gateway-data-policy.md): Create data policies that redact sensitive data and control trace content in the LLM Gateway.

#### Advanced

- [Direct model access](../langsmith/llm-gateway-direct-model-access.md): Access provider APIs directly through provider-specific LLM Gateway paths without using the gateway standardization layer.

### No-code agents

- [No-code agents with LangSmith Fleet](../langsmith/fleet/index.md): Create helpful AI agents without code. Start from a template, connect your accounts, and let the agent handle routine work while you stay in control.

#### Get started

- [Quickstart](../langsmith/fleet/quickstart.md): Build an agent from a template
- [Essentials](../langsmith/fleet/essentials.md): Fleet's core features
- [Templates](../langsmith/fleet/templates.md): Start faster with curated Fleet templates and customize tools, prompts, and channels.
- [Agent platform comparison](../langsmith/fleet/comparison.md): Compare LangSmith Fleet with Claude Cowork, Amazon Quick, Google Workspace Studio, and Microsoft Copilot to choose the right enterprise agent platform for your team

#### Configure

- [Manage workspace administration](../langsmith/fleet/workspace-admin.md): Configure workspace-level settings for Fleet.
- [Agent identity](../langsmith/fleet/agent-identity.md): Choose whether your Fleet agent authenticates with its own credentials or with each user's credentials.
- [Manage agent settings](../langsmith/fleet/manage-agent-settings.md): Manage your agents in Fleet.
- [Computer use](../langsmith/fleet/computer-use.md): Run code, manage files, and call authenticated APIs from a persistent virtual computer attached to your Fleet agent.

#### Tools and automation

- [Tool integrations](../langsmith/fleet/tools.md): Give your agents access to a wide range of tools and services.
- [Channels](../langsmith/fleet/channels.md): Configure channels to trigger your Fleet agents automatically.
- [Schedules](../langsmith/fleet/schedules.md): Configure schedules to run your Fleet agents on a recurring basis.
- [Skills](../langsmith/fleet/skills.md): Use skills to give your agents access to specific capabilities.
- [Integrate Slack with an agent](../langsmith/fleet/slack-app.md): Connect LangSmith Fleet to your Slack workspace so your agents work as Slack bots your team can tag directly.
- [Integrate Teams with an agent](../langsmith/fleet/teams-app.md): Connect LangSmith Fleet to Microsoft Teams by bringing your own Azure Bot to let agents communicate with users in Teams.
- [Remote MCP servers](../langsmith/fleet/remote-mcp-servers.md): Connect Fleet to popular remote MCP servers
- [Arcade integration](../langsmith/fleet/arcade.md): Connect your workspace to Arcade to give agents access to third-party tools like GitHub, Gmail, Slack, and more.
- [Salesforce integration](../langsmith/fleet/salesforce.md): Connect LangSmith Fleet to Salesforce so your agents can query records, navigate schemas, and read custom fields.

#### Advanced

- [Use Fleet agents in code](../langsmith/fleet/code.md): Invoke Fleet agents via the LangGraph SDK or REST API, or download and run them locally with the fleet-deepagents-export package.
- [LangSmith Tool Server](../langsmith/fleet/mcp-framework.md)
- [Fleet webhooks](../langsmith/fleet/webhooks.md): Integrate agent publishing with external systems, CI/CD pipelines, or custom deployment workflows.
- [Auth-aware tool responses](../langsmith/fleet/auth-format.md): Format tool responses to trigger OAuth flows and resume execution automatically.

#### Additional resources

- [Access & oversight](../langsmith/fleet/access-and-oversight.md): Control who can access agents, how they authenticate, and audit everything they do.
- [Self-hosted](../langsmith/fleet/self-hosted-link.md)
- [LangSmith Fleet changelog](../langsmith/fleet/changelog.md): Weekly updates to LangSmith Fleet

### Engine

- [LangSmith Engine](../langsmith/engine-overview.md): LangSmith Engine is the agent for agent engineering, turning production traces into tracked issues, fixes, and datasets across the development lifecycle.
- [Find and fix your agent's issues with LangSmith Engine](../langsmith/engine.md): Automatically detect and resolve recurring issues in your tracing project using LangSmith Engine.
- [Connect LangSmith Engine to GitHub](../langsmith/engine-github.md): Connect LangSmith Engine to GitHub in LangSmith Cloud, or create and configure your own GitHub App for a self-hosted deployment.
- [LangSmith Engine notifications](../langsmith/engine-notifications.md): Send LangSmith Engine notifications to Slack, Jira Automation, and webhook endpoints.
- [LangSmith Engine security](../langsmith/engine-security.md): How LangSmith Engine handles your data, the GitHub and model subprocessor controls that govern its access, and its compliance posture.
- [LangSmith Engine on Self-hosted](../langsmith/engine-self-hosted.md): Set up LangSmith Engine on a self-hosted LangSmith instance, including model provider options and external network requirements.

### Deep Agents Code

- [Deep Agents Code](../deepagents/code/overview.md): Terminal coding agent built on the Deep Agents SDK
- [Quickstart](../deepagents/code/quickstart.md): Install Deep Agents Code, run your first task, and use interactive or non-interactive modes
- [Command reference](../deepagents/code/cli-reference.md): Deep Agents Code command-line flags and management subcommands
- [Approval modes](../deepagents/code/approval-modes.md): Choose how Deep Agents Code reviews gated tool calls with Manual, Auto, and YOLO modes
- [Goals and rubrics](../deepagents/code/goals-and-rubrics.md): Define objectives and acceptance criteria for Deep Agents Code sessions
- [Plugins and marketplaces](../deepagents/code/plugins.md): Install plugins from marketplaces or package skills, MCP servers, hooks, and Python extensions for dcode
- [Python extensions](../deepagents/code/extensions.md): Customize dcode with Python tools, middleware, and storage routes
- [Memory and Skills](../deepagents/code/memory-and-skills.md): Persistent memory, AGENTS.md files, and reusable skills for Deep Agents Code, including creation, discovery, and invocation.
- [Use remote sandboxes](../deepagents/code/remote-sandboxes.md): Run Deep Agents Code tool execution in LangSmith, AgentCore, Daytona, Modal, Runloop, Vercel, or E2B sandboxes. Install provider dependencies, set credentials, and use flags and setup scripts.
- [Use subagents in Deep Agents Code](../deepagents/code/subagents.md): Define custom Deep Agents Code subagents as AGENTS.md files with YAML frontmatter. Covers project and user paths, optional model overrides, and examples.
- [Model providers](../deepagents/code/providers.md): Configure any LangChain-compatible model provider for Deep Agents Code
- [Changelog](../deepagents/code/changelog.md)

#### Configuration

- [Configuration](../deepagents/code/configuration.md): Configure Deep Agents Code with config files, administrator settings, environment variables, hooks, and CLI flags
- [Provider credentials](../deepagents/code/credentials.md): Add and manage API keys for model providers, Tavily web search, and LangSmith tracing
- [Config file](../deepagents/code/config-file.md): Configure model providers, defaults, retries, and gateways in config.toml
- [Hooks](../deepagents/code/hooks.md): Observe and control Deep Agents Code lifecycle events with command hooks configured in hooks.json
- [MCP tools](../deepagents/code/mcp-tools.md): Load additional tools from MCP (Model Context Protocol) servers
