---
title: "Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE"
description: "Documentation for LangSmith, Fleet, and our open source packages."
source: "https://docs.langchain.com/_llms/agent-development-lifecycle"
category: "docs"
tags: [docs, llms, agent-development-lifecycle]
---

# Docs by LangChain: AGENT DEVELOPMENT LIFECYCLE

> Documentation for LangSmith, Fleet, and our open source packages.

## AGENT DEVELOPMENT LIFECYCLE

- [AGENT DEVELOPMENT LIFECYCLE / Build (475 pages)](agent-development-lifecycle/build.md): Build agents with open source
- [AGENT DEVELOPMENT LIFECYCLE / Deploy (256 pages)](agent-development-lifecycle/deploy.md): Ship agents to production
- [AGENT DEVELOPMENT LIFECYCLE / Monitor (670 pages)](agent-development-lifecycle/monitor.md): Trace, debug, and observe agents

### Home

- [Docs by LangChain](../index.md)

### Test

#### Get started

- [LangSmith Evaluation](../langsmith/evaluation.md): Evaluate and test agent quality at scale with datasets, evaluators, prompts, and Studio.
- [Evaluation quickstart](../langsmith/evaluation-quickstart.md)
- [Evaluation concepts](../langsmith/evaluation-concepts.md)
- [Application-specific evaluation approaches](../langsmith/evaluation-approaches.md)

#### Datasets & Experiments

##### Datasets

- [Manage datasets](../langsmith/manage-datasets.md)
- [Custom output rendering](../langsmith/custom-output-rendering.md)

###### Create a dataset

- [Create and manage datasets in the UI](../langsmith/manage-datasets-in-application.md)
- [How to create and manage datasets programmatically](../langsmith/manage-datasets-programmatically.md)

##### Run an evaluation

- [How to evaluate agents](../langsmith/evaluate-llm-application.md)
- [How to evaluate with OpenTelemetry](../langsmith/evaluate-with-opentelemetry.md)
- [Run an evaluation with the UI](../langsmith/playground-link.md)
- [How to use the REST API](../langsmith/run-evals-api-only.md)

##### Evaluation techniques

###### Define evaluation target

