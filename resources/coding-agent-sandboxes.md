---
title: "Coding Agent Sandboxes: Why Agents Need Isolated Environments"
description: "Coding agents generate code, install dependencies, run tests, and edit files. These capabilities make them useful, but they also give untrusted, model-generated code access to the systems around it."
source: "https://www.langchain.com/resources/coding-agent-sandboxes"
category: "resources"
published: "2026-10-15"
author: "LangChain"
tags: [resources, coding-agent-sandboxes]
---

# Coding Agent Sandboxes: Why Agents Need Isolated Environments

## Why coding agents need secure sandboxes

Coding agents generate code, install dependencies, run tests, and edit files. These capabilities make them useful, but they also give untrusted, model-generated code access to the systems around it.

Production coding agents need isolated execution environments where they can write files, install dependencies, run tests, and inspect failures without reaching the host machine. Hardware-virtualized sandboxes are a good fit for such environments. In addition, they can produce a record of the agents actions that can serve as input for improving the agent. Such sandboxes need the following to be suitable for production environments:

- Code isolation at the kernel level
- Fast starts
- Persistent state
- Enforceable network and resource limits
- Lifecycle control via API

A production sandbox must isolate code at the kernel level, start fast so work isn't blocked, preserve useful state, enforce network and resource limits, and let the orchestrator control every step of lifecycle through an API.

## Why coding agents need stronger isolation than what a standard container provides

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ad0fb58faa46865a3c67a64_container-vs-microvm-isolation.png)

A coding agent does not invoke one narrow, predefined operation. It can write a shell command, fetch a package, execute a test suite, start a server, and use the result to decide what to do next. In many workflows, that's the same permissions as a developer sitting at a terminal.

That authority makes the code untrusted by definition, regardless of intent. Whether the risk comes from faulty output, a compromised dependency, or a prompt injection, the sandbox must let the agent work without letting its actions escape the assigned environment. It should expose only the credentials required for the task and disappear when the work ends.

Containers help with packaging and process isolation, but standard containers share the host kernel. Namespaces and control groups separate processes and resources, yet a kernel vulnerability or container escape can still cross that boundary. For trusted application code, that tradeoff is often acceptable. For code generated in an agent loop, a safer boundary is a separate kernels for code execution and the host, which hardware virtualization provides.

A hardware-virtualized sandbox runs with its own guest kernel behind a hypervisor, adding a boundary between the code and the host so a process can't reach the host kernel through ordinary system calls. No sandbox creates perfect isolation, but a separate kernel materially reduces the blast radius of this workload.

Isolation is the fundamental requirement for running agents safely. But production usage adds requirements on top of that baseline.

## What a production coding agent needs in a sandbox

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ad0fb7a2791a0e9ad8591c1_sandbox-requirements-layers.png)

A production sandbox relies on the requirements below. Weaknesses in any of them show up as either security exceptions that engineers have to work around or latency that the agent incurs on every iteration.

### **Isolate untrusted code with a separate kernel**

Some coding tasks require root privileges to install system packages, start services, or run Docker. A good sandbox gives the agent that freedom inside its assigned environment without granting the same authority on the host.

That combination requires a separate guest kernel between the workload and both the host and neighboring tenants; a process namespace alone doesn't provide the same boundary.

### **Sub-second starts and persistent state**

Coding agents rarely execute a single command. They make a change, run a test, inspect the output, revise the code, and test it again, putting sandbox startup directly in the agent loop.

