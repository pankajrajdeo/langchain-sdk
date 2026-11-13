---
title: "Functional API overview"
description: "Wrap other frameworks with entrypoints and tasks for LangSmith Agent Server. Covers checkpointing, resume rules, and common pitfalls."
source: "https://docs.langchain.com/oss/javascript/langgraph/functional-api"
category: "docs"
tags: [docs, javascript, langgraph, functional-api]
---

# Functional API overview

> Wrap other frameworks with entrypoints and tasks for LangSmith Agent Server. Covers checkpointing, resume rules, and common pitfalls.

The **Functional API** wraps ordinary functions with LangGraph runtime features ([persistence](persistence.md), [memory](add-memory.md), [human-in-the-loop](interrupts.md), and [streaming](streaming.md)). Use it when you already have existing code or are using a different framework and want to [deploy it on LangSmith](../../langsmith/deploy-other-frameworks.md) without rewriting that agent as a graph. Prefer the [Graph API](graph-api.md) for building new agents.

This page is the concept reference for entrypoints, tasks, checkpointing, and resume rules. For the wrap-and-deploy how-to, see [Deploy other frameworks](../../langsmith/deploy-other-frameworks.md).

The Functional API uses two building blocks:

* **`entrypoint`**: Encapsulates workflow logic and manages execution, interrupts, and checkpointing.
* **`task`**: Marks a discrete unit of work (for example, an API call). Tasks return a `Promise` that you await inside the entrypoint.

## When to use the Functional API

| Build | Use |
| - | - |
| New LangGraph agents and workflows | [Graph API](graph-api.md) |
| Existing agent in another framework (Claude Agent SDK, Strands, CrewAI, AutoGen, and similar) that you want on LangSmith Agent Server | Functional API via [Deploy other frameworks](../../langsmith/deploy-other-frameworks.md) |

