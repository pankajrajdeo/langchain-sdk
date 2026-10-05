---
title: "Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE Build TypeScript"
description: "Documentation for LangSmith, Fleet, and our open source packages."
source: "https://docs.langchain.com/_llms/agent-development-lifecycle/build/type-script"
category: "docs"
tags: [docs, llms, agent-development-lifecycle, build, type-script]
---

# Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE Build TypeScript

> Documentation for LangSmith, Fleet, and our open source packages.

## TypeScript

### Overview

- [Build](../../../build-overview.md): Build agents with LangChain, LangGraph, Deep Agents, Managed Deep Agents, and Fleet.

### Deep Agents

- [Deep Agents overview](../../../javascript/deepagents/overview.md): Build agents that can plan, use subagents, and leverage file systems for complex tasks

#### Get started

- [Quickstart](../../../javascript/deepagents/quickstart.md): Build your first deep agent in minutes
- [Customize Deep Agents](../../../javascript/deepagents/customization.md): Learn how to customize Deep Agents with system prompts, tools, subagents, and more
- [Models](../../../javascript/deepagents/models.md): Configure model providers and parameters for Deep Agents
- [Comparison with Claude Agent SDK](../../../javascript/deepagents/comparison.md): Compare LangChain Deep Agents with the Claude Agent SDK to choose the right tool for your use case.
- [Changelog](../../../javascript/deepagents/changelog-js.md)

#### Deployment

- [Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents.md)

##### Going to production

- [Going to production](../../../javascript/deepagents/going-to-production.md): Take your deep agent to production with persistent memory, sandboxes, resilience middleware, and deployment options
- [Fault tolerance](../../../javascript/deepagents/fault-tolerance.md): Make your deep agent resilient with rate limiting, retries, fallbacks, and error handling

#### Execution environment

- [Tools](../../../javascript/deepagents/tools.md): Connect Deep Agents to custom functions, APIs, databases, and any MCP server
- [Backends](../../../javascript/deepagents/backends.md): Choose and configure filesystem backends for Deep Agents. You can specify routes to different backends, implement virtual filesystems, and enforce policies.
- [Permissions](../../../javascript/deepagents/permissions.md): Control filesystem access with declarative permission rules for Deep Agents
- [Multimodal inputs and outputs](../../../javascript/deepagents/multimodal.md): Use images, audio, video, and documents with Deep Agents when your model supports multimodal inputs and tool results
- [Sandboxes](../../../javascript/deepagents/sandboxes.md): Execute code in isolated environments with sandbox backends
- [Interpreters](../../../javascript/deepagents/interpreters.md): Run lightweight code inside Deep Agents to compose tools, orchestrate subagents, and transform structured data
- [Event streaming](../../../javascript/deepagents/event-streaming.md): Stream subagents, messages, tool calls, and final output from Deep Agents.
- [Streaming](../../../javascript/deepagents/streaming.md): Stream real-time updates from deep agent runs and subagent execution

#### Context management

- [Skills](../../../javascript/deepagents/skills.md): Learn how to extend your deep agent's capabilities with skills
- [Memory](../../../javascript/deepagents/memory.md): Add persistent memory to agents built with Deep Agents so they learn and improve across conversations
- [Retrieval](../../../javascript/deepagents/retrieval.md)
- [Context engineering in Deep Agents](../../../javascript/deepagents/context-engineering.md): Control what context your deep agent has access to and how it is managed across long-running tasks
- [Profiles](../../../javascript/deepagents/profiles.md): Package per-provider and per-model defaults that Deep Agents applies when a model is selected
- [OpenWiki](../../../javascript/deepagents/openwiki.md): Generate and maintain repository wikis that coding agents discover through AGENTS.md

#### Delegation

- [Subagents](../../../javascript/deepagents/subagents.md): Learn how to use subagents to delegate work and keep context clean
- [Dynamic subagents](../../../javascript/deepagents/dynamic-subagents.md): Use interpreters to dispatch and orchestrate Deep Agents subagents from code
- [Async subagents](../../../javascript/deepagents/async-subagents.md): Launch background subagents that run concurrently while the supervisor continues interacting with the user

#### Steering