Sub-second startup keeps isolation from becoming a tax on every tool call. [LangSmith Sandboxes](https://www.langchain.com/langsmith/sandboxes) use prewarmed microVMs to bring isolated environments online quickly and have a p50 latency under 0.98 seconds. Teams can quickly create sandboxes on demand, removing the need for a pool of long-lived, broadly privileged workers.

Fast creation has to coexist with state because packages, source files, build artifacts, and test results should survive useful pauses and later agent turns. Processes can terminate between turns while the filesystem persists for the life of the task, so the agent can retain files and dependencies without relying on long-running processes.

Snapshots provide a repeatable starting point for repositories, dependencies, and test fixtures, which makes both agent iteration and evaluation faster.

### **Egress controls**

Many coding tasks need network access so an agent can fetch dependencies, call a model, read an issue, or push a branch. Because unrestricted egress gives generated code a path to exfiltrate data or contact arbitrary services, that access still needs a policy.

For production, use deny-by-default or allowlisted outbound access. When a request needs authentication, route it through an [auth proxy](https://www.langchain.com/blog/how-auth-proxy-secures-network-access-for-langsmith-agent-sandboxes). The proxy adds credentials after the request leaves the sandbox and only for approved external services. The agent can then call an approved API without reading the underlying secret from an environment variable or file. This keeps credentials outside the sandbox but allows the agent to complete approved work.

### Resource limits

Resource limits prevent runaway workloads from consuming unlimited capacity. CPU, memory, storage, and wall-clock ceilings contain infinite loops, runaway builds, and dependency risks. Set these limits when the sandbox starts so the platform can enforce them automatically throughout the run.

### Ephemerality and persistent state

Production systems need to spin up many concurrent, short-lived sandboxes. They should be easy to create for a task, stop when idle, and delete when no longer needed.

Agents also need to pick up where they left off. Task-scoped state preserves the repository, filesystem changes, and working context across calls, so the sandbox can stay ephemeral without forcing the agent to restart from scratch.

### Programmatic usage for agents

A sandbox should be controllable through an API and SDK, so an agent can create, inspect, stop, snapshot, fork, and delete a sandbox.

This approach creates a clean architecture boundary. The agent reasons about the task and calls tools while the sandbox service owns execution policy, credentials, network rules, and lifecycle. With this separation, you can change the agent without rebuilding the execution layer or change the isolation policy without rewriting the agent loop.

## Workflows for coding agent sandboxes

Coding agents connect to sandboxes in one of two ways: the agent runs inside the sandbox, or it runs outside and calls the sandbox as a remote execution tool. Both patterns can support coding workflows, but they draw the security boundary in different places.

For a deeper comparison, see [The two patterns by which agents connect sandboxes](https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes).

### Write, test, and fix in one loop

In this pattern, the agent uses the [sandbox as a tool](https://www.langchain.com/blog/execute-code-with-sandboxes-for-deepagents) to run commands against the repository. Your agent writes a patch, runs the relevant test command, reviews the test output and error messages, and edits the patch based on the failure. The same environment preserves the repository and installed dependencies between calls.

This workflow gives the model grounded feedback. Instead of predicting whether the code works, it can observe the compiler, test runner, linter, browser, or application itself. The sandbox confines the code's activity to the assigned environment while keeping the resulting evidence in the agent’s context.

You can also run the agent inside the sandbox when it needs a full computer-like environment, long-running shell state, or direct access to local tools. The process orchestrating the agent now lives alongside the code it executes, making network and credential policies even more important.

### Clone, test, and open pull requests

A CI agent needs a clean, reproducible environment for every run. A fresh sandbox gives each run its own machine-level boundary and a deterministic starting point.

Because the agent needs access to the repository and package dependencies, scope its repository credentials to the task and limit outbound access to the source host and approved registries. Terminate the environment after it pushes the branch. The trace still records how the agent arrived at the patch, while CI provides an independent check on the result.

### Branch in parallel from one snapshot

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ad0fbb9c14c1bb7601e23d6_Branch%20in%20parallel%20from%20one%20snapshot.png)

When an agent has several plausible fixes, running them sequentially is inefficient, but creating and preparing a full environment for every branch wastes compute.

Snapshots and forks let agents reuse a prepared environment while keeping each candidate fix isolated. You can start with one prepared filesystem and fork it into isolated branches that share unchanged disk blocks. Each branch can try a different implementation against the same tests without reinstalling every dependency. In [LangSmith Sandboxes](https://www.langchain.com/langsmith/sandboxes), spinning up ten parallel branches costs about the same as one.

Once the branches have run, the agent can compare their test results, traces, or evaluation scores and discard the weaker candidates. That parallelism improves the patch the agent finds and how quickly it finds one.

### Run evaluations and RL jobs at scale

Files and dependencies left by one sample can contaminate the next unless every evaluation or reinforcement learning run starts in its own isolated environment. The [harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) can then ask the agent to modify a repository, run commands, and return an artifact or score.

Prewarmed fleets make it possible to provision sandboxes across a dataset without paying a long boot penalty for every example. Resource and network policies remain consistent across the fleet, while snapshots provide a common starting state. That makes parallel results easier to compare and failed runs easier to reproduce.

This turns sandboxed execution into part of the evaluation harness. The same policy, filesystem base, and trace format can be reused across test runs, making regressions easier to detect and reproduce.

## Where coding sandboxes fit into the Agent Development Lifecycle

Sandboxes are useful not only for coding agents, but any production agent that benefits from the ability to write and execute code. This includes data analysis, document parsing, and calling APIs within an agent workflow. Agents that perform these tasks benefit from the same sandbox requirements as coding agents.

[LangSmith Sandboxes](https://www.langchain.com/langsmith-platform) are secure, isolated environments in LangSmith for running agents and agent-generated code. Sandboxes provides agents with ephemeral microVMs that they can use without affecting your main infrastructure. Sandboxes use the same SDK and API key as the rest of LangSmith and work with any framework or custom code.

Sandboxes are most effective when they work within a managed, integrated platform that supports every phase of [the Agent Development Lifecycle](https://www.langchain.com/blog/the-agent-development-lifecycle) (ALDC). This loop has four main parts that creates a repeatable system for shipping, learning, and improving overtime.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ad0fbe88854a2bcde23bce8_agent%20development%20lifecycle%20loop.png)

The Deploy stage is where an agent moves from a tested workflow into an environment where it needs to do real work safely. For code-running agents, sandboxes provide that boundary: a place to execute code, inspect files, and maintain working state without exposing the host application or production infrastructure.

LangSmith Sandboxes are more useful than standalone sandboxes because they provide out-of-the-box monitoring through LangSmith tracing and evals. The sandbox reduces risk by giving the agent a protected place to run code, while traces show what happened during the run and evals turn failures into test cases for future iterations. That gives teams a way to prevent incidents, debug failures, and make the next version of the agent better.

[Get started with LangSmith Sandboxes](../langsmith/sandboxes.md) through the LangSmith SDK.
