---
title: "Microsoft integrations"
description: "Integrate with Microsoft using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/microsoft"
category: "docs"
tags: [docs, integrations, providers, microsoft]
---

# Microsoft integrations

> Integrate with Microsoft using LangChain Python.

Browse common LangChain Python integrations with [Microsoft Azure](https://portal.azure.com) and other [Microsoft](https://www.microsoft.com) products. For package selection, shared Azure setup, memory, vector stores, and hosted agents, see [Azure AI integrations](azure_ai.md).

> [!TIP]
>
> **Recommended: Microsoft Foundry**
>
> For new LangChain or LangGraph applications centered on [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/), start with [`langchain-azure-ai`](azure_ai.md). It adds Foundry project endpoints, Azure credential integration, Agent Service, hosting, tools, Content Safety, retrieval, and Azure observability.
>
> For direct [Azure OpenAI v1 API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?tabs=python) model access, code that switches between OpenAI and Azure, traditional Azure OpenAI API versions, completion LLMs, or a smaller dependency surface, use the `langchain-openai` package.

> [!NOTE]
>
> **Claude on Azure**
>
> Microsoft Foundry also offers access to all [Anthropic Claude models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude), including Opus, Sonnet, and Haiku. Claude models are served through a dedicated Anthropic-native endpoint rather than the Azure OpenAI v1 API. Prefer `AzureAIAnthropicChatModel` from `langchain-azure-ai` for Foundry project endpoints and Microsoft Entra ID. You can also use [`ChatAnthropic`](../chat/anthropic.md) from `langchain-anthropic` pointed at your Foundry Anthropic endpoint.

## Explore integrations

### Use models

> [card] [Microsoft Foundry chat models](../chat/azure_ai.md)

> [card] [Azure OpenAI chat](../chat/azure_chat_openai.md)

> [card] [Azure OpenAI LLMs](../llms/azure_openai.md)

> [card] [Microsoft Foundry embeddings](azure_ai.md#microsoft-foundry-embeddings)

> [card] [AzureOpenAIEmbeddings](../embeddings/azure_openai.md)

### Persist history and cache responses

> [card] [Azure Cosmos DB chat message history](azure_ai.md#azure-cosmos-db-chat-message-history)

> [card] [Azure Cosmos DB semantic cache](azure_ai.md#azure-cosmos-db-semantic-cache)

### Load and retrieve data

> [card] [Azure Blob Storage](../document_loaders/azure_blob_storage.md)

> [card] [Azure Cosmos DB for MongoDB vCore](../vectorstores/azure_cosmos_db_mongo_vcore.md)

> [card] [Azure Cosmos DB NoSQL](../vectorstores/azure_cosmos_db_no_sql.md)

> [card] [Azure Database for PostgreSQL](../vectorstores/azure_db_for_postgresql.md)

> [card] [PGVector](../vectorstores/pgvector.md)

> [card] [Azure SQL Database](azure_ai.md#azure-sql-database)

### Use Deep Agents

> [card] [Azure Blob Storage Backend](azure_ai.md#azure-blob-storage-backend)

### Build and deploy agents

> [card] [Microsoft Foundry middleware](../middleware/azure_ai.md)

> [card] [Microsoft Foundry tools](../tools/azure_ai.md)

> [card] [Microsoft Foundry service tools](../tools/azure_ai_services.md)

> [card] [Azure Container Apps Dynamic Sessions](../tools/azure_dynamic_sessions.md)

> [card] [Azure Logic Apps](../tools/azure_logic_apps.md)

> [card] [Microsoft Foundry hosted agents](azure_ai.md#microsoft-foundry-hosted-agents)

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/microsoft.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
