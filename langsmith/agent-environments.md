---
title: "Agent environments"
description: "How an agent's environments divide its traces, how to select one, and which parts of the set are fixed."
source: "https://docs.langchain.com/langsmith/agent-environments"
category: "docs"
tags: [docs, langsmith, agent-environments]
---

# Agent environments

> How an agent's environments divide its traces, how to select one, and which parts of the set are fixed.

An *environment* records where an agent was running when it produced a trace. Every trace an [agent](agents.md) records lands in exactly one of its environments, which are drawn from a fixed set of four.

Because the environment travels with the trace, where the agent was running is a property of the trace itself.

> [!NOTE]
>
> Agent-based workspaces are available on [LangSmith Cloud](cloud.md). They are not available on [self-hosted](self-hosted.md) LangSmith. To check whether your workspace is agent-based, look at the control at the top left. In an agent-based workspace, it is a workspace switcher that names your workspace. In a [project-based](observability-concepts.md#tracing-projects) workspace, it shows the LangSmith logo.

## Environment names

The four environments are fixed, and custom names are not supported. The environment switcher lists them most production-like first:

* **Production**
* **Staging**
* **Development**
* **Local**

How many of the four an agent has depends on [how it was created](create-an-agent.md). An agent created in the UI, through [Build](build-an-agent.md), starts with **Production** alone, and each of the others appears the first time a trace is addressed to it. An agent created any other way starts with all four.

LangSmith attaches no behavior to the choice beyond keeping each environment's traces apart. An environment does not change how an agent is instrumented, and the same build can report into a different environment by changing its [agent addressing](log-traces-to-agent.md).

## Select an environment

Wherever LangSmith needs one environment instead of all of them, it uses the same control: a button showing the current environment, which opens the list. It lists the agent's environments in the order above.

The environment selected when you arrive depends on the section:

* **Studio and alerts**: **Production**.
* **Monitoring and Deployments**: The environment you last used for the agent, or **Production** when there is none.
* **Tracing**: The environment you last used for the agent, then **Local**, then the first environment the agent has.

On Deployments, **Local** does not display, and the list adds a **Preview** entry when preview builds are turned on and the agent has previews.

The list holds only the environments that exist for the agent.

This control drives environment selection on Tracing, Monitoring, alerts, [Engine](engine.md), Studio, and Deployments. [Evaluators](evaluators.md) and [Insights](insights.md) also scope to a single environment, but they do it without this dropdown.

## See also

* [Agents](agents.md)
* [Log traces to an agent](log-traces-to-agent.md)
* [Log traces to a specific project](log-traces-to-project.md)
* [Observability concepts](observability-concepts.md)

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/agent-environments.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
