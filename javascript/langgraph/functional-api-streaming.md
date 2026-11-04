---
title: "Stream with the Functional API"
description: "Emit custom progress from Functional API entrypoints, or read state snapshots from the values stream."
source: "https://docs.langchain.com/oss/javascript/langgraph/functional-api-streaming"
category: "docs"
tags: [docs, javascript, langgraph, functional-api-streaming]
---

# Stream with the Functional API

> Emit custom progress from Functional API entrypoints, or read state snapshots from the values stream.

Stream from a Functional API [entrypoint](functional-api.md#entrypoint) in two ways. Custom data is a side channel: you push progress with a writer, then read `custom` chunks. Values are state snapshots the runtime records, including the entrypoint return value. You do not call a writer for values.

For concepts, see the [Functional API overview](functional-api.md). For messages and other typed projections, see [event streaming](event-streaming.md).

## Emit custom data

The Functional API uses the same stream as the [Graph API](graph-api.md). Emit with a writer, then consume `custom` chunks. For stream modes, see [Streaming](streaming.md).

```ts
import { entrypoint, MemorySaver } from "@langchain/langgraph";
import type { LangGraphRunnableConfig } from "@langchain/langgraph";

const checkpointer = new MemorySaver();

const main = entrypoint(
  { checkpointer, name: "main" },
  async (
    inputs: { x: number },
    config: LangGraphRunnableConfig,
  ): Promise<number> => {
    config.writer?.("Started processing");
    const result = inputs.x * 2;
    config.writer?.(`Result is ${result}`);
    return result;
  },
);

const config = {
  configurable: { thread_id: "functional-api-stream-custom-data" },
};

const stream = await main.stream(
  { x: 5 },
  { ...config, streamMode: "custom" },
);
for await (const chunk of stream) {
  console.log(chunk);
}
// Started processing
// Result is 10
```

> [card] [View example trace](https://smith.langchain.com/public/a43b8f1e-e11c-48d9-be99-23e2473c0ef4/r)
>
> Open a public LangSmith run for this example.

1. Take `config` as the second argument to the entrypoint.
2. Emit custom data with `config.writer` before and after the computation.
3. Call `stream(..., { streamMode: "custom" })` and iterate the chunks.

## Stream values

Reuse the `main` entrypoint from [Emit custom data](#emit-custom-data). Iterate `stream.values` for state snapshots. For messages and other projections, see [event streaming](event-streaming.md).

```ts
const valuesStream = await main.streamEvents(
  { x: 5 },
  {
    configurable: { thread_id: "functional-api-stream-values" },
    version: "v3",
  },
);
for await (const snapshot of valuesStream.values) {
  console.log(snapshot);
}
// 10
```

## See also

* [Functional API overview](functional-api.md)
* [Build checklist for the Functional API](use-functional-api.md)
* [Event streaming](event-streaming.md)
* [Streaming](streaming.md)
* [Add human-in-the-loop with the Functional API](functional-api-human-in-the-loop.md)

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/functional-api-streaming.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