- [Human-in-the-loop](../../../javascript/deepagents/human-in-the-loop.md): Learn how to configure human approval for sensitive tool operations

#### Middleware

- [Middleware overview](../../../javascript/langchain/middleware/overview.md): Control and customize agent execution at every step
- [Prebuilt middleware](../../../javascript/langchain/middleware/built-in.md): Prebuilt middleware for common agent use cases
- [Custom middleware](../../../javascript/langchain/middleware/custom.md)

#### Frontend

- [Overview](../../../javascript/deepagents/frontend/overview.md): Build UIs that display real-time subagent streams, task progress, and sandbox for Deep Agents

##### Patterns

- [Subagent streaming](../../../javascript/deepagents/frontend/subagent-streaming.md): Display specialist subagents with streaming content, progress tracking, and collapsible cards
- [Todo list](../../../javascript/deepagents/frontend/todo-list.md): Track agent progress with a real-time todo list synced from agent state
- [Sandbox](../../../javascript/deepagents/frontend/sandbox.md): Build an IDE-like UI for a coding agent backed by a sandbox environment

#### Protocols

- [Agent Client Protocol (ACP)](../../../javascript/deepagents/acp.md): Expose Deep Agents over the Agent Client Protocol (ACP) to integrate with code editors and IDEs.
- [Model Context Protocol](../../../javascript/deepagents/mcp.md)
- [A2A server](../../../javascript/deepagents/a2a.md)
- [Agent User Interaction Protocol (AG-UI)](../../../javascript/deepagents/ag-ui.md): Expose deep agents over the Agent User Interaction Protocol (AG-UI) to stream events to any AG-UI client or frontend.

### Managed Deep Agents

#### Get started

- [Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-overview.md): Build your agent as a directory of files while LangSmith runs the harness and runtime.
- [Managed Deep Agents quickstart](../../../langsmith/javascript/managed-deep-agents-quickstart.md): Create and deploy your first Managed Deep Agent with the mda CLI.
- [Managed Deep Agents project structure](../../../langsmith/javascript/managed-deep-agents-project-structure.md): Understand the project layout for Managed Deep Agents.
- [Move from Deep Agents to Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-migrate.md): Convert an agent built with create_deep_agent into a Managed Deep Agents project.

#### Agent capabilities

- [Define a Managed Deep Agent](../../../langsmith/javascript/managed-deep-agents-agent-definition.md): Configure the model and core capabilities of a managed deep agent.
- [Add instructions to Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-instructions.md): Define the system prompt for a managed deep agent in instructions.md.
- [Add skills to Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-skills.md): Add reusable task-specific instructions to a managed deep agent.
- [Add custom tools to Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-tools.md): Define authored tools for managed deep agents projects.
- [Built-in search powered by Parallel](../../../langsmith/javascript/managed-deep-agents-search.md): Add web search powered by Parallel to Managed Deep Agents without a separate account or API key.
- [Manage connections](../../../langsmith/javascript/managed-deep-agents-connections.md): Store API keys and OAuth grants so Managed Deep Agents can authenticate with external services at runtime.
- [Connect to MCP servers](../../../langsmith/javascript/managed-deep-agents-mcp-connectors.md): Add tools from remote MCP servers to a managed deep agent.
- [Add custom middleware to Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-middleware.md): Add built-in or custom middleware to a managed deep agent.
- [Add memory to Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-memory.md): Opt in to durable agent and user memory layers for a managed deep agent.
- [Add a sandbox to Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-sandboxes.md): Configure an isolated filesystem and shell for a managed deep agent.
- [Add identity to Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-identity.md): Authenticate callers to a Managed Deep Agents deployment with a LangSmith API key, Supabase, or your own backend.
- [Add schedules to Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-schedules.md): Declare managed cron schedules for Managed Deep Agents deployments.
- [Evaluate Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-evals.md): Develop Harbor evals for Managed Deep Agents with a coding agent and the eval-engineering skill.

##### Channels

