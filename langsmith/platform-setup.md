# Set up LangSmith
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/platform-setup)
Host and manage LangSmith infrastructure for observability, evaluation, and prompt engineering.

Set up **LangSmith** for [observability](https://docs.langchain.com/langsmith/observability), [evaluation](https://docs.langchain.com/langsmith/evaluation), and [prompt engineering](https://docs.langchain.com/langsmith/prompt-context-hub#prompts). LangSmith offers two hosting models: fully managed Cloud, or Self-hosted (Enterprise) for full control.

If you also want to deploy agents in production, you can use [**LangSmith Deployment**](https://docs.langchain.com/langsmith/deployment) with either hosting model.

#### [Cloud](https://docs.langchain.com/langsmith/cloud)
Fully managed observability, evaluation, and prompt engineering.

#### [Self-hosted](https://docs.langchain.com/langsmith/self-hosted)
**(Enterprise)** Full control with observability, evaluation, and prompt engineering in your infrastructure.

> [!NOTE]
> Self-hosted is available on the [Enterprise plan](https://docs.langchain.com/langsmith/pricing-plans). [Get a demo](https://www.langchain.com/contact-sales) to learn more.

## Compare Cloud and Self-hosted

| Feature                                          | **Cloud**                           | **Self-hosted**                      |
| ------------------------------------------------ | ----------------------------------- | ------------------------------------ |
| **Infrastructure location**                      | LangChain's cloud                   | Your infrastructure                  |
| **Who manages updates**                          | LangChain                           | You                                  |
| **Observability data location**                  | LangChain cloud                     | Your infrastructure                  |
| **Pairs with LangSmith Deployment**              | Yes                                 | When you enable LangSmith Deployment |
| **[Pricing](https://www.langchain.com/pricing)** | Plus tier                           | Enterprise                           |
| **Best for**                                     | Quick setup, managed infrastructure | Full control, data isolation         |

Both hosting models support [LangSmith Deployment](https://docs.langchain.com/langsmith/deployment) for agent workloads. Refer to the [LangSmith Deployment overview](https://docs.langchain.com/langsmith/deployment) to pick a topology (Cloud managed, Hybrid, self-hosted with control plane, or standalone).

## Common setups

* **Fastest to start, managed everything.** [LangSmith Cloud](https://docs.langchain.com/langsmith/cloud) paired with [LangSmith Deployment](https://docs.langchain.com/langsmith/deployment) on Cloud. LangChain hosts the platform, and, when you use LangSmith Deployment, also hosts your [Agent Servers](https://docs.langchain.com/langsmith/agent-server).
* **Observability data must stay in your infrastructure.** Self-hosted LangSmith, paired with any LangSmith Deployment topology, including [self-hosted LangSmith Deployment](https://docs.langchain.com/langsmith/deploy-with-control-plane) for agent workloads.
* **Managed observability, agents in your VPC.** LangSmith Cloud paired with [Hybrid](https://docs.langchain.com/langsmith/hybrid) LangSmith Deployment. Traces and evaluations stay on SaaS while agent workloads stay in your infrastructure.
* **Observability only, no agent hosting.** LangSmith Cloud or self-hosted, without LangSmith Deployment. Run your agents wherever you already run apps and send traces to LangSmith.

## Related

#### [Account setup](https://docs.langchain.com/langsmith/admin)
Create an account, manage API keys, and choose a pricing tier.

#### [Plans and pricing](https://www.langchain.com/pricing)
Compare LangSmith plans and tiers.

#### [Observability](https://docs.langchain.com/langsmith/observability)
Trace and monitor your LLM applications.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/platform-setup.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
