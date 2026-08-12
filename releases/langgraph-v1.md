# What's new in LangGraph v1
> Source: [Original LangChain documentation](https://docs.langchain.com/oss/python/releases/langgraph-v1)
**LangGraph v1 is a stability-focused release for the agent runtime.** It keeps the core graph APIs and execution model unchanged, while refining type safety, docs, and developer ergonomics.

It's designed to work hand-in-hand with [LangChain v1](https://docs.langchain.com/oss/python/releases/langchain-v1) (whose `create_agent` is built on LangGraph) so you can start high-level and drop down to granular control when needed.

#### Stable core APIs
Graph primitives (state, nodes, edges) and the execution/runtime model are unchanged, making upgrades straightforward.

#### Reliability, by default
Durable execution with checkpointing, persistence, streaming, and human-in-the-loop continues to be first-class.

#### Seamless with LangChain v1
LangChain's `create_agent` runs on LangGraph. Use LangChain for a fast start; drop to LangGraph for custom orchestration.

To upgrade,

```bash
pip install -U langgraph
```

```bash
uv add langgraph
```

## Deprecation of `create_react_agent`

The LangGraph [`create_react_agent`](https://reference.langchain.com/python/langchain-classic/agents/react/agent/create_react_agent) prebuilt has been deprecated in favor of LangChain's [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent). It provides a simpler interface, and offers greater customization potential through the introduction of middleware.

* For information on the new [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) API, see the [LangChain v1 release notes](https://docs.langchain.com/oss/python/releases/langchain-v1#create_agent).
* For information on migrating from [`create_react_agent`](https://reference.langchain.com/python/langchain-classic/agents/react/agent/create_react_agent) to [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent), see the [LangChain v1 migration guide](https://docs.langchain.com/oss/python/migrate/langchain-v1#migrate-to-create_agent).

## Reporting issues

Please report any issues discovered with 1.0 on [GitHub](https://github.com/langchain-ai/langgraph/issues) using the [`'v1'` label](https://github.com/langchain-ai/langgraph/issues?q=state%3Aopen%20label%3Av1).

## Additional resources

#### [LangGraph 1.0](https://blog.langchain.com/langchain-langchain-1-0-alpha-releases/)
Read the announcement

#### [Overview](https://docs.langchain.com/oss/python/langgraph/overview)
What LangGraph is and when to use it

#### [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api)
Build graphs with state, nodes, and edges

#### [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents)
High-level agents built on LangGraph

#### [Migration guide](https://docs.langchain.com/oss/python/migrate/langgraph-v1)
How to migrate to LangGraph v1

#### [GitHub](https://github.com/langchain-ai/langgraph)
Report issues or contribute

## See also

* [Versioning](https://docs.langchain.com/oss/python/versioning) – Understanding version numbers
* [Release policy](https://docs.langchain.com/oss/python/release-policy) – Detailed release policies

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/releases/langgraph-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