- [Connect Managed Deep Agents to channels](../../../langsmith/javascript/managed-deep-agents-channels.md): Connect Managed Deep Agents to external messaging services that can start runs and receive responses.
- [Connect a Managed Deep Agent to Slack](../../../langsmith/javascript/managed-deep-agents-channels-slack.md): Start Managed Deep Agents runs from Slack messages and send responses to Slack conversations.
- [Connect a Managed Deep Agent over HTTP](../../../langsmith/javascript/managed-deep-agents-channels-http.md): Start Managed Deep Agents runs from any external service that can send a webhook, and return responses through your own transport.
- [Prompt Slack users with agent-owned interrupts](../../../langsmith/javascript/managed-deep-agents-agent-owned-interrupts.md): Post a Slack form from a Managed Deep Agents tool, pause the run, and resume it when the user submits the form.

#### Build and deploy

- [Develop locally with LangSmith Studio](../../../langsmith/javascript/managed-deep-agents-local-development.md): Run and test a Managed Deep Agent locally with mda dev and LangSmith Studio.
- [Add a custom search tool, memory, and a schedule](../../../langsmith/javascript/managed-deep-agents-tutorial.md): Replace provider search with a Tavily tool, then add durable memory and a daily schedule to the research assistant from the quickstart.
- [Deploy a Managed Deep Agent](../../../langsmith/javascript/managed-deep-agents-deploy.md): Test and deploy a Managed Deep Agent with the mda CLI.
- [Connect MCP clients to a Managed Deep Agent](../../../langsmith/javascript/managed-deep-agents-mcp-endpoint.md): Expose a deployed Managed Deep Agent as a tool to MCP clients such as Claude Code.
- [Manage Context Hub for Managed Deep Agents](../../../langsmith/javascript/managed-deep-agents-context-hub.md): Understand how Managed Deep Agents stores instructions, skills, and durable memory in LangSmith Context Hub.
- [Managed Deep Agents CLI reference](../../../langsmith/javascript/managed-deep-agents-cli.md): Reference for mda commands, project files, and deploy behavior.
- [Changelog](../../../langsmith/javascript/managed-deep-agents-changelog.md)

### LangChain

- [LangChain overview](../../../javascript/langchain/overview.md): LangChain provides create_agent: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware.

#### Get started

- [Install LangChain](../../../javascript/langchain/install.md): Install the LangChain package and the independent provider packages for the models and integrations you use.
- [Quickstart](../../../javascript/langchain/quickstart.md): Build your first agent in minutes
- [Changelog](../../../javascript/langchain/changelog-js.md)
- [Philosophy](../../../javascript/langchain/philosophy.md): LangChain exists to be the easiest place to start building with LLMs, while also being flexible and production-ready.

#### Core components

- [Agents](../../../javascript/langchain/agents.md): Build a LangChain agent: a model calling tools in a loop until a task is complete, shaped by a harness of prompt, tools, and middleware.
- [Models](../../../javascript/langchain/models.md): Initialize and configure chat models, the reasoning engine of LangChain agents, with support for tool calling, structured output, and multimodal inputs.
- [Messages](../../../javascript/langchain/messages.md)
- [Tools](../../../javascript/langchain/tools.md): Define tools that let LangChain agents fetch real-time data, execute code, query external databases, and take actions.
- [Short-term memory](../../../javascript/langchain/short-term-memory.md)
- [Event streaming](../../../javascript/langchain/event-streaming.md): Stream real-time updates from LangChain agent runs
- [Streaming](../../../javascript/langchain/streaming.md): Stream real-time updates from agent runs
- [Structured output](../../../javascript/langchain/structured-output.md)

#### Middleware

- [Middleware overview](../../../javascript/langchain/middleware/overview.md): Control and customize agent execution at every step
- [Prebuilt middleware](../../../javascript/langchain/middleware/built-in.md): Prebuilt middleware for common agent use cases
- [Custom middleware](../../../javascript/langchain/middleware/custom.md)

#### Frontend

- [Overview](../../../javascript/langchain/frontend/overview.md): Build generative UIs with real-time streaming from LangChain agents

##### Patterns

