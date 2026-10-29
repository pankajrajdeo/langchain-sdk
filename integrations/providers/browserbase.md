---
title: "Browserbase integrations"
description: "Integrate with Browserbase using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/browserbase"
category: "docs"
tags: [docs, integrations, providers, browserbase]
---

# Browserbase integrations

> Integrate with Browserbase using LangChain Python.

[Browserbase](https://www.browserbase.com) runs cloud browsers for agents, with [session recordings](https://docs.browserbase.com/platform/browser/observability/observability) and a [live view](https://docs.browserbase.com/platform/browser/observability/session-live-view) for debugging. The same API key covers [Search](https://docs.browserbase.com/platform/search/overview) and [Fetch](https://docs.browserbase.com/platform/fetch/overview), which find and read pages without starting a browser session.

This page covers using Browserbase with [Deep Agents](../../deepagents/overview.md): a Stagehand-driven cloud browser, plus Search and Fetch as agent tools.

## Installation and setup

Get an API key from [Browserbase](https://www.browserbase.com) and set it as an environment variable:

```bash
export BROWSERBASE_API_KEY="your-browserbase-api-key"
```

Install the [Browserbase Python SDK](https://github.com/browserbase/sdk-python):

**pip**

```bash
pip install "browserbase>=1.21.0"
```

**uv**

```bash
uv add "browserbase>=1.21.0"
```

## Deep Agents

A [deep agent](../../deepagents/overview.md) can use Browserbase in two ways: a cloud browser that it drives through Stagehand tools, and Search and Fetch tools for pages that do not need a browser. For when to give an agent a browser, see [Browser use](../../deepagents/browser-use.md).

### Browser tools with Stagehand

The [Stagehand integration](../tools/stagehand.md) adds `run`, `snapshot`, and `screenshot` through native Python middleware. Pass a configured Stagehand client to `StagehandMiddleware`, then include it in your agent's `middleware` list. No MCP server or custom browser system prompt is needed.

Your application owns the browser and can keep it open across runs to reuse tabs and logins. For installation, a complete agent, and cleanup, see [Use with a deep agent](../tools/stagehand.md#use-with-a-deep-agent). For session isolation, see [Choose a browser scope](../../deepagents/browser-use.md#choose-a-browser-scope).

### Search and fetch tools

Expose Search and Fetch as agent tools. Those APIs find and read pages without starting a browser session. Fetch does not execute JavaScript.

Install the agent packages and set the model-provider credential before running this example:

**pip**

```bash
pip install "browserbase>=1.21.0" deepagents langchain-openai
```

**uv**

```bash
uv add "browserbase>=1.21.0" deepagents langchain-openai
```

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

The example uses OpenAI's [GPT-5.5 snapshot](https://developers.openai.com/api/docs/models/gpt-5.5). Omit `provider` on `search.web` to use your project's default search provider:

```python
import os

from browserbase import Browserbase
from deepagents import create_deep_agent
from langchain.tools import tool

bb = Browserbase(api_key=os.environ["BROWSERBASE_API_KEY"])

@tool
def web_search(query: str) -> str:
    """Search the web and return result titles and URLs."""
    response = bb.search.web(query=query, num_results=5)
    return "\n".join(f"{result.title}: {result.url}" for result in response.results)

@tool
def fetch_page(url: str) -> str:
    """Fetch a page as markdown without opening a browser."""
    return bb.fetch_api.create(url=url, format="markdown").content

agent = create_deep_agent(
    model="openai:gpt-5.5-2026-04-23",
    tools=[web_search, fetch_page],
    system_prompt="Search to find pages, then fetch the pages you need to read.",
)
```

For a complete example that combines Search, Fetch, and Stagehand, see Browserbase's [Deep Agents guide](https://docs.browserbase.com/integrations/langchain/deepagents).

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/browserbase.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
