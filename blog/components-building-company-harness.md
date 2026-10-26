---
title: "The five components of building a &quot;company harness&quot;"
description: "Learn how LangChain built internal agents across marketing, sales, and engineering, and how they have completely changed how those teams work."
source: "https://www.langchain.com/blog/components-building-company-harness"
category: "blog"
published: "2026-10-24T23:49:00.000Z"
author: "LangChain Accounts"
tags: [blog, components-building-company-harness]
---

# The five components of building a &quot;company harness&quot;

***How do you build a company harness?***

***We've built internal agents at LangChain across marketing, sales, and engineering, and they have completely changed how those teams work. They weren't easy to get right. We spent a lot of time solving the problems that come with a multiplayer harness, and every team landed on the same core primitives:***

- ‍***It lives where people already work (for us that's Slack)***
- ***It knows who's asking and acts OBO that person for some services and with its own identity for others***
- ***It has memory, scoped globally and/or at the user level***
- ***Code runs in a sandbox and can make requests to services which require auth***
- ***Large % of its runs are scheduled rather than explicitly invoked by someone (ambient agents!!)***

***Thank you to ***[***@caspar_br***](https://x.com/@caspar_br)*** for help on this blog***

## LangChain Internal Agents

To ground this discussion, a brief overview of the three main agents we have at LangChain:

**GTM Agent**: a proactive, always-on agent that assists with GTM activities. Monitors and responds to emails, to new qualified leads, sends daily briefs, can answer questions about accounts, can run outbound motions

**OpenSWE**: our engineering agent, can work on and draft PRs, but also runs code review over all PRs

**Content Studio**: our marketing agent, can draft assets (blogs, images, PowerPoints, videos) in our style and with knowledge of our positioning

All of these agents are built in the same way. We think this is a general recipe for building company harnesses.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6add442530f2704b9d5e03af_HVZbWoXb0AAOzqm.png)

## Problem: User Experience

All our agents live where people already work, which for us is Slack. They each have their own [Slack apps](../langsmith/python/managed-deep-agents-channels-slack.md), and can be DM’d or tagged in a channel. One benefit of working with these agents in channels is that others can see how people use it.

One nice thing we added was the concept of “breaking” out a conversation in Slack. Oftentimes, a great conversation would be happening and you’d want to add in your agent to get their opinion or get them to do something. But if they ran in that thread it would pollute the human conversation and distract. So we added an easy way for agents to “breakout” into their own thread in the channel.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6add451310058c5037cabbb0_Harness%20user%20experience.jpeg)

There are some user experiences that are best NOT done in Slack. For example, when reviewing emails GTM Agent wants me to send, it's fine to do that in a one-off way in Slack, but if there is a big backlog it's not a fun experience at all to track those from Slack messages. For experiences like that, we did end up building a custom UI.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6add4532f950f25096ed5a7d_GTM%20agent%20user%20experience.jpeg)

## Problem: Identity

The thorniest and trickiest problem we tackled was identity, specifically: when these agents take actions, who do they take actions on behalf of?

There are two main ways this is handled in the industry:

- ‍*On-behalf-of*: the agent acts on behalf of the user invoking the agent*‍*
- *Fixed credentials*: there is a fixed set of credentials that the agent uses no matter who is invoking it (eg a service account)

This is how we handled it for each agent (docs: [Add identity to Managed Deep Agents](../langsmith/python/managed-deep-agents-identity.md), [Manage connections](../langsmith/python/managed-deep-agents-connections.md)):

#### OpenSWE:

- When you message it, it acts on behalf of you (eg will open up PRs with your GitHub handle)
- When it runs in background (for example, as a code review agent) it acts with its own identity (GitHub app)

#### GTM Agent:

- It has some tools (eg Salesforce access) where it uses a fixed identity, so not everyone has to log in
- It has some tools (eg email) where it acts on behalf of the user invoking the agent. These tools are ONLY available in DMs. In shared channels, they are not available

#### Content Studio:

- It has some tools (eg Notion) where it acts on behalf of the user invoking the agent
- It has some tools (eg Twitter) where it uses a fixed set of credentials, in this case for our company Twitter account. Only a whitelisted set of users can invoke certain operations here though. Eg not everyone can post to Twitter (they may only be able to read/draft)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6add459a10058c5037cac545_Content%20Studio%20agent.png)

## Problem: Memory

All agents have [two tiers of memory](../langsmith/python/managed-deep-agents-memory.md):

- Global memory: memory that applies to all users
- User memory: memory that only applies to the specific user

Agents decide which facts they want to remember to which level of memory.

This is probably the least explored area so far - we have a lot of work we want to do here!

## Problem: Code Execution

All three of our agents can write and execute code, and often need to in order to accomplish tasks. They all follow the pattern of running outside the sandbox, but connecting to it and executing code in there. They all have slightly different base images with different dependencies. OpenSWE (the most coding related agent) is intelligent about which base image it spins up (differs based on channel/user). They all take advantage of the [secret proxy](../langsmith/sandbox-auth-proxy.md) on [LangSmith Sandboxes](../langsmith/sandboxes.md) (see also [Add a sandbox to Managed Deep Agents](../langsmith/python/managed-deep-agents-sandboxes.md)) to let the agent connect to services in a safe and secure way from inside the sandbox itself.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ade4515f950f250960af9f0_LangSmith%20sandbox.jpeg)

## Problem: Scheduled Runs

A large percent of runs are scheduled or triggered in the background by events, rather than being directly kicked off by a user.

Some of these are set up by the developer of the agent. For example: OpenSWE listens for PRs and when a new one is created it reviews it.

Others of these are set up by the user asking the agent to do so. For example: I asked GTM agent to send me a daily brief, and it created its own [cron](../langsmith/python/managed-deep-agents-schedules.md) to do so.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6add46108744271fad7d41f3_Agent%20runs.png)

## All built on Managed Deep Agents

All of these agents are built on [Managed Deep Agents](../langsmith/python/managed-deep-agents-overview.md), which sits on top of the open source [Deep Agents](../deepagents/overview.md) harness. It provides infrastructure to solve all these problems (channels, crons, sandboxes, memory, identity) while providing enough flexibility to customize agent behavior as needed. Try it out today with the [quickstart](../langsmith/python/managed-deep-agents-quickstart.md)!