- [Markdown messages](../../../javascript/langchain/frontend/markdown-messages.md): Render LLM responses as rich, formatted markdown with proper streaming support
- [Tool calling](../../../javascript/langchain/frontend/tool-calling.md): Display agent tool calls with rich, type-safe UI cards
- [Headless tools](../../../javascript/langchain/frontend/headless-tools.md): Run browser and device APIs on the client with headless tool implementations
- [Human-in-the-Loop](../../../javascript/langchain/frontend/human-in-the-loop.md): Add approval workflows with interrupt-based human review
- [Branching chat](../../../javascript/langchain/frontend/branching-chat.md): Edit messages and regenerate responses by forking from checkpoints
- [Reasoning tokens](../../../javascript/langchain/frontend/reasoning-tokens.md): Display model thinking and reasoning processes in collapsible blocks
- [Structured output](../../../javascript/langchain/frontend/structured-output.md): Render structured agent responses with custom UI components instead of plain text
- [Message queues](../../../javascript/langchain/frontend/message-queues.md): Queue multiple messages and manage them while the agent processes sequentially
- [Join & rejoin streams](../../../javascript/langchain/frontend/join-rejoin.md): Disconnect from and reconnect to running agent streams
- [Time travel](../../../javascript/langchain/frontend/time-travel.md): Inspect, navigate, and resume from any checkpoint in the conversation history

###### Generative UI

- [Generative UI overview](../../../javascript/langchain/frontend/generative-ui-overview.md): Understand the generative UI spectrum from controlled to declarative to open-ended interfaces
- [Controlled generative UI](../../../javascript/langchain/frontend/controlled-generative-ui.md): Render agent output with components you author using components as tools, tool-call rendering, state rendering, and reasoning
- [Declarative generative UI](../../../javascript/langchain/frontend/declarative-generative-ui.md): Compose agent-generated interfaces from a registered component catalog using json-render and A2UI
- [Open-ended generative UI](../../../javascript/langchain/frontend/open-ended-generative-ui.md): Render UI created outside your application, such as sandboxed MCP Apps, at the open end of the generative UI spectrum

##### Integrations

- [Overview](../../../javascript/langchain/frontend/integrations/overview.md): Connect useStream to any React UI component library or generative UI framework
- [CopilotKit](../../../javascript/langchain/frontend/integrations/copilotkit.md): Use CopilotKit with LangGraph, Deep Agents, and React with custom endpoints, the Python AG-UI bridge, structured generative UI, and messaging-platform channels
- [AI Elements](../../../javascript/langchain/frontend/integrations/ai-elements.md): Composable shadcn/ui-based components for AI chat interfaces with useStream
- [assistant-ui](../../../javascript/langchain/frontend/integrations/assistant-ui.md): Headless React AI chat framework with a full runtime layer, bridged to useStream
- [OpenUI](../../../javascript/langchain/frontend/integrations/openui.md): Generate complete, interactive dashboards and reports using the OpenUI component library and openui-lang

#### Advanced usage

- [Guardrails](../../../javascript/langchain/guardrails.md): Implement safety checks and content filtering for your agents
- [Runtime](../../../javascript/langchain/runtime.md)
- [Context engineering in agents](../../../javascript/langchain/context-engineering.md)
- [Human-in-the-loop](../../../javascript/langchain/human-in-the-loop.md)
- [Retrieval](../../../javascript/deepagents/retrieval.md)
- [Long-term memory](../../../javascript/langchain/long-term-memory.md): Add long-term memory to LangChain agents to store and recall data across conversations and sessions

##### MCP

- [Model Context Protocol (MCP)](../../../javascript/langchain/mcp/index.md): Connect LangChain agents to MCP servers with MCPAdapter.
- [Tools](../../../javascript/langchain/mcp/tools.md): Load MCP tools into LangChain agents, control their execution, and handle server results and requests.
- [Connections](../../../javascript/langchain/mcp/connections.md): Connection lifecycle, multiple servers, deployment scaling, protocol eras, and caching for MCP in LangChain.
- [Authentication](../../../javascript/langchain/mcp/auth.md): Authenticate MCP connections with bearer tokens, OAuth 2.1, or per-user credentials in LangChain.

##### Multi-agent