- [How to define a target function to evaluate](../langsmith/define-target-function.md)
- [How to evaluate an application's intermediate steps](../langsmith/evaluate-on-intermediate-steps.md)
- [How to evaluate a runnable](../langsmith/langchain-runnable.md)
- [How to evaluate a graph](../langsmith/evaluate-graph.md)
- [How to simulate multi-turn interactions](../langsmith/multi-turn-simulation.md)
- [How to evaluate your agent with trajectory evaluations](../langsmith/trajectory-evals.md)

###### Scoring methods

- [How to return multiple scores in one evaluator](../langsmith/multiple-scores.md)
- [How to return categorical vs numerical metrics](../langsmith/metric-type.md)

###### Experiment configuration

- [Experiment configuration](../langsmith/experiment-configuration.md)
- [How to run an evaluation asynchronously](../langsmith/evaluation-async.md)
- [How to evaluate with repetitions](../langsmith/repetition.md)
- [How to handle model rate limits](../langsmith/handle-model-rate-limiting.md)
- [Automatically run evaluators on experiments](../langsmith/bind-evaluator-to-dataset-link.md)
- [How to add evaluators to an existing experiment (Python only)](../langsmith/evaluate-existing-experiment.md)
- [How to run an evaluation locally (Python only)](../langsmith/local.md)
- [How to read experiment results locally](../langsmith/read-local-experiment-results.md)
- [How to retry failed runs in experiments (Python only)](../langsmith/evaluate-with-retry.md)

###### Multimodal evaluations

- [Run an evaluation with multimodal content](../langsmith/evaluate-with-attachments.md): Learn how to create dataset examples with file attachments and use them in prompts and evaluators when running LangSmith evaluations with multimodal content.

##### Analyze experiment results

- [Analyze an experiment](../langsmith/analyze-an-experiment.md)
- [LangSmith Chat](../langsmith/chat-evaluation.md): Use Chat to analyze evaluations and experiments.
- [How to compare experiment results](../langsmith/compare-experiment-results.md)
- [How to filter experiments in the UI](../langsmith/filter-experiments-ui.md)
- [How to fetch performance metrics for an experiment](../langsmith/fetch-perf-metrics-experiment.md)
- [How to upload experiments run outside of LangSmith with the REST API](../langsmith/upload-existing-experiments.md)

##### Fine-tuning

- [Fine-tune models with Smithtune](../langsmith/smithtune.md): Use Smithtune to fine-tune models on LangSmith conversations and compare the results in LangSmith.

##### Tutorials

- [Evaluate a chatbot](../langsmith/evaluate-chatbot-tutorial.md)
- [Evaluate a RAG application](../langsmith/evaluate-rag-tutorial.md)
- [Test a ReAct agent with Pytest/Vitest and LangSmith](../langsmith/test-react-agent-pytest.md)
- [Evaluate a complex agent](../langsmith/evaluate-complex-agent.md)
- [Run backtests on a new version of an agent](../langsmith/run-backtests-new-agent.md)

##### Common data types

- [Example data format](../langsmith/example-data-format.md)
- [Dataset prebuilt JSON schema types](../langsmith/dataset-json-types.md)
- [Dataset transformations](../langsmith/dataset-transformations.md)

#### Evaluators

- [Evaluation types](../langsmith/evaluation-types.md)
- [Manage evaluators](../langsmith/evaluators.md): View and manage evaluators at the workspace level in LangSmith.
- [Manage evaluators with the SDK](../langsmith/manage-evaluators-sdk.md): Create, retrieve, update, list, and delete LangSmith evaluators programmatically with the SDK.
- [Automatically run evaluators on experiments](../langsmith/bind-evaluator-to-dataset.md)
- [Track and limit evaluator spend](../langsmith/evaluator-spend.md): Cap weekly LLM spend on evaluators with an organization-wide default or per-evaluator overrides to keep evaluator costs predictable.

##### Evaluator types

###### UI

- [How to define an LLM-as-a-judge evaluator](../langsmith/llm-as-judge.md)
- [How to define a decision model evaluator](../langsmith/decision-model-evaluator.md): Set up a LangSmith evaluator that uses SemIf or Jev as the judge, with noul, choice, and score questions that each return typed feedback.
- [How to define a code evaluator](../langsmith/code-evaluator-ui.md)
- [How to create a composite evaluator](../langsmith/composite-evaluators-ui.md)

###### SDK

- [How to define an LLM-as-a-judge evaluator](../langsmith/llm-as-judge-sdk.md)
- [How to define a code evaluator](../langsmith/code-evaluator-sdk.md)
- [How to create a composite evaluator](../langsmith/composite-evaluators-sdk.md)
- [How to define a summary evaluator](../langsmith/summary.md)
- [How to run a pairwise evaluation](../langsmith/evaluate-pairwise.md)

##### Frameworks & integrations

- [Run evals with openevals package](../langsmith/openevals.md): Run evaluations using the open-source openevals and agentevals packages with LangSmith.
- [How to run evaluations with pytest](../langsmith/pytest.md)
- [How to run evaluations with Vitest/Jest](../langsmith/vitest-jest.md)
- [Harbor integrations](../langsmith/harbor-integrations.md): Run evaluations, Deep Agents, and sandboxes on LangSmith with Harbor.

##### Improve evaluators

- [Improve LLM-as-judge evaluators using human feedback](../langsmith/improve-judge-evaluator-feedback.md)
- [How to improve your evaluator with few-shot examples](../langsmith/create-few-shot-evaluators.md)
- [How to audit evaluator scores](../langsmith/audit-evaluator-scores.md)

#### Annotation Queues

- [Use annotation queues](../langsmith/annotation-queues.md)
- [Manage feedback & annotation queues programmatically](../langsmith/annotation-queues-sdk.md)
- [Use assertions](../langsmith/assertions.md): Capture free-form acceptance criteria as dataset examples by writing assertions while reviewing runs in an annotation queue.
- [Set up feedback criteria](../langsmith/set-up-feedback-criteria.md)
- [Annotate traces and runs inline](../langsmith/annotate-traces-inline.md)

##### Feedback

- [Log user feedback using the SDK](../langsmith/attach-user-feedback.md)
- [Collect feedback with presigned URLs](../langsmith/presigned-feedback-tokens.md): Use presigned feedback tokens to collect user feedback from client-side applications without exposing your LangSmith API key.

#### Test from Playground

- [Test from the Playground](../langsmith/test-from-playground.md): Test prompts and model configurations over datasets in the LangSmith Playground without writing code.
- [Run an evaluation from the Playground](../langsmith/run-evaluation-from-playground.md)

#### Test from Studio

- [LangSmith Studio](../langsmith/studio.md)
- [Get started with Studio](../langsmith/quick-start-studio.md)
- [How to use Studio](../langsmith/use-studio.md)
- [Observability in Studio](../langsmith/observability-studio.md)
- [Studio troubleshooting](../langsmith/troubleshooting-studio.md)

## OpenAPI Specs

- [agent-server-openapi](https://docs.langchain.com/langsmith/agent-server-openapi.json)
- [openapi](https://api.host.langchain.com/openapi.json)
- [langsmith-platform-openapi](https://docs.langchain.com/langsmith/langsmith-platform-openapi.json)
