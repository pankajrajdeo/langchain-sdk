# Set up LangSmith
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/platform-setup)
Host and manage LangSmith infrastructure for observability, evaluation, and prompt engineering.

Set up **LangSmith** for [observability](observability.md), [evaluation](evaluation.md), and [prompt engineering](prompt-context-hub.md#prompts). LangSmith offers two hosting models: fully managed Cloud, or Self-hosted (Enterprise) for full control.

If you also want to deploy agents in production, you can use [**LangSmith Deployment**](deployment.md) with either hosting model.

#### [Cloud](cloud.md)
Fully managed observability, evaluation, and prompt engineering.

#### [Self-hosted](self-hosted.md)
**(Enterprise)** Full control with observability, evaluation, and prompt engineering in your infrastructure.

> [!NOTE]
> Self-hosted is available on the [Enterprise plan](pricing-plans.md). [Get a demo](https://www.langchain.com/contact-sales) to learn more.

## Compare Cloud and Self-hosted

| Feature                                          | **Cloud**                           | **Self-hosted**                      |
| ------------------------------------------------ | ----------------------------------- | ------------------------------------ |
| **Infrastructure location**                      | LangChain's cloud                   | Your infrastructure                  |
| **Who manages updates**                          | LangChain                           | You                                  |
| **Observability data location**                  | LangChain cloud                     | Your infrastructure                  |
| **Pairs with LangSmith Deployment**              | Yes                                 | When you enable LangSmith Deployment |
| **[Pricing](https://www.langchain.com/pricing)** | Plus tier                           | Enterprise                           |
| **Best for**                                     | Quick setup, managed infrastructure | Full control, data isolation         |

Both hosting models support [LangSmith Deployment](deployment.md) for agent workloads. Refer to the [LangSmith Deployment overview](deployment.md) to pick a topology (Cloud managed, Hybrid, self-hosted with control plane, or standalone).

## Common setups

* **Fastest to start, managed everything.** [LangSmith Cloud](cloud.md) paired with [LangSmith Deployment](deployment.md) on Cloud. LangChain hosts the platform, and, when you use LangSmith Deployment, also hosts your [Agent Servers](agent-server.md).
* **Observability data must stay in your infrastructure.** Self-hosted LangSmith, paired with any LangSmith Deployment topology, including [self-hosted LangSmith Deployment](deploy-with-control-plane.md) for agent workloads.
* **Managed observability, agents in your VPC.** LangSmith Cloud paired with [Hybrid](hybrid.md) LangSmith Deployment. Traces and evaluations stay on SaaS while agent workloads stay in your infrastructure.
* **Observability only, no agent hosting.** LangSmith Cloud or self-hosted, without LangSmith Deployment. Run your agents wherever you already run apps and send traces to LangSmith.

## Related

#### [Account setup](admin.md)
Create an account, manage API keys, and choose a pricing tier.

#### [Plans and pricing](https://www.langchain.com/pricing)
Compare LangSmith plans and tiers.

#### [Observability](observability.md)
Trace and monitor your LLM applications.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/platform-setup.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