- [Multi-agent](../../../javascript/langchain/multi-agent/index.md)
- [Subagents](../../../javascript/langchain/multi-agent/subagents.md)
- [Handoffs](../../../javascript/langchain/multi-agent/handoffs.md)
- [Skills](../../../javascript/langchain/multi-agent/skills.md)
- [Router](../../../javascript/langchain/multi-agent/router.md)
- [Custom workflow](../../../javascript/langchain/multi-agent/custom-workflow.md)

#### Agent development

- [LangSmith Studio](../../../javascript/langchain/studio.md)
- [Agent Chat UI](../../../javascript/langchain/ui.md)

##### Test

- [Test](../../../javascript/langchain/test/index.md): Strategies for testing LangChain agents, including unit tests, integration tests, and trajectory evaluations.
- [Unit testing](../../../javascript/langchain/test/unit-testing.md): Test agent logic without API calls using fake chat models and in-memory persistence.
- [Integration testing](../../../javascript/langchain/test/integration-testing.md): Test agents with real LLM APIs by organizing tests, managing keys, handling flakiness, and controlling costs.
- [Agent Evals](../../../javascript/langchain/test/evals.md): Evaluate agent trajectories using deterministic matching or LLM-as-judge evaluators with AgentEvals and LangSmith.

#### Production

- [Deployment](../../../javascript/langchain/deploy.md): Deploy LangChain agents to production with LangSmith Cloud or JavaScript frameworks and hosting platforms.
- [LangSmith Observability](../../../javascript/langchain/observability.md)

### LangGraph

- [LangGraph overview](../../../javascript/langgraph/overview.md): Gain control with LangGraph to design agents that reliably handle complex tasks
- [Studio](../../../javascript/studio.md): Develop, run, and debug LangGraph agents in an interactive environment with LangSmith Studio.

#### Get started

- [Install LangGraph](../../../javascript/langgraph/install.md)
- [Quickstart](../../../javascript/langgraph/quickstart.md)
- [Run a local server](../../../javascript/langgraph/local-server.md)
- [Changelog](../../../javascript/langgraph/changelog-js.md)
- [Thinking in LangGraph](../../../javascript/langgraph/thinking-in-langgraph.md): Learn how to think about building agents with LangGraph
- [Workflows and agents](../../../javascript/langgraph/workflows-agents.md)

#### Capabilities

- [Persistence](../../../javascript/langgraph/persistence.md): LangGraph's persistence layer gives agents short-term memory through checkpointers and long-term memory through stores.
- [Fault tolerance](../../../javascript/langgraph/fault-tolerance.md): Configure per-node timeouts, retries, and error handlers in LangGraph.
- [Checkpointers](../../../javascript/langgraph/checkpointers.md): LangGraph checkpointers save graph state as checkpoints at each step, enabling persistence, human-in-the-loop, and fault-tolerant execution.
- [Stores](../../../javascript/langgraph/stores.md): LangGraph stores provide cross-thread long-term memory, complementing per-thread checkpointer persistence.
- [Event streaming](../../../javascript/langgraph/event-streaming.md): Stream LangGraph runs with typed projections for messages, state, subgraphs, output, and extensions.
- [Streaming](../../../javascript/langgraph/streaming.md)
- [Interrupts](../../../javascript/langgraph/interrupts.md)
- [Use time-travel](../../../javascript/langgraph/use-time-travel.md): Replay past executions and fork to explore alternative paths in LangGraph
- [Memory](../../../javascript/langgraph/add-memory.md)
- [Subgraphs](../../../javascript/langgraph/use-subgraphs.md)

#### Production

- [Application structure](../../../javascript/langgraph/application-structure.md)
- [Test](../../../javascript/langgraph/test.md)
- [Backward compatibility](../../../javascript/langgraph/backward-compatibility.md): Update LangGraph graph code in production without breaking in-flight runs.
- [LangSmith Studio](../../../javascript/langgraph/studio.md)
- [Agent Chat UI](../../../javascript/langgraph/ui.md)
- [Deployment](../../../javascript/langgraph/deploy.md): Deploy LangGraph agents to production with LangSmith Cloud or JavaScript frameworks and hosting platforms.
- [LangSmith Observability](../../../javascript/langgraph/observability.md)

#### Frontend

