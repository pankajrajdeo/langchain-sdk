# LangSmith Evaluation
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/evaluation)
Evaluate and test agent quality at scale with datasets, evaluators, prompts, and Studio.

LangSmith's testing tools help you measure agent quality, iterate on prompts, and debug live in an interactive environment. Evaluation is the core of testing: it scores your agent's outputs against datasets and criteria so you can benchmark versions, catch regressions, and track quality over time.

LangSmith supports two types of evaluation based on when and where they run:

#### Offline Evaluation
**Test before you ship**

Run evaluations on curated datasets during development to compare versions, benchmark performance, and catch regressions.

#### Online Evaluation
**Monitor in production**

Evaluate real user interactions in real-time to detect issues and measure quality on live traffic.

## Set up your account

### Create an account
Sign up at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-langsmith-account-api-key-quickstart) (no credit card required).
You can log in with **Google**, **GitHub**, or **email**.

### Create an API key
Go to your [Settings page](https://smith.langchain.com/settings) → **API Keys** → **Create API Key**.
Copy the key and save it securely.

Once your account and API key are ready, [run your first evaluation](https://docs.langchain.com/langsmith/evaluation-quickstart).

## Evaluation workflow

#### Offline evaluation flow
### Create a dataset
Create a [dataset](https://docs.langchain.com/langsmith/manage-datasets) with [examples](https://docs.langchain.com/langsmith/evaluation-concepts#examples) from manually curated test cases, historical production traces, or synthetic data generation.

### Define evaluators
Create [evaluators](https://docs.langchain.com/langsmith/evaluation-concepts#evaluators) to score performance:

* [Human](https://docs.langchain.com/langsmith/evaluation-concepts#human) review
* [Code](https://docs.langchain.com/langsmith/evaluation-concepts#code) rules
* [LLM-as-judge](https://docs.langchain.com/langsmith/llm-as-judge)
* [Pairwise](https://docs.langchain.com/langsmith/evaluate-pairwise) comparison

### Run an experiment
Execute your application on the dataset to create an [experiment](https://docs.langchain.com/langsmith/evaluation-concepts#experiment). Configure [repetitions, concurrency, and caching](https://docs.langchain.com/langsmith/experiment-configuration) to optimize runs.

### Analyze results
Compare experiments for [benchmarking](https://docs.langchain.com/langsmith/evaluation-types#benchmarking), [unit tests](https://docs.langchain.com/langsmith/evaluation-types#unit-tests), [regression tests](https://docs.langchain.com/langsmith/evaluation-types#regression-tests), or [backtesting](https://docs.langchain.com/langsmith/evaluation-types#backtesting).

#### Online evaluation flow
### Deploy your application
Each interaction creates a [run](https://docs.langchain.com/langsmith/evaluation-concepts#runs) without reference outputs.

### Configure online evaluators
Set up [evaluators](https://docs.langchain.com/langsmith/online-evaluations-llm-as-judge) to run automatically on production traces: safety checks, format validation, quality heuristics, and reference-free LLM-as-judge. Apply [filters and sampling rates](https://docs.langchain.com/langsmith/online-evaluations-llm-as-judge#configure-a-sampling-rate) to control costs.

### Monitor in real-time
Evaluators run automatically on [runs](https://docs.langchain.com/langsmith/evaluation-concepts#runs) or [threads](https://docs.langchain.com/langsmith/online-evaluations-multi-turn), providing real-time monitoring, anomaly detection, and alerting.

### Establish a feedback loop
Add failing production traces to your [dataset](https://docs.langchain.com/langsmith/manage-datasets), create targeted evaluators, validate fixes with offline experiments, and redeploy.

> [!TIP]
> For more on the differences between offline and online evaluation, refer to the [Evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts#quick-reference-offline-vs-online-evaluation) page.

## Get started

#### [Evaluation quickstart](https://docs.langchain.com/langsmith/evaluation-quickstart)
Get started with offline evaluation.

#### [Manage datasets](https://docs.langchain.com/langsmith/manage-datasets)
Create and manage datasets for evaluation through the UI or SDK.

#### [Run offline evaluations](https://docs.langchain.com/langsmith/evaluate-llm-application)
Explore evaluation types, techniques, and frameworks for comprehensive testing.

#### [Analyze results](https://docs.langchain.com/langsmith/analyze-an-experiment)
View and analyze evaluation results, compare experiments, filter data, and export findings.

#### [Run online evaluations](https://docs.langchain.com/langsmith/online-evaluations-llm-as-judge)
Monitor production quality in real-time from the Observability tab.

#### [Follow tutorials](https://docs.langchain.com/langsmith/evaluate-chatbot-tutorial)
Learn by following step-by-step tutorials, from simple chatbots to complex agent evaluations.

#### [Studio](https://docs.langchain.com/langsmith/studio)
Use an interactive environment for developing and debugging agents.

> [!NOTE]
> To set up a LangSmith instance, visit the [Platform setup section](https://docs.langchain.com/langsmith/platform-setup) to choose between cloud, hybrid, or self-hosted. All options include observability, evaluation, prompt engineering, and deployment.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
