> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Kùzu integrations

> Integrate with Kùzu using LangChain Python.

> [Kùzu](https://kuzudb.com/) is an embeddable, scalable, extremely fast graph database.
> It is permissively licensed with an MIT license, and you can see its source code on [GitHub](https://github.com/kuzudb/kuzu).

> Key characteristics of Kùzu:
>
> * Performance and scalability: Implements modern, state-of-the-art join algorithms for graphs.
> * Usability: Very easy to set up and get started with, as there are no servers (embedded architecture).
> * Interoperability: Can conveniently scan and copy data from external columnar formats, CSV, JSON and relational databases.
> * Structured property graph model: Implements the property graph model, with added structure.
> * Cypher support: Allows convenient querying of the graph in Cypher, a declarative query language.

> Get started with Kùzu by visiting their [documentation](https://docs.kuzudb.com/).

## Installation and setup

Install the Python SDK as follows:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain-kuzu
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-kuzu
  ```
</CodeGroup>

## Usage

## Graphs

See a [usage example](/oss/python/integrations/graphs/kuzu_db).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_kuzu.graphs.kuzu_graph import KuzuGraph
```

## Chains

See a [usage example](/oss/python/integrations/graphs/kuzu_db/#creating-kuzuqachain).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_kuzu.chains.graph_qa.kuzu import KuzuQAChain
```

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/kuzu.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