- [Overview](../../../javascript/langgraph/frontend/overview.md): Render LangGraph agents to the frontend
- [Graph execution](../../../javascript/langgraph/frontend/graph-execution.md): Visualize multi-step graph pipelines with per-node status and streaming content
- [Custom stream channels](../../../javascript/langgraph/frontend/custom-stream-channels.md): Stream custom server-side data to the frontend and read it with useExtension and useChannel

#### LangGraph APIs

- [LangGraph runtime](../../../javascript/langgraph/pregel.md)

##### Graph API

- [Choosing between Graph and Functional APIs](../../../javascript/langgraph/choosing-apis.md)
- [Graph API overview](../../../javascript/langgraph/graph-api.md): LangGraph models agent workflows as graphs: define state, nodes, and edges with StateGraph to build looping, stateful workflows.
- [Use the graph API](../../../javascript/langgraph/use-graph-api.md)

##### Functional API

- [Functional API overview](../../../javascript/langgraph/functional-api.md)
- [Use the functional API](../../../javascript/langgraph/use-functional-api.md)

### OpenWiki

- [OpenWiki](../../../openwiki/overview.md): CLI that writes and maintains agent wikis so coding agents work faster
- [Quickstart](../../../openwiki/quickstart.md): Install OpenWiki, configure a model provider, and generate your first wiki.
- [Coding-agent integrations](../../../openwiki/integrations.md): Run OpenWiki inside Codex, Claude Code, OpenCode, or Cursor using the host model and tools
- [Visualize your wiki](../../../openwiki/visualize.md): Explore an OpenWiki Markdown wiki with a local interactive node graph and reader
- [Command reference](../../../openwiki/cli-reference.md): OpenWiki command-line usage, flags, and connector subcommands
- [Customize OpenWiki](../../../openwiki/customize.md): Ignore paths, wiki instructions, agent pointers, and telemetry for OpenWiki
- [Model providers](../../../openwiki/providers.md): Configure inference providers and credentials for OpenWiki
- [Automate updates](../../../openwiki/automate-updates.md): Schedule OpenWiki documentation updates with GitHub Actions, GitLab CI, or Bitbucket Pipelines
- [Changelog](../../../openwiki/changelog.md)

#### Modes

- [Code mode](../../../openwiki/code-mode.md): Generate and maintain repository documentation for coding agents with OpenWiki
- [Personal mode](../../../openwiki/personal-mode.md): Build a local personal brain wiki from configured sources with OpenWiki.

### Integrations

- [LangChain JavaScript integrations](../../../javascript/integrations/providers/overview.md): Integrate with providers using LangChain JavaScript/TypeScript.
- [All LangChain JavaScript integration providers](../../../javascript/integrations/providers/all_providers.md)

#### Popular Providers

##### OpenAI

- [OpenAI integrations](../../../javascript/integrations/providers/openai.md): Integrate with OpenAI using LangChain JavaScript.
- [ChatOpenAI integration](../../../javascript/integrations/chat/openai.md): Integrate with the ChatOpenAI chat model using LangChain JavaScript.
- [OpenAIEmbeddings integration](../../../javascript/integrations/embeddings/openai.md): Integrate with the OpenAIEmbeddings embedding model using LangChain JavaScript.
- [OpenAI integration](../../../javascript/integrations/tools/openai.md): Integrate with the OpenAI tool using LangChain JavaScript.

##### Anthropic

- [Anthropic integrations](../../../javascript/integrations/providers/anthropic.md): Integrate with Anthropic using LangChain JavaScript.
- [ChatAnthropic integration](../../../javascript/integrations/chat/anthropic.md): Integrate with the ChatAnthropic chat model using LangChain JavaScript.
- [Anthropic integration](../../../javascript/integrations/tools/anthropic.md): Integrate with the Anthropic tool using LangChain JavaScript.

##### Google

