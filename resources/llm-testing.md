---
title: "How to Test LLMs and AI Agents"
description: "- Testing AI applications and agents combines code checks, evals, and human review to ensure any changes are safe to release. - Offline evals use curated datasets to test changes before release..."
source: "https://www.langchain.com/resources/llm-testing"
category: "resources"
published: "2026-10-27"
author: "LangChain"
tags: [resources, llm-testing]
---

# How to Test LLMs and AI Agents

- Testing AI applications and agents combines code checks, evals, and human review to ensure any changes are safe to release.
- Offline evals use curated datasets to test changes before release. Online evals use real production traces to monitor live traffic.
- Production failures should become regression tests, so resolved issues do not return.
- LangSmith supports this workflow with datasets, experiments, trace-based evaluation, annotation queues, LLM-as-judge evaluators, and regression comparison.

LLM applications do not behave like traditional software. The same input can produce different outputs, and agents can choose different tools, actions, or paths. An AI agent can also produce a plausible answer while taking the wrong path to get there. For example, it may skip a policy lookup or choose the wrong tool, so if tests only check the final response, those failures can look like successes.

This means that software testing practices break down when applied to agents and AI applications [Testing LLM applications](https://www.langchain.com/testing-guide-ebook) requires checking what’s around the model, including prompts, retrieval, tools, state, and agent workflows, and evaluating quality over time. Teams need to test before they ship, monitor in production, and turn production failures into regression tests.

This guide covers the testing patterns that help teams catch issues before release and keep them from coming back later.

## What is LLM testing?

LLM testing checks whether an AI-powered application or agent behaves as intended. That includes checking an agent's output, tool calls, state it updates, and whether it completes the user’s task.

LLM and agent tests can run at different scopes. A **run** is one model or tool call, useful for checking a narrow behavior like a tool argument or structured output. A **trace** is one complete execution, useful for checking whether the agent completed a task and followed the right steps. A **thread** is a multi-turn conversation, useful for checking whether the agent maintains context and resolves the user’s goal over time.

### Agent tests vs evaluations

[An eval](https://www.langchain.com/resources/how-to-evaluate-llms) measures behavior or quality. A test uses that measurement, often with thresholds or pass/fail rules, to decide whether a change is acceptable. Teams often turn eval results into a release gate.

There are different types of agent evals. *Offline evaluations* run on curated datasets before release. Online evaluations score live traffic after deployment to catch failures and regressions.

For example, take a refund agent that has to return valid JSON and consult the refund policy before answering an end user. The answer explaining the policy takes judgment from either a domain expert or an [LLM-as-a-judge](https://www.langchain.com/resources/llm-as-a-judge), which uses a model to score the response.

A test compares those results against a release gate: the set of conditions a version must meet before it ships. In our refund agent example, the gate might require every policy lookup to pass and every answer to clear an agreed quality score. The table below pairs common testing questions with the check that answers them and an example gate:

| Testing question | Evaluation mechanism | Release gate |
| --- | --- | --- |
| Did this component return the exact field we need? | Code evaluator | Fail if the schema, enum, citation, or tool argument is wrong |
| Did the answer meet the quality bar? | LLM-as-judge evaluator or human review | Fail if helpfulness, groundedness, or task completion falls below the release threshold |
| Did the new version regress? | Experiment comparison on the same dataset | Fail if the candidate performs worse than the baseline on must-pass examples |
| Would a domain expert approve this answer? | Human review in an annotation queue | Hold release until assigned reviewers approve the response |
| Did the agent take the right path? | Trajectory evaluator over the recorded steps | Fail if the tool order, approval step, routing decision, or loop behavior violates the expected trajectory |

## How to test LLMs and AI agents

### Build the dataset before writing checks

A useful test dataset defines what the application should do for each example, using a set of inputs and good outputs. These actions range from retrieving information and calling tools to completing a conversation. For many teams, starting with a small set of carefully chosen, high-quality [examples](../langsmith/evaluation-concepts.md) is more useful than using a large dataset with shallow examples. Start with cases that represent real user tasks, known failure modes, and high-risk behavior. You can expand from there as production traces reveal new issues.

The table below shows how a test dataset might capture a refund request submitted after the company’s refund window has passed.

| Test-case field | What it captures | Example |
| --- | --- | --- |
| Input | The user request or component input | "Refund my annual plan after 31 days" |
| Reference output | The ideal response or end state for this input | “Your plan is past the 30-day refund window, so I can’t issue a refund. I can connect you with support to review your case.” |
| Evaluation criteria | The rules or standards used to score the output | must_cite_refund_policy: the answer cites the refund policy. must_not_promise_refund: the answer does not promise a refund. |
| Trajectory requirement | Required or forbidden intermediate steps | Must call lookup_policy before answering |
| Metadata | Labels that help filter and compare related examples | intent=refund, risk=high, locale=en-US |

Assertion names such as `must_cite_refund_policy` are labels the team chooses, and a code check, LLM-as-a-judge evaluator, or human reviewer can check whether the output satisfies them.

A strong dataset usually includes:

- Common user requests
- Known production failures
- High-risk edge cases
- Adversarial requests
- Less common production examples
- Examples corrected by domain experts

If a trace reveals a failure, teams can add the request to the dataset as a regression case. The case can specify either the expected outcome or a rule that an evaluator can check.

[In LangSmith](https://www.langchain.com/langsmith-platform), a framework-agnostic agent engineering platform, teams can use versioned datasets to run later experiments against the same stable set of examples. Teams can encode assertions in an example’s reference output or metadata, then write evaluators that read those criteria during an experiment. Trajectory requirements can be stored the same way.

### Test individual components with single-step evals

Unit tests are typically used in traditional software engineering, and can still be useful for deterministic pieces of LLM applications. But for behavior that depends on model output, a single-step eval is the better fit. These evals test a narrow behavior (such as retrieval, classification, extraction, or routing), without treating the model like deterministic code. Score the run’s output, and use the trace to understand failures.

To set up a single-step eval:

- Create a dataset slice for the run you want to test.
- Run the target function against each example.
- Score the output with the narrowest evaluator that catches the failure mode.
- Fail the build when the score falls below your threshold.

If the run depends on prior context, include the relevant thread state in the input. That keeps the eval focused on one behavior while still matching how the application behaves in practice.

Some behaviors are easy to [verify with code](../langsmith/code-evaluator-sdk.md). If the output needs to be valid JSON, match an exact class, include a required account ID, or call a specific tool, a deterministic check is usually the right fit.

Other behaviors require judgment. You may need to know whether an answer is grounded, follows instructions, has the right tone, or actually completes the task. Those checks are better suited to an [LLM-as-judge evaluator](../langsmith/llm-as-judge.md) or human review.

Human review usually shows up in two places. Teams can search traces or spot-check failed runs to understand what went wrong. This is useful for debugging specific issues, like an output that does not match the expected behavior.

Teams can also use annotation queues to collect structured feedback from reviewers, making human review part of the evaluation workflow. For example, if a reviewer spots an invented link in an annotation queue, they can label that failure, add feedback explaining the issue, and save the example to a dataset. Future offline evals can then check for the same failure pattern using an LLM judge, regex, schema validation, or a custom code evaluator.

Unit tests make individual component failures easier to diagnose, but they do not show whether an action made sense in context. You can check that the agent made a tool call, but whether it was the right one depends on the context from the thread.

### End-to-end test for the full workflow

Functional tests check whether an application completes a user task . For agents, this usually means an end-to-end test that evaluates the full run, often paired with trajectory evaluation to check the path the agent took..

For example, a support agent handling an out-of-window refund should look up the policy, find the right account, follow the approval path, and either explain the available options or escalate. A coding agent should edit the right files, run the project’s checks, and return a passing patch. A coding agent could check that the agent edits the right files, runs the project’s checks, and returns a patch that passes them.

The final output alone is weak evidence. Agent regressions often show up in the trajectory, including which tools the agent called, what arguments it passed, and whether it followed routing or approval rules.

Each test runs the application on a dataset of user tasks and records a trace of every step. Several checks can then score that trace:

- Code checks for deterministicpass/fail checks
- LLM-as-judge scores for answer quality
- Trajectory checks for tool calls, routing, and approval behavior
- Performance checks for latency, cost, retries, and token usage
- Human review for high-risk or ambiguous cases

The trace gives reviewers the context they need to understand why a test passed or failed.

### Apply regression tests to keep old failures fixed

Regression testing reruns known cases after a change to confirm that previously fixed failures have not returned. For LLM applications and agents, changes to any part of the workflow can affect behavior, including prompts, models, retrieval, tool schemas, memory policies, and routing logic.

Teams compare the candidate and the current baseline on the same stable dataset, examining failures on must-pass examples alongside average scores (an improved average can still mask a regression on a critical case).

Because a model can answer the same input differently, one output doesn't prove much. For high-risk or variable cases, teams can [run each example several times](../langsmith/experiment-configuration.md) for both versions with the same checks and compare failure rates rather than individual outputs. Before running the comparison, they set the repeat count and the acceptable failure rate. Forbidden actions, such as an unapproved write or a tool call with the wrong account ID, should typically use deterministic checks and a zero-failure threshold.

LLM judges can also vary, so their scores need to be checked against human-reviewed examples before a team relies on them for a release decision.

Regression suites organize cases around the risks they need to protect against. The table below outlines common coverage areas, why each exists, and how teams create the relevant cases.

In [LangSmith](https://www.langchain.com/langsmith-platform), each candidate run can be recorded as an experiment. Experiment comparison helps teams compare a candidate against a selected baseline, inspect score changes, review side-by-side outputs, and filter results by metadata.

![LangSmith comparison view showing regressions and improvements.](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ae0f20e270222b0c6de437e_LLM%20testing.png)

[Automation rules](../langsmith/rules.md) can route production traces with negative feedback to annotation queues for review. Teams can then add representative failures to datasets as regression cases.

### Measure performance across the workflow

Performance testing checks whether the application can complete the task within the latency, cost, token, and retry budgets you’ve set. A request can exceed its latency or cost budget because of a single bottleneck or inefficiencies across several steps.

End-to-end metrics tell you that a request exceeded its latency or cost budget, but the trace shows you where it happened. Common thresholds include:

- Maximum end-to-end latency for the user-facing path
- Maximum tool call latency for critical tools
- Maximum input and output tokens per trace
- Maximum retry count or loop count
- Minimum task-completion score at the chosen latency budget

These thresholds should be read alongside quality scores. A version with higher judge scores may also be much slower, while a cheaper version may call the wrong tool more often.

LangSmith experiment metadata and trace metrics support these decisions by making it possible to compare candidate versions across model, prompt, tool, route, data slice and release commit.

### Combine code checks and human review for safety tests

Safety testing usually needs both deterministic checks and judgment-based review.

Deterministic checks are useful when the rule is unambiguous, catching forbidden tool calls, known patterns of PII, missing disclaimers, invalid refusal formats, schema violations, or disallowed network destinations.

Other cases require more context. An agent may need to follow a support policy, stay within legal scope or escalate a sensitive case. These decisions are better suited for LLM judges, domain experts, or both.

A safety release gate can combine these approaches. It can block a version that makes a forbidden tool call, hold uncertain policy decisions for expert review, and turn reviewed cases into future tests. For high-stakes scenarios, human review is important because correct handling can depend on context, policy interpretation, and potential harms that automated checks cannot reliably judge.

[Annotation queues](../langsmith/annotation-queues.md) give domain experts a structured place to review and score cases that require contextual judgment before release.

### Validate AI agent trajectories and tool calls

Trajectory tests evaluate the path an agent takes to complete a task. For a refund request, did it look up the policy before answering? Did it get approval before making a write? Did it pass the right account identity into billing tools? Did it delegate correctly and stop when the task was done?

A trajectory view shows the full sequence of messages, tool calls, and subagent actions across a session, making it easier to spot skipped steps, incorrect tool use, and regressions in agent behavior.

[LangSmith Trajectories](https://www.langchain.com/blog/langsmith-trajectories-tracing) provide a chronological view of the messages and actions across a session, including subagents.

## LLM testing best practices

### Automate the release gate in CI/CD

The test types described above become release controls when a CI/CD pipeline runs them against each candidate change and compares the results with agreed thresholds.

A pipeline can draw on the following layers, depending on each pull request.

| CI step | What it catches | How to run it |
| --- | --- | --- |
| Component checks | Broken parsers, routers, tool schemas, prompt contracts | Run deterministic checks against individual components |
| Offline experiment | Quality regressions on curated examples | Run evals on a versioned dataset before release |
| Sandbox task run | Coding-agent changes that fail in a controlled environment | Run the task in a fresh sandbox created from a snapshot |
| Trajectory checks | Wrong tools, wrong order, missing approvals, or loops | Score the trace for required and forbidden steps |
| Human sign-off | Ambiguous, sensitive, or high-risk cases | Route examples to domain experts before merge or deployment |

In LangSmith, these layers map to code evaluators, datasets, offline experiments, experiment comparison, trace evaluation, and annotation queues. If the application uses coding agents, sandbox runs can be added when the product and environment support them. Our [CI/CD pipeline guide](../langsmith/cicd-pipeline-example.md) shows how automated tests and offline evaluations can fit into a quality gate before merge or deployment. Additionally, sandbox tests and expert sign-off can be layered in when an application’s risks require them.

### Use production failures to improve the test suite

After deployment, online evals continue evaluation on agents in production. In the [Agent Development Lifecycle (ADLC)](https://www.langchain.com/blog/the-agent-development-lifecycle), production traces feed the next round of evals, reviews and fixes. [LangSmith Engine](https://www.langchain.com/langsmith/engine) helps automate this process so users can quickly and continually improve agent behavior. It surfaces issues in production traces, proposes code and prompt fixes, builds examples for evaluation datasets, and monitors online behavior for any regressions of previously-resolved issues.

[LangSmith Evaluations](https://www.langchain.com/langsmith/evaluation) supports core parts of this workflow, including datasets, offline experiments, trajectory evaluation, experiment comparison, and human review through annotation queues. [Get started with LangSmith today](https://smith.langchain.com/).
