---
title: "Create an agent"
description: "The four ways an agent is created in LangSmith, what each route decides about the agent it makes, and the rules an identifier must follow."
source: "https://docs.langchain.com/langsmith/create-an-agent"
category: "docs"
tags: [docs, langsmith, create-an-agent]
---

# Create an agent

> The four ways an agent is created in LangSmith, what each route decides about the agent it makes, and the rules an identifier must follow.

You can create an [agent](agents.md) through four routes. The route you choose sets how the agent gets its identifier and how many [environments](agent-environments.md) the agent starts with.

Pick a route based on where the agent runs. If you build the agent in LangSmith, LangSmith creates the agent as you build it. If the agent runs on your own machines, LangSmith can create the agent when the agent sends its first trace.

> [!NOTE]
>
> Agent-based workspaces are available on [LangSmith Cloud](cloud.md). They are not available on [self-hosted](self-hosted.md) LangSmith. To check whether your workspace is agent-based, look at the control at the top left. In an agent-based workspace, it is a workspace switcher that names your workspace. In a [project-based](observability-concepts.md#tracing-projects) workspace, it shows the LangSmith logo.

## Compare the four routes

An agent can be created in four ways, which differ in how the identifier is set and which environments the agent starts with:

| Route | Use it when | Identifier | Environments at creation |
| - | - | - | - |
| [Build tab](build-an-agent.md) | LangSmith runs the agent for you | Generated for you | Production alone |
| **Create a new agent** dialog | You want the agent named before its first run | You set it | All four |
| [Tracing](log-traces-to-agent.md) to an identifier that does not exist | The agent already runs somewhere else | The value you send | All four |
| [Deploying a project](deploy-to-agent-environment.md) | You deploy the agent from a project | The agent ID you pass, or derived from the deployment name | All four |

Not every agent can have a [deployment](deployment.md). An agent created by deploying a project has a deployment from the start. An agent created by a trace, by the Observability option in the [**New Agent** panel](#start-from-the-new-agent-panel), or by the **Create a new agent** dialog has no deployment at first, but you can [deploy to it](deploy-to-agent-environment.md) later. An agent built in the UI cannot have a deployment, because it runs on a Studio runtime. After a deployment, the agent's Overview shows a **Deployments** section.

An agent created in the UI gains its other environments the first time a trace is addressed to one. For what the four are, see [Agent environments](agent-environments.md#environment-names).

## Identifier rules

An identifier is 1 to 63 characters, using lowercase letters, digits, and hyphens. It must start with a letter and end with a letter or digit, so `support-agent` and `billing-v2` are valid. Anything else is rejected.

The rules apply wherever you supply the value: in the **Agent ID** field, in the identifier you trace to, and in the agent ID you deploy to. The Build tab generates an identifier instead. A deployment without an agent ID derives one from the deployment name, appending a suffix when that value is already taken, so a deployed agent can end up with an identifier close to the deployment name rather than equal to it.

An identifier cannot be changed after the agent is created. The display name can. For which value is which, see [Identifiers and display names](agents.md#identifiers-and-display-names).

## Start from the New Agent panel

Four controls open the **New Agent** panel: **+ Agent** above the agent list, **+ Create new agent** and **Trace existing agent** on a creation card at the end of the list, also titled **New Agent**, and the **+** button beside the search box in the agent switcher, which shows a **New agent** tooltip on hover. **Trace existing agent** opens the panel on the Observability option, and the other three open it on its grid of options. An **All options** button returns to the grid.

The panel hands off to four flows. Only Observability creates the agent inside the panel:

* **Builder** ("Build and configure inside LangSmith"): Leaves the panel for the **Build** tab, where submitting the form creates the agent. See [Build an agent in the UI](build-an-agent.md).
* **Managed Deep Agent** ("Build locally and deploy"): The agent is created when you deploy. See [Managed Deep Agents](python/managed-deep-agents-overview.md). This route requires a paid plan.
* **Open Source** ("Build an agent with our open source frameworks"): The agent is created by the first trace. See [LangChain](../langchain/overview.md).
* **Observability** ("Trace an existing agent"): Name the agent in the panel, and LangSmith creates it and opens its tracing page, which holds the setup steps. See the [tracing quickstart](observability-quickstart.md).

## Name an agent traced from outside LangSmith

To create the agent before any trace arrives, name it in either of two places:

* The Observability option in the **New Agent** panel.
* The **Create a new agent** dialog, opened from **+ New agent** below the agent list on Tracing when no agent is selected.

Both take an **Agent name** and, in its own field, an **Agent ID**, with a note that the ID is used in URLs and API calls and cannot be changed later. Both require permission to create projects. The agent switcher has the same **+** button, beside its search box, for users with the same permission, wherever the switcher appears, and it opens the **New Agent** panel rather than the dialog.

Creating the agent first is optional. [Tracing to an identifier that does not exist](log-traces-to-agent.md#send-traces-to-an-agent) creates the agent under the value you sent, so the dialog is for naming an agent ahead of its first run.

## See also

* [Agents](agents.md)
* [Agent environments](agent-environments.md)
* [Build an agent in the UI](build-an-agent.md)
* [Deploy to an agent environment](deploy-to-agent-environment.md)
* [Log traces to an agent](log-traces-to-agent.md)

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/create-an-agent.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