- [Google integrations](../../../javascript/integrations/providers/google.md): Integrate with Google using LangChain JavaScript.
- [ChatGoogle integration](../../../javascript/integrations/chat/google.md): Integrate with the ChatGoogle chat model using LangChain JavaScript.
- [Google integration](../../../javascript/integrations/tools/google.md): Integrate with Google Gemini tools using LangChain JavaScript.
- [ChatGoogleGenerativeAI integration](../../../javascript/integrations/chat/google_generative_ai.md): Integrate with the ChatGoogleGenerativeAI chat model using LangChain JavaScript.
- [ChatVertexAI integration](../../../javascript/integrations/chat/google_vertex_ai.md): Integrate with the ChatVertexAI chat model using LangChain JavaScript.

##### AWS

- [AWS integrations](../../../javascript/integrations/providers/aws.md): Integrate with AWS using LangChain JavaScript.
- [ChatBedrockConverse integration](../../../javascript/integrations/chat/bedrock_converse.md): Integrate with the ChatBedrockConverse chat model using LangChain JavaScript.
- [BedrockEmbeddings integration](../../../javascript/integrations/embeddings/bedrock.md): Integrate with the BedrockEmbeddings embedding model using LangChain JavaScript.

##### Microsoft

- [Microsoft integrations](../../../javascript/integrations/providers/microsoft.md): Integrate with Microsoft using LangChain JavaScript.
- [AzureChatOpenAI integration](../../../javascript/integrations/chat/azure.md): Integrate with the AzureChatOpenAI chat model using LangChain JavaScript.
- [AzureOpenAIEmbeddings integration](../../../javascript/integrations/embeddings/azure_openai.md): Integrate with the AzureOpenAIEmbeddings embedding model using LangChain JavaScript.

#### General integrations

- [Chat model integrations](../../../javascript/integrations/chat/index.md): Integrate with chat models using LangChain JavaScript.
- [Tool integrations](../../../javascript/integrations/tools/index.md): Integrate with tools using LangChain JavaScript.
- [LLM integrations](../../../javascript/integrations/llms/index.md): Integrate with LLMs using LangChain JavaScript.
- [Middleware integrations](../../../javascript/integrations/middleware/index.md): Integrate with middleware using LangChain JavaScript.
- [Sandbox integrations](../../../javascript/integrations/sandboxes/index.md): Integrate with sandbox providers using LangChain JavaScript.
- [Backend integrations](../../../javascript/integrations/backends/index.md): Filesystem backends for Deep Agents.
- [Store integrations](../../../javascript/integrations/stores/index.md): Integrate with stores using LangChain JavaScript.
- [Store integrations](../../../javascript/integrations/long-term-memory/index.md): Integrate with store backends for LangGraph long-term memory.
- [Document transformer integrations](../../../javascript/integrations/document_transformers/index.md): Integrate with document transformers using LangChain JavaScript.
- [Cache integrations](../../../javascript/integrations/llm_caching/index.md): Integrate with caches using LangChain JavaScript.

#### RAG integrations

- [Retriever integrations](../../../javascript/integrations/retrievers/index.md): Integrate with retrievers using LangChain JavaScript.
- [Text splitter integrations](../../../javascript/integrations/splitters/index.md): Integrate with text splitters using LangChain.
- [Embedding model integrations](../../../javascript/integrations/embeddings/index.md): Integrate with embedding models using LangChain JavaScript.
- [Vector store integrations](../../../javascript/integrations/vectorstores/index.md): Integrate with vector stores using LangChain JavaScript.
- [Document loader integrations](../../../javascript/integrations/document_loaders/index.md): Integrate with document loaders using LangChain JavaScript.
- [Store integrations](../../../javascript/integrations/stores/index.md): Integrate with stores using LangChain JavaScript.

### Learn

- [Learn](../../../javascript/learn.md): Tutorials, conceptual guides, and resources to help you get started.

#### Tutorials

##### Deep Agents

- [Build a deep research agent](../../../javascript/deepagents/deep-research.md): Build a multi-step web research agent with subagent delegation
- [Build a content builder agent](../../../javascript/deepagents/content-builder.md): Build a content writing agent with brand memory, skills, subagents, and image generation
- [Retrieval Augmented Generation (RAG) with Deep Agents](../../../javascript/deepagents/rag.md): RAG patterns for Deep Agents, including skills-guided retrieval, rubric grading, and a tutorial that indexes LangChain docs, offloads chunks to the filesystem, and delegates analysis to subagents

##### LangChain

