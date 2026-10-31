---
title: "LangSmith Evaluation"
description: "Evaluate and test agent quality at scale with datasets, evaluators, prompts, and Studio."
source: "https://docs.langchain.com/langsmith/evaluation"
category: "docs"
tags: [docs, langsmith, evaluation]
---

# LangSmith Evaluation

> Evaluate and test agent quality at scale with datasets, evaluators, prompts, and Studio.

LangSmith's testing tools help you measure agent quality, iterate on prompts, and debug live in an interactive environment. Evaluation is the core of testing: it scores your agent's outputs against datasets and criteria so you can benchmark versions, catch regressions, and track quality over time.

Add real traces to a dataset so a failure you saw once becomes a test you run every time.

LangSmith supports two types of evaluation based on when and where they run:

> [card] Offline Evaluation
>
> **Test before you ship**
>
> Run evaluations on curated datasets during development to compare versions, benchmark performance, and catch regressions.

> [card] Online Evaluation
>
> **Monitor in production**
>
> Evaluate real user interactions in real-time to detect issues and measure quality on live traffic.

## Set up your account

**1. Create an account**

Sign up at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-langsmith-account-api-key-quickstart) (no credit card required).
You can log in with **Google**, **GitHub**, or **email**.

**2. Create an API key**

Go to your [Settings page](https://smith.langchain.com/settings) > **API Keys** > **Create API Key**.
Copy the key and save it securely.

Once your account and API key are ready, [run your first evaluation](evaluation-quickstart.md).

## Evaluation workflow

> [tab] Offline evaluation flow
>
> **1. Create a dataset**
>
> Create a [dataset](manage-datasets.md) with [examples](evaluation-concepts.md#examples) (Individual test cases with inputs and reference outputs) from manually curated test cases, historical production traces, or synthetic data generation.
>
> **2. Define evaluators**
>
> Create [evaluators](evaluation-concepts.md#evaluators) (Functions that score how well your application performs) to score performance:
>
> * [Human](evaluation-concepts.md#human) review
> * [Code](evaluation-concepts.md#code) rules
> * [LLM-as-judge](llm-as-judge.md)
> * [Pairwise](evaluate-pairwise.md) comparison
>
> **3. Run an experiment**
>
> Execute your application on the dataset to create an [experiment](evaluation-concepts.md#experiment) (Results of evaluating a specific application version on a dataset). Configure [repetitions, concurrency, and caching](experiment-configuration.md) to optimize runs.
>
> **4. Analyze results**
>
> Compare experiments for [benchmarking](evaluation-types.md#benchmarking), [unit tests](evaluation-types.md#unit-tests), [regression tests](evaluation-types.md#regression-tests), or [backtesting](evaluation-types.md#backtesting).

> [tab] Online evaluation flow
>
> **1. Deploy your application**
>
> Each interaction creates a [run](evaluation-concepts.md#runs) (A single execution trace including inputs, outputs, and intermediate steps) without reference outputs.
>
> **2. Configure online evaluators**
>
> Set up [evaluators](online-evaluations-llm-as-judge.md) to run automatically on production traces: safety checks, format validation, quality heuristics, and reference-free LLM-as-judge. Apply [filters and sampling rates](online-evaluations-llm-as-judge.md#configure-a-sampling-rate) to control costs.
>
> **3. Monitor in real-time**
>
> Evaluators run automatically on [runs](evaluation-concepts.md#runs) or [threads](online-evaluations-multi-turn.md) (Collections of related runs forming multi-turn conversations), providing real-time monitoring, anomaly detection, and alerting.
>
> **4. Establish a feedback loop**
>
> Add failing production traces to your [dataset](manage-datasets.md), create targeted evaluators, validate fixes with offline experiments, and redeploy.

> [!TIP]
>
> For more on the differences between offline and online evaluation, refer to the [Evaluation concepts](evaluation-concepts.md#quick-reference-offline-vs-online-evaluation) page.

## Get started

> [card] [Evaluation quickstart](evaluation-quickstart.md)
>
> Get started with offline evaluation.

> [card] [Manage datasets](manage-datasets.md)
>
> Create and manage datasets for evaluation through the UI or SDK.

> [card] [Run offline evaluations](evaluate-llm-application.md)
>
> Explore evaluation types, techniques, and frameworks for comprehensive testing.

> [card] [Analyze results](analyze-an-experiment.md)
>
> View and analyze evaluation results, compare experiments, filter data, and export findings.

> [card] [Run online evaluations](online-evaluations-llm-as-judge.md)
>
> Monitor production quality in real-time from the Observability tab.

> [card] [Follow tutorials](evaluate-chatbot-tutorial.md)
>
> Learn by following step-by-step tutorials, from simple chatbots to complex agent evaluations.

> [card] [Studio](studio.md)
>
> Use an interactive environment for developing and debugging agents.

> [!NOTE]
>
> To set up a LangSmith instance, visit the [Platform setup section](platform-setup.md) to choose between cloud, hybrid, or self-hosted. All options include observability, evaluation, prompt engineering, and deployment.

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
