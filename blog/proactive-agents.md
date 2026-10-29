---
title: "Why aren’t you building proactive agents yet?"
description: "Most proactive agents run on a simple cron. Learn what scheduled runs unlock, from memory to smart triage, and how to add them to Managed Deep Agents."
source: "https://www.langchain.com/blog/proactive-agents"
category: "blog"
published: "2026-10-28T07:15:00.000Z"
author: "LangChain Accounts"
tags: [blog, proactive-agents]
---

# Why aren’t you building proactive agents yet?

Ever hear of the Baader-Meinhof phenomenon? It's when you learn a word for the first time, and suddenly start hearing it everywhere. I think the same principle applies in software engineering: You learn about a simple, but effective, design pattern, and then suddenly start seeing it everywhere.

We're seeing this happen with proactive agents, where we've noticed that nearly all of your favorite emerging proactive agentic systems are powered by a very simple mechanism: Agent runs as cron tasks, leveraging a more than fifty-year old principle of operating systems for a very modern use case.

The future belongs to proactive, always-on, ambient agents. Launches like Muse, Instinct, Dots, Claude Duet, Hone, and more reflect this.

Crons power a few different capabilities that combine to make these agents proactive, personalized, and [ambient](https://www.langchain.com/blog/introducing-ambient-agents) — that is, they can perform tasks on their own, without being manually instructed.

In this blog, we will go through the capabilities that crons unlock, the two core underlying parts you need in order to build agents like this, and then show examples of how you can do this in [Managed Deep Agents](https://app.notion.com/p/Proactive-Agents-406808527b1780d2b7b2e31c5fcf7748?pvs=21).

We’ve seen the impact crons can have. Proactivity is the new default for agent behaviour because of the breadth of new functions it unlocks. **More than 70% of Managed Deepagent runs on LangSmith come from scheduled runs** rather than a human typing a message.

## What do crons unlock?

Crons, despite being a simple concept, unlock a few different behaviors that shape these proactive, always-on agents.

**Memory:** A distinctive part of all these agents is that they remember facts about you over longer time horizons. Implementing this partially involves running a background job to condense previous conversations into a denser form of memory. This is colloquially called “dreaming”. Under the hood, this is just a cron that runs on some cadence (e.g. once a day) and updates long-term memory with any learnings from reflecting on the conversations.

**Proactiveness**: Part of what makes these agents work is that they initiate communication about an idea that they think you may be interested in. Under the hood, the way that this works is there is some “idea” of what this agent should be accomplishing.

For a general purpose agent, it may be as simple as being a good assistant: taking steps to anticipate what you need next, like flagging an upcoming deadline, following up on an open thread, or surfacing news related to your work. For specialized agents, like with Hone, the agent is working towards an explicit goal. The cron then runs on some cadence (once an hour) and prompts the agent to explore new actions to progress on its goal. These actions then show up as proactive messages to the user.

**Smart Triage:** There is so much noise in the world. A big use case for always-on agents is to monitor a source of information (Slack, Email, etc) and ping the user with relevant messages. Under the hood, this can be implemented as a cron that runs on a cadence (once every ten minutes) and is prompting an agent to look at an event stream and notify the user of anything of note.

**Follow ups**: Crons aren’t just used in the background. Oftentimes users may ask to be reminded about something at some point. Crons can be used to set a schedule to wake up and remind the user then.

**Orchestration:** Agent fleets can be managed by a single orchestration agent with the ability to wake itself up in the future. An orchestrator agent can monitor a fleet with crons. It can sleep while waiting for an asynchronous subtask to finish, and wake itself back up again to check in on progress at regular intervals.

## The two key parts to building proactive agents

In order two build these types of agents, we’ve found that there is generally two key parts.

First is a robust cron server. You will need a server that makes it easy for developers to add crons . They should be able to add them with whatever schedule they need, and include a prompt to run as part of that. If the agent needs certain skills or permissions when running, these should be included. If there are a lot of runs at a specific time point, the server should “jitter” them slightly to spread out the load.

Second, you need an agent-friendly interface. For actions like follow ups, the agent needs to be able to interact with these reminders. It needs an easy - but governed - way to set up and modify reminders.

## Build this with MDA

Managed Deep Agents - which are hosted using [LangSmith Deployments](https://www.langchain.com/langsmith/deployment) - provide a built-in cron server that can dynamically trigger an agent run. A scheduled run is deceptively simple: It is just the prompt that was passed in, triggered at a schedule, with the thread and memory based on the principal who created the schedule. This toolkit above provides foundation for tools that accept only a prompt and a cron schedule.

With Managed Deep Agents, schedules can be defined either statically or dynamically by an agent.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ae21b2813f25a98348ba1ca_image.png)In Managed Deep Agents, schedules can be defined within the agent definition or can be created at runtime by calling the Schedules SDK with tools.

For example, building an agent with a fixed schedule as part of its core design - say, a daily sales readout - is just a file in `schedules/`:

```
# schedules/daily_digest.py
from managed_deepagents import define_schedule

schedule = define_schedule(
    cron="0 8 * * 1-5",
    timezone="America/Los_Angeles",
    prompt="Inspect the sales report using your tools and send a KPI readout.",
)
```

Managed Deep Agents also offers dynamic schedules, where end users can prompt your agent to schedule recurring tasks that you didn’t anticipate in development. To support this, wrap the Schedules SDK in tools:

```
# tools/scheduling.py
from langchain.tools import tool
from managed_deepagents import ManagedDeepAgentRuntime

@tool
async def set_schedule(prompt: str, cron: str, runtime: ManagedDeepAgentRuntime) -> str:
    """Run a prompt for the current user on a cron schedule."""
    item = await runtime.schedules.create(owner={"type": "user"}, cron=cron, prompt=prompt)
    return f"Created schedule {item['id']}."

@tool
async def list_schedules(runtime: ManagedDeepAgentRuntime) -> str:
    """List the current user's schedules."""
    page = await runtime.schedules.list(owner={"type": "user"})
    return str(page["items"])

@tool
async def delete_schedule(schedule_id: str, runtime: ManagedDeepAgentRuntime) -> str:
    """Delete one of the current user's schedules."""
    await runtime.schedules.delete(schedule_id, owner={"type": "user"})
    return f"Deleted schedule {schedule_id}."
```

`‍`Developers need flexibility, and the Managed Deep Agents tool system is designed with this in mind. Different agent types may need to expose different toolkits for scheduling. In some cases, a basic `remind_me` wrapping one-off run or a `check_in_later` may be sufficient:

```
from datetime import datetime, timedelta, timezone

from langchain.tools import tool
from managed_deepagents import ManagedDeepAgentRuntime

@tool
async def check_in_later(prompt: str, minutes: int, runtime: ManagedDeepAgentRuntime) -> str:
    """Run a prompt once for the current user, a number of minutes from now."""
    at = datetime.now(timezone.utc) + timedelta(minutes=minutes)
    item = await runtime.schedules.create(owner={"type": "user"}, at=at, prompt=prompt)
    return f"Scheduled a check-in {item['id']}."
```

Get started with adding schedules to your Managed Deep Agents from our documentation: [langch.in/mda](http://langch.in/mda). You’re one `mda init` and `mda deploy` away from distributing a proactive agent within your organization.

‍
