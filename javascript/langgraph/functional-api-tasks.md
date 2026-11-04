---
title: "Configure Functional API tasks"
description: "Add retries, timeouts, caching, and error recovery to Functional API tasks and entrypoints."
source: "https://docs.langchain.com/oss/javascript/langgraph/functional-api-tasks"
category: "docs"
tags: [docs, javascript, langgraph, functional-api-tasks]
---

# Configure Functional API tasks

> Add retries, timeouts, caching, and error recovery to Functional API tasks and entrypoints.

A [task](functional-api.md#task) is a discrete unit of work whose result can be [checkpointed](persistence.md) on its own. When an [entrypoint](functional-api.md#entrypoint) or a [Graph API node](graph-api.md#using-tasks-in-nodes) runs several operations, wrap each operation in a task instead of putting all the work in one function body. With a checkpointer, completed task results are saved, so a resumed thread can skip finished work and continue from the next task.

This page covers retries, timeouts, caching, and error recovery on tasks. For concepts, see the [Functional API overview](functional-api.md). For an ordered build path, see the [Build checklist for the Functional API](use-functional-api.md). For the shared retry and timeout lifecycle, see [Fault tolerance](fault-tolerance.md).

## Add a retry policy

Pass `retry` on `task` (not `retryPolicy`). Retries are opt-in. If the policy omits `retryOn`, LangGraph retries most thrown errors except abort/cancel, `GraphValueError`, aborted connections, selected HTTP 4xx statuses, and OpenAI-style quota errors. This example retries any `Error`. See [Fault tolerance](fault-tolerance.md#retries) for the full default list.

```ts
import { entrypoint, task } from "@langchain/langgraph";
import type { RetryPolicy } from "@langchain/langgraph";

// Used only to simulate a transient failure. Do not use a variable like this in production.
let attempts = 0;

const retryPolicy: RetryPolicy = {
  retryOn: (error) => error instanceof Error,
};

const getInfo = task({ name: "getInfo", retry: retryPolicy }, () => {
  attempts += 1;

  if (attempts < 2) {
    throw new Error("Failure");
  }
  return "OK";
});

const main = entrypoint({ name: "main" }, async (inputs: Record<string, unknown>) => {
  return await getInfo();
});

console.log(await main.invoke({ any_input: "foobar" }));
// 'OK'
```

## Set a timeout

Cap how long a single async attempt can run. If a retry policy retries the timeout error, the timer resets on the next attempt.

Pass `timeout` on `task` or `entrypoint` in milliseconds, or as `{ idleTimeout: 30_000 }`. Use `isNodeTimeoutError` to narrow timeout errors. `NodeTimeoutError` is retryable when a retry policy is set.

The first attempt sleeps past the timeout. The retry policy retries. The second attempt returns immediately.

```ts
import { entrypoint, task } from "@langchain/langgraph";

let attempts = 0;

const callApi = task(
  {
    name: "callApi",
    timeout: 1_000,
    retry: { maxAttempts: 3 },
  },
  async (url: string) => {
    attempts += 1;
    if (attempts < 2) {
      await new Promise((resolve) => setTimeout(resolve, 2_000));
    }
    return `result from ${url}`;
  }
);

const workflow = entrypoint(
  { name: "workflow", timeout: 5_000 },
  async (inputs: { url: string }) => {
    return await callApi(inputs.url);
  }
);

console.log(await workflow.invoke({ url: "https://example.com" }));
// 'result from https://example.com'
```

## Cache a task

Cache a task result by input. Pass a cache on the [entrypoint](functional-api.md#entrypoint) and a policy on the task. `ttl` is in seconds. The second call is a cache hit, so this run takes about 1 second, not 2.

```ts
import { entrypoint, task } from "@langchain/langgraph";
import { InMemoryCache } from "@langchain/langgraph-checkpoint";

const slowAdd = task(
  {
    name: "slowAdd",
    cache: { ttl: 120 },  // [!code highlight]
  },
  async (x: number) => {
    await new Promise((resolve) => setTimeout(resolve, 1000));
    return x * 2;
  }
);

const main = entrypoint(
  { cache: new InMemoryCache(), name: "main" },
  async (inputs: { x: number }) => {
    const result1 = await slowAdd(inputs.x);
    const result2 = await slowAdd(inputs.x);
    return { result1, result2 };
  }
);

console.log(await main.invoke({ x: 5 }));
// { result1: 10, result2: 10 }
```

## Resume after an error

A [checkpointer](persistence.md) is required so completed task results survive the failed run.

`slow_task` is restored from the checkpoint. `get_info` runs again and returns `"OK"`. The entrypoint still returns the `slow_task` result.

Resume the same `thread_id` with `null`.

```ts
import { entrypoint, task, MemorySaver } from "@langchain/langgraph";

// Used only to simulate a transient failure. Do not use a variable like this in production.
let attempts = 0;

const getInfo = task("getInfo", async () => {
  attempts += 1;

  if (attempts < 2) {
    throw new Error("Failure");
  }
  return "OK";
});

const checkpointer = new MemorySaver();

const slowTask = task("slowTask", async () => {
  await new Promise((resolve) => setTimeout(resolve, 1000));
  return "Ran slow task.";
});

const main = entrypoint(
  { checkpointer, name: "main" },
  async (inputs: Record<string, unknown>) => {
    const slowTaskResult = await slowTask();
    await getInfo(); // throws on the first run
    return slowTaskResult;
  }
);

const config = {
  configurable: {
    thread_id: "1",
  },
};

try {
  await main.invoke({ any_input: "foobar" }, config);
} catch (err) {
  // First run fails in getInfo.
}

console.log(await main.invoke(null, config));
// 'Ran slow task.'
```

## See also

* [Functional API overview](functional-api.md)
* [Build checklist for the Functional API](use-functional-api.md)
* [Fault tolerance](fault-tolerance.md)
* [Stream with the Functional API](functional-api-streaming.md)
* [Add memory with the Functional API](functional-api-memory.md)

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/functional-api-tasks.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
