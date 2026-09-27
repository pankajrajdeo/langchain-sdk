---
title: "Connect a Managed Deep Agent to Slack"
description: "Start Managed Deep Agents runs from Slack messages and send responses to Slack conversations."
source: "https://docs.langchain.com/langsmith/python/managed-deep-agents-channels-slack"
category: "docs"
tags: [docs, langsmith, managed-deep-agents-channels-slack]
---

# Connect a Managed Deep Agent to Slack

> Start Managed Deep Agents runs from Slack messages and send responses to Slack conversations.

A Slack channel lets people invoke a managed deep agent through app mentions, direct messages, and replies in an active Slack thread. Managed Deep Agents verifies Slack events, maps each conversation to a thread, runs the agent as the resolved caller, and posts the response back to Slack.

Managed Deep Agents creates and configures the resources that connect Slack to the deployed agent. Add a channel declaration to the agent project, then deploy.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Project structure

```text
my-agent/
  agent.py
  channels/
    slack.py
```

## Add a Slack channel

A managed deep agent deployment supports one Slack channel.

The channel declaration lives at `channels/slack.py`.

To include Slack when you create a project, pass `--channel slack`:

```bash
uvx --from managed-deepagents mda init my-agent --channel slack
```

To add Slack to an existing project, run the channel initialization command from the project root:

```bash
uv run mda channels init slack
```

**channels/slack.py**

```python
from managed_deepagents import channels

channel = channels.slack()
```

## Configure your agent's appearance in Slack

Edit the channel declaration to control how the agent appears in Slack.

#### `name` — `string`
The agent name in Slack. The name must contain 1–35 characters and can contain letters, numbers, spaces, underscores, dashes, and periods. It cannot start or end with a space or dash.

#### `description` — `string`
A description of what the agent does. The description can contain up to 139 characters.

#### `icon` — `string`
A path to the agent icon shown in Slack, relative to the `channels/` directory. The icon must be a 512 by 512 pixel PNG file no larger than 1 MB. If you omit this parameter, Managed Deep Agents will generate an icon for you.

#### `background_color` — `string`
The background color behind the agent icon as a six-digit hexadecimal color, such as `#1d4ed8`.

For example, put an icon next to the channel declaration:

```text
my-agent/
  agent.py
  channels/
    slack.py
    support-agent.png
```

**channels/slack.py**

```python
from managed_deepagents import channels

channel = channels.slack(
    name="Support Agent",
    description="Answers customer questions about orders and returns",
    icon="support-agent.png",
    background_color="#1d4ed8",
)
```

### Configure which messages start runs

#### `trigger_on_all_messages` — `bool`
Whether every new channel message can start an agent run. When `False`, channel messages start runs only when they mention the agent; direct messages still start runs.

#### `allow_bot_triggers` — `bool`
Whether messages from other Slack bots can start agent runs.

## Deploy the agent

During deployment, Managed Deep Agents provisions your agent in Slack from the channel declaration.

### Deploy your agent
Run the deployment command from the project root:

```bash
uv run mda deploy
```

Managed Deep Agents deploys the agent and sets up the resources it needs to appear in Slack.

### Authorize Slack if prompted
If you haven't authorized LangSmith before, the CLI displays an HTTPS authorization link. Open the link, select the Slack workspace, and approve the requested access.

Return to the terminal and press Enter. The CLI checks the authorization again and continues provisioning. If the Slack workspace requires admin approval, complete that approval before continuing.

### Use the agent in Slack
After the first deployment, your agent sends you a direct message in Slack. Reply to the message to start an agent run. The final response appears in the Slack conversation.

> [!NOTE]
> Human-in-the-loop requests in Slack support only the `approve` and `reject` [decision types](managed-deep-agents-tools.md#human-in-the-loop).

If Slack is already authorized, deployment completes without an authorization prompt.

After you change the agent's name, description, icon, or background color in the Slack channel declaration, redeploy the agent to apply the changes in Slack.

## Exchange files with Slack

A Slack channel moves files in both directions. Uploads land in the agent's sandbox under `/workspace/attachments/`, and the agent sends a file back by calling `attach_file` with a path under `/workspace`. Declaring a Slack channel and a [sandbox](managed-deep-agents-sandboxes.md) is the whole setup.

> [!NOTE]
> Slack file transfer requires `managed-deepagents>=0.8.0` and a sandbox. Without a sandbox, incoming files are not saved and `attach_file` is not offered to the model.

Managed Deep Agents stages the files on the incoming message before the run, along with files shared earlier in the same Slack thread. The agent reads an attachment status message for the paths, then opens the files with its sandbox tools. That status and the file contents are labeled as data, not instructions.

Attachment is never automatic, so state in the agent's [instructions](managed-deep-agents-instructions.md) when a file belongs in the reply:

**instructions.md**

```markdown
When someone asks for a report, write the report to a file under `/workspace`,
then call `attach_file` with that path so the file arrives in Slack.
```

Files stay scoped to the Slack thread they arrived in, because every thread gets its own sandbox. A direct message and a channel thread never share attachments. Within one thread, anyone reaches the files anyone else uploaded, since transfers use the bot's Slack access rather than the caller's.

### Review transfer limits

* **File size**: 200 MiB in each direction.
* **Paths**: `attach_file` accepts paths under `/workspace` only.
* **Thread history**: the scan covers recent messages in the thread. When it falls short, the attachment status reports that earlier files may be missing.
* **Skipped files**: files stored outside Slack, and files deleted from Slack.
* **Slack scopes**: a transfer blocked by a missing `files:read`, `files:write`, or history scope reports that you need to reconnect Slack.

## See also

* [Channels overview](managed-deep-agents-channels.md): understand how channels connect messaging services to an agent.
* [Agent-owned interrupts](managed-deep-agents-agent-owned-interrupts.md): post a Slack form from a tool and resume the run on submit.
* [Sandboxes](managed-deep-agents-sandboxes.md): give the agent the filesystem that file transfers read and write.
* [Deploy an agent](managed-deep-agents-deploy.md): configure and deploy a managed deep agent.
* [CLI reference](managed-deep-agents-cli.md): review Managed Deep Agents commands and flags.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-channels-slack.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