Compared with the Graph API, the Functional API uses ordinary language control flow (`if` / `else`, loops, and calls), keeps values scoped to the entrypoint and tasks instead of a shared [state](graph-api.md#state) schema, saves task results on the entrypoint checkpoint rather than after each [super-step](graph-api.md#super-steps), and has no static graph visualization.

## Entrypoint

The `entrypoint` function creates a workflow from a function. It manages long-running work and [interrupts](interrupts.md).

### Definition

Pass a [checkpointer](persistence.md) when you need persistence or human-in-the-loop. Identify each run with a `thread_id` in config. A thread is the durable identity for one conversation or workflow run.

An **entrypoint** is created by calling `entrypoint` with configuration and a function.

The function **must accept a single positional argument** as the workflow input. To pass multiple values, use an object as that argument.

The result is a workflow object. Call `invoke` to run it.

```ts
import { MemorySaver, entrypoint } from "@langchain/langgraph";

const checkpointer = new MemorySaver();

const myWorkflow = entrypoint(
  { checkpointer, name: "workflow" },
  async (name: string): Promise<string> => {
    return `Hello, ${name}`;
  }
);

const config = { configurable: { thread_id: "1" } };
await myWorkflow.invoke("Alice", config); // "Hello, Alice"
```

> [!WARNING]
>
> **Serialization**
> Entrypoint **inputs** and **outputs** must be JSON-serializable when a checkpointer is configured. See [Serialization](#serialization).

### Run and resume

Call `invoke` for a final result. For streams, see [Streaming](streaming.md).

Resume after [`interrupt`](https://reference.langchain.com/javascript/langchain-langgraph/index/interrupt) by passing a resume value in [`Command`](https://reference.langchain.com/javascript/langchain-langgraph/index/Command). For recipes, see [Interrupts](interrupts.md).

After an error, resume the same `thread_id` with `null`.

### Short-term memory

When an `entrypoint` has a `checkpointer`, successive invocations on the same **thread id** store state in [checkpoints](checkpointers.md#checkpoints).

Call `getPreviousState` inside the entrypoint. It returns the last value saved on this thread. On the first run it is `undefined`. To save a different value for the next run, use [`entrypoint.final`](https://reference.langchain.com/javascript/langchain-langgraph/index/entrypoint/final).

### Injectable parameters

You can skip this until you add [memory](add-memory.md) or [custom streaming](streaming.md).

The `entrypoint` function can take a second `config` argument. LangGraph also provides helpers you call inside the function:

| Helper | Description |
| - | - |
| **getPreviousState** | The return value from the previous invocation on the same thread (requires a checkpointer). See [short-term memory](#short-term-memory). |
| **config** | A `LangGraphRunnableConfig` object with run-time configuration values. |
| **config.store** | A store instance for [long-term memory](add-memory.md). |
| **config.writer** | A writer for custom streaming. See [Streaming](streaming.md). |

> [accordion] Requesting injectable parameters
>
```ts
> import {
>   MemorySaver,
>   InMemoryStore,
>   entrypoint,
>   getPreviousState,
> } from "@langchain/langgraph";
> import type { LangGraphRunnableConfig } from "@langchain/langgraph";
>
> const checkpointer = new MemorySaver();
> const store = new InMemoryStore();
>
> const myWorkflow = entrypoint(
>   { checkpointer, store, name: "workflow" },
>   async (
>     someInput: Record<string, unknown>,
>     config: LangGraphRunnableConfig
>   ) => {
>     const previous = getPreviousState();
>     const memoryStore = config.store;
>     const writer = config.writer;
>     return { previous, someInput };
>   }
> );
```

## Task

A **task** is a discrete unit of work (for example, an API call or data step). Tasks have two key properties:

* **Concurrent execution**: Calling a task starts it immediately. The entrypoint blocks only when you wait for the result, so independent tasks can overlap.
* **Checkpointing**: Task results are saved so resume can restore them. See [persistence](persistence.md).

### Definition

Define tasks with the `task` function:

```typescript
import { task } from "@langchain/langgraph";

const slowComputation = task("slowComputation", async (inputValue: number) => {
  // Long-running or side-effecting work
  return inputValue * 2;
});
```

> [!WARNING]
>
> **Serialization**: Task **outputs** must be JSON-serializable to support checkpointing.

### Execution

Call **tasks** only from an **entrypoint**, another **task**, or a [Graph API node](graph-api.md#nodes). Do not call them from application code outside the workflow.

Calling a task returns a `Promise`. Await it inside the entrypoint:

```ts
import { MemorySaver, entrypoint, task } from "@langchain/langgraph";

const checkpointer = new MemorySaver();

const slowComputation = task("slowComputation", async (inputValue: number) => {
  return inputValue * 2;
});

const myWorkflow = entrypoint(
  { checkpointer, name: "workflow" },
  async (someInput: number): Promise<number> => {
    return await slowComputation(someInput);
  }
);
```

### When to use a task

Use **tasks** when you need:

* **Checkpointing**: Save a long-running result so resume does not recompute it.
* **Human-in-the-loop**: Wrap work you should not redo after a pause in a task, for example an LLM call. Resume after an [interrupt](interrupts.md) restores the result. For randomness, see [Determinism](#determinism).
* **Parallel execution**: Run independent I/O-bound work concurrently.
* **Observability**: Track discrete steps in [LangSmith](../../langsmith/observability.md).
* **Retries**: Apply retry policies to discrete units of work. See [Fault tolerance](fault-tolerance.md).

## Resume and checkpointing

Resume replay depends on serialization, determinism, and idempotency.

### Serialization

Two rules apply when a checkpointer is configured:

1. `entrypoint` inputs and outputs must be JSON-serializable.
2. `task` outputs must be JSON-serializable.

Use primitives such as objects, arrays, strings, numbers, and booleans.

Serialization is what makes task results and intermediate values restorable for human-in-the-loop, fault tolerance, and parallel execution. Non-serializable values raise a runtime error when a checkpointer is configured.

### Determinism

Resume does **not** continue from the exact line where execution stopped. Execution returns to a checkpoint boundary and **replays** forward until it hits the pause again.

For the Functional API, replay starts at the beginning of the **entrypoint**. LangGraph restores completed [**task**](#task) and [**subgraph**](use-subgraphs.md) results from the checkpointer instead of recomputing them. That preserves step order across pauses, including for long-running or non-deterministic **task** outputs.

For **human-in-the-loop**, put non-deterministic work (for example, random values) and side effects (for example, file writes or API calls) in [**tasks**](#task).

Different runs can produce different results. Resuming a **specific** thread should replay the same persisted **task** and **subgraph** results.

Guidelines:

* **Avoid repeating work**: Give each side effect in an entrypoint its own **task** so resume restores outputs instead of re-running them.
* **Encapsulate non-deterministic operations**: Keep values that change between attempts (random numbers, wall-clock time) inside **tasks**.
* **Use idempotent operations**: For partial failures and retries, see [Idempotency](#idempotency).

### Idempotency

Idempotency means running the same operation more than once has the same effect as running it once. Place API calls and other writes inside **tasks**, and design those tasks to be safe if they run again.

On resume, LangGraph restores completed **task** results. A **task** that started but did not finish may run again, so use idempotency keys or check existing results before writing.

## Pause for human review

This workflow writes an essay and [interrupts](interrupts.md) for human review:

```ts
import { MemorySaver, entrypoint, task, interrupt } from "@langchain/langgraph";

const writeEssay = task("writeEssay", async (topic: string) => {
  // Placeholder for a long-running task.
  await new Promise((resolve) => setTimeout(resolve, 1000));
  return `An essay about topic: ${topic}`;
});

const workflow = entrypoint(
  { checkpointer: new MemorySaver(), name: "workflow" },
  async (topic: string) => {
    const essay = await writeEssay(topic);
    const isApproved = interrupt({
      // Any JSON-serializable payload. Surfaces as an Interrupt when streaming.
      essay,
      action: "Please approve/reject the essay",
    });

    return {
      essay,
      isApproved,
    };
  }
);
```

Invoke with a topic such as `"cat"`. The run writes the essay, then pauses at `interrupt`. The pause can last indefinitely. Resume starts at the beginning of the entrypoint.

The `writeEssay` task result is restored, not recomputed.

For stream, resume, and tool-call review, see [Interrupts](interrupts.md).

## Common pitfalls

### Handling side effects

Put side effects (writing a file, sending an email) in tasks so resume does not run them again.

> [tab] Incorrect
>
> The file write runs in the entrypoint, so resume executes it a second time.
>
```typescript
> import { MemorySaver, entrypoint, interrupt } from "@langchain/langgraph";
> import fs from "fs";
>
> const checkpointer = new MemorySaver();
>
> const myWorkflow = entrypoint(
>   { checkpointer, name: "workflow" },
>   async (inputs: Record<string, any>) => {
>     // Runs again on resume.
>     fs.writeFileSync("output.txt", "Side effect executed");
>     const value = interrupt("question");
>     return value;
>   }
> );
```

> [tab] Correct
>
> The side effect lives in a task, so resume restores the checkpointed result.
>
```typescript
> import { MemorySaver, entrypoint, task, interrupt } from "@langchain/langgraph";
> import * as fs from "fs";
>
> const checkpointer = new MemorySaver();
>
> const writeToFile = task("writeToFile", async () => {
>   fs.writeFileSync("output.txt", "Side effect executed");
> });
>
> const myWorkflow = entrypoint(
>   { checkpointer, name: "workflow" },
>   async (inputs: Record<string, any>) => {
>     await writeToFile();
>     const value = interrupt("question");
>     return value;
>   }
> );
```

### Non-deterministic control flow

Encapsulate time and randomness in tasks so resume returns the same values.

* In a task: Get random number (5) → interrupt → resume → (returns 5 again) → ...
* Not in a task: Get random number (5) → interrupt → resume → get new random number (7) → ...

With multiple [`interrupt`](https://reference.langchain.com/javascript/langchain-langgraph/index/interrupt) calls, LangGraph matches resume values **by index** to each interrupt. If resume changes the order of interrupts, a resume value can attach to the wrong interrupt. See [Determinism](#determinism).

> [tab] Incorrect
>
> Reading the clock in the entrypoint can change which branch runs on resume.
>
```typescript
> import { MemorySaver, entrypoint, task, interrupt } from "@langchain/langgraph";
>
> const checkpointer = new MemorySaver();
>
> const slowTask = task("slowTask", async (x: number) => x);
>
> const myWorkflow = entrypoint(
>   { checkpointer, name: "workflow" },
>   async (inputs: { t0: number }) => {
>     const t1 = Date.now();
>
>     const deltaT = t1 - inputs.t0;
>
>     if (deltaT > 1000) {
>       const result = await slowTask(1);
>       const value = interrupt("question");
>       return { result, value };
>     } else {
>       const result = await slowTask(2);
>       const value = interrupt("question");
>       return { result, value };
>     }
>   }
> );
```

> [tab] Correct
>
> Read the clock inside a task so resume restores the same timestamp and branch.
>
```typescript
> import { MemorySaver, entrypoint, task, interrupt } from "@langchain/langgraph";
>
> const checkpointer = new MemorySaver();
>
> const slowTask = task("slowTask", async (x: number) => x);
> const getTime = task("getTime", async () => Date.now());
>
> const myWorkflow = entrypoint(
>   { checkpointer, name: "workflow" },
>   async (inputs: { t0: number }) => {
>     const t1 = await getTime();
>
>     const deltaT = t1 - inputs.t0;
>
>     if (deltaT > 1000) {
>       const result = await slowTask(1);
>       const value = interrupt("question");
>       return { result, value };
>     } else {
>       const result = await slowTask(2);
>       const value = interrupt("question");
>       return { result, value };
>     }
>   }
> );
```

## Learn more

* [Deploy other frameworks](../../langsmith/deploy-other-frameworks.md)
* [Graph API overview](graph-api.md)
* [Interrupts](interrupts.md)
* [Streaming](streaming.md)
* [Fault tolerance](fault-tolerance.md)
* [Memory](add-memory.md)

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/functional-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