- [Build a semantic search engine with LangChain](../../../javascript/langchain/knowledge-base.md)
- [Build a SQL agent](../../../javascript/langchain/sql-agent.md)
- [Build a voice agent with LangChain](../../../javascript/langchain/voice-agent.md)

##### Multi-agent

- [Build a personal assistant with subagents](../../../javascript/langchain/multi-agent/subagents-personal-assistant.md)
- [Build customer support with handoffs](../../../javascript/langchain/multi-agent/handoffs-customer-support.md)
- [Build a multi-source knowledge base with routing](../../../javascript/langchain/multi-agent/router-knowledge-base.md)
- [Build a SQL assistant with on-demand skills](../../../javascript/langchain/multi-agent/skills-sql-assistant.md)

##### LangGraph

- [Build a custom RAG agent with LangGraph](../../../javascript/langgraph/agentic-rag.md): Build a custom retrieval agent with LangGraph that decides when to search a vector store or respond directly.

#### Conceptual overviews

- [Runtimes, frameworks, and harnesses](../../../javascript/concepts/products.md): Understand the differences between LangChain, LangGraph, and Deep Agents and when to use each one
- [Providers and models](../../../javascript/concepts/providers-and-models.md): Understand how LangChain uses providers to give you a single API for any model from any provider
- [Component architecture](../../../javascript/langchain/component-architecture.md)
- [Memory overview](../../../javascript/concepts/memory.md)
- [Context overview](../../../javascript/concepts/context.md)
- [Graph API overview](../../../javascript/langgraph/graph-api.md): LangGraph models agent workflows as graphs: define state, nodes, and edges with StateGraph to build looping, stateful workflows.
- [Functional API overview](../../../javascript/langgraph/functional-api.md)

#### LangChain Academy

- [LangChain Academy](../../../javascript/langchain/academy.md)

#### Additional resources

- [Use docs programmatically](../../../use-these-docs.md): Connect LangChain documentation to your AI tools and workflows
- [Case studies](../../../javascript/langgraph/case-studies.md)
- [Get help](../../../javascript/langchain/get-help.md)

### Reference

- [Reference](../../../javascript/reference/overview.md)

#### Reference

- [Deep Agents](../../../javascript/reference/deepagents-javascript.md)
- [LangChain SDK](../../../javascript/reference/langchain-javascript.md)
- [LangGraph SDK](../../../javascript/reference/langgraph-javascript.md)
- [Integrations](../../../javascript/reference/integrations-javascript.md)
- [Errors](../../../javascript/common-errors.md)

#### Releases

- [Versioning](../../../javascript/versioning.md)
- [Changelog](../../../javascript/releases/changelog.md): Log of updates and improvements to our JavaScript/TypeScript packages

##### Releases

- [What's new in LangChain v1](../../../javascript/releases/langchain-v1.md)
- [What's new in LangGraph v1](../../../javascript/releases/langgraph-v1.md)

##### Migration guides

- [LangChain v1 migration guide](../../../javascript/migrate/langchain-v1.md)
- [LangGraph v1 migration guide](../../../javascript/migrate/langgraph-v1.md)
- [Migrate to @langchain/mcp-adapters 2.0](../../../javascript/migrate/langchain-mcp-adapters.md): Upgrade from @langchain/mcp-adapters 1.x to 2.0, covering renamed APIs, stricter configuration, authentication, elicitation, and tool result changes.

#### Policies

- [Release policy](../../../javascript/release-policy.md)
- [Security policy](../../../javascript/security-policy.md)

### Contribute

- [Contributing](../../../javascript/contributing/overview.md)

#### Contribute

- [Contributing to documentation](../../../javascript/contributing/documentation.md)
- [Contributing to code](../../../javascript/contributing/code.md)

##### Integrations

- [Contributing integrations](../../../javascript/contributing/integrations-langchain.md)
- [Implement a LangChain integration](../../../javascript/contributing/implement-langchain.md)
- [Using standard tests](../../../javascript/contributing/standard-tests-langchain.md)
- [Publish an integration](../../../javascript/contributing/publish-langchain.md)
- [Co-marketing](../../../javascript/contributing/comarketing.md)
