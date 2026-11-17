---
title: "Monitor coding agent cost and pull requests"
description: "Track what your team's coding agents cost and link that spend to the GitHub or GitLab pull requests they open."
source: "https://docs.langchain.com/langsmith/coding-agents"
category: "docs"
tags: [docs, langsmith, coding-agents]
---

# Monitor coding agent cost and pull requests

> Track what your team's coding agents cost and link that spend to the GitHub or GitLab pull requests they open.

Send traces from your team's coding agents, such as Claude Code, Codex, and Cursor, to see what each coding agent costs. Connect GitHub or GitLab to link each [thread](threads.md) to the pull requests it opened, so you can see the spend behind each pull request. When a chart shows a pull request or a user's spend that stands out, open the threads behind that spend to see what the coding agent did.

> [!NOTE]
>
> The Coding agent type is in [beta](release-stages.md). It requires an [agent-based workspace](agent-registry.md), which is available on LangSmith Cloud and not on self-hosted LangSmith.

## Set up

The pull request connection and the coding charts on the agent Overview appear only on agents with the Coding type.

### Create an agent with the Coding type

If you send traces with an official LangSmith plugin to an agent ID that does not exist yet, LangSmith creates the agent and sets its type to **Coding**. Integrations that follow the [Coding agent metadata contract](coding-agent-metadata-contract.md) get the same behavior.

To set the type yourself, set **Agent type** to **Coding** when you [create an agent](create-an-agent.md).

Changing the type of an existing agent requires permission to manage workspace settings. To change it, click the **Agent settings**  icon on the agent's Overview and select **Change agent type**.

### Send traces to the agent

Set up tracing for each coding agent your team uses, and send its traces to your LangSmith agent with the Coding type. Each guide shows how to send traces to that agent.

You can send traces from all your coding agents to one LangSmith agent. That lets you run the same [evaluators](evaluators.md) on every coding agent and compare them by harness (the coding agent, such as Claude Code).

| Coding agent | Set up tracing |
| - | - |
| Claude Code | [Install the plugin](trace-claude-code.md#install-the-plugin) |
| OpenAI Codex | [Install the plugin](trace-with-codex.md#install-the-plugin) |
| Cursor | [Install the plugin](trace-with-cursor.md#install-the-plugin) |
| GitHub Copilot | [Configure tracing](trace-with-vscode-copilot.md#configure-tracing) |
| Deep Agents Code | [Trace with LangSmith](../deepagents/code/quickstart.md#trace-with-langsmith) |

To trace every engineer's sessions, admins can install the Claude Code, Codex, and Cursor plugins with a mobile device management (MDM) tool and lock the agent and workspace the traces go to. For the managed file and the settings you can lock, see Lock settings for [Claude Code](trace-claude-code.md#lock-settings), [Codex](trace-with-codex.md#lock-settings), and [Cursor](trace-with-cursor.md#lock-settings).

### Connect GitHub or GitLab

Pull request tracking uses the same GitHub and GitLab connections as [LangSmith Engine](engine.md). To connect an account, you need permission to update all of the agent's environments. Each provider adds its own requirement:

* **GitHub**: Installing the GitHub App for the first time requires permission to install it on your repositories, and your GitHub organization may require an admin to approve it. If you have already connected repositories to Engine, those installations appear in the connection dialog, and you can link them without authorizing GitHub again.
* **GitLab**: A workspace admin connects the account in workspace settings.

For details, see [Connect repositories to Engine](engine-repositories.md).

On the agent Overview, click **Track pull requests** and connect a GitHub or GitLab account. You can reuse an installation that is already connected to another agent in the workspace.

LangSmith links a pull request when GitHub or GitLab reports activity on it, such as opening, updating, or merging it. It links the threads whose traces record the pull request's repository and source branch in their Git metadata. Pull requests merged before you connect do not appear. Time to merge, cost per merged pull request, and the pull request cards fill in as developers open and merge pull requests.

If a pull request shows no threads, check that its traces record the repository and branch:

* **GitHub Copilot**: Records them only on the [Local harness](trace-with-vscode-copilot.md#choose-your-harness), and only for a folder with a Git remote.
* **Deep Agents Code**: Records them unless you [turn off Git trace attribution](../deepagents/code/config-file.md#disable-git-trace-attribution).

## Read the agent Overview

The summary cards at the top compare each metric with the period before:

* **Always shown**: **LLM cost**, **Threads**, and **Turns / thread**.
* **Before you connect GitHub or GitLab**: **Tokens** and **Cost / 1M tokens**.
* **After you connect**: **Cost / merged PR**, **Cache rate**, and **Time to merge**, which also shows the merge rate. These replace **Tokens** and **Cost / 1M tokens**.

Select a card to chart that metric over time. You can group the chart by dimensions such as pull request state, user, user group, Git user, repo, harness, provider, model, or a metadata key. Click a bar or category to open a filtered view of the threads behind it.

Below the summary, the Overview shows these cards:

* **Work type**: Threads by the kind of work they ask for: feature, bugfix, refactor, investigation, review, or off topic. This card requires the prebuilt Coding Work Type evaluator, and walks you through setting it up.
* **Skill usage**: Which skills the coding agents call.
* **Cost per PR by state**: Average cost of open, closed, and merged pull requests.
* **Top PRs by cost**: The most expensive pull requests in the time range, with each one's state, author, threads, turns, and cost. Each row links to the pull request.
* **Cost by conversation length**: Threads grouped by number of turns, with total cost and average cost per thread and per turn.

## Example uses

### Find expensive pull requests

Use **Top PRs by cost** to find the pull requests that cost the most. Open a pull request's threads to see the models and the user behind it.

### Check the effect of shorter threads

Each new turn sends the conversation so far, so long threads cost more per turn. If you ask engineers to start new threads more often, use **Cost by conversation length** to check whether long threads become less common.

### Compare models

When your team switches models, group cost over time by model to compare spend before and after. Check the merge rate on the **Time to merge** card in the same time range to see whether pull requests still get merged.

## See also

* [Trace Claude Code sessions](trace-claude-code.md)
* [Trace OpenAI Codex](trace-with-codex.md)
* [Trace Cursor](trace-with-cursor.md)
* [Trace GitHub Copilot](trace-with-vscode-copilot.md)
* [Trace Deep Agents Code](../deepagents/code/quickstart.md#trace-with-langsmith)
* [Route coding agents through the LLM Gateway](llm-gateway-coding-agents.md)
* [Coding agent metadata contract](coding-agent-metadata-contract.md)
* [Cost tracking](cost-tracking.md)

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/coding-agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
