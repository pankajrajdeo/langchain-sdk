---
title: "SmithDB feature availability"
description: "LangSmith features that are unavailable on self-hosted installations that query ClickHouse, and what still works without SmithDB."
source: "https://docs.langchain.com/langsmith/self-host-smithdb-features"
category: "docs"
tags: [docs, langsmith, self-host-smithdb-features]
---

# SmithDB feature availability

> LangSmith features that are unavailable on self-hosted installations that query ClickHouse, and what still works without SmithDB.

Some LangSmith features read trace data only from [SmithDB](self-host-smithdb.md). On a self-hosted installation that still queries ClickHouse, these features are hidden, disabled, or fall back to an older experience. Use this page to see what you gain by moving queries to SmithDB, and what keeps working if you have not.

> [!NOTE]
>
> ClickHouse support ends in LangSmith v0.19. For upgrade timing, see the [self-hosted changelog](self-hosted-changelog.md).

## Check whether queries use SmithDB

The features on this page turn on when LangSmith [queries SmithDB](self-host-smithdb-install.md#step-6-switch-queries-to-smithdb). [Dual ingestion](self-host-smithdb-install.md#step-4-enable-dual-ingestion) alone does not enable them. To check the current setting, read the `sdb_query_enabled` instance flag:

```bash
curl -s https://LANGSMITH_HOST/api/v1/info | jq '.instance_flags | {sdb_ingestion_enabled, sdb_query_enabled}'
```

SmithDB is necessary but not always sufficient. A feature can also depend on your LangSmith version, and some features roll out to self-hosted installations after they reach LangSmith Cloud. Each feature's page states its own version and region availability.

## Features that require SmithDB

Several rows cover a newer version of a feature that also works without SmithDB. The last column lists what you can still use on an installation that queries ClickHouse.

| Feature | What requires SmithDB | What works without SmithDB |
| - | - | - |
| [Filter query syntax](filter-traces.md#query-syntax) | The filter search bar and `field:value` query syntax, with thread, root run, single run, and any run scopes. | Filtering with legacy function-style filters. |
| [Custom dashboard chart editor](dashboards.md#custom-dashboards) | The current chart editor, with templates, ratios, per-series filters, grouping, breakdowns, and chart drilldowns. | Creating custom dashboards and charts with [custom dashboards (legacy)](dashboards.md#custom-dashboards-legacy), and prebuilt dashboards. |
| [Trajectory view](view-traces.md#trajectory-view) | The deduplicated conversation across turns, model calls, tools, and subagents. Also powers the Markdown export of a thread and parsed messages in experiment run details. | Trace inspection and message rendering for a single run. |
| [Trajectory evaluators](online-evaluations-multi-turn.md#evaluate-trajectories) | Online evaluators that use the `trajectory` variable to score the full agent path, including child model and tool calls. | Run evaluators and thread evaluators that read root-run messages. |
| [Threads in annotation queues](annotation-queues.md#assign-runs-and-threads-to-a-single-run-queue) | Adding a thread to an annotation queue from the thread view, and reviewing a thread item, which displays its trajectory. | Run-level annotation queues. |
| [Trajectory review in annotation queues](annotation-queues.md#review-a-single-run-queue) | Opening a queued run in the Trajectory view, on the graded turn. | Reviewing a run's inputs and outputs, with tool calls collapsed. |
| [Threads in datasets](manage-datasets-in-application.md#manually-from-a-tracing-project) | Adding selected threads, including thread items from an annotation queue, to a dataset as conversation examples. | Adding runs to a dataset. |
| [Thread automation rules](rules.md#set-the-item-type-to-runs-or-threads) | Creating thread rules that add threads to annotation queues or datasets, or send [webhooks](webhooks.md#read-a-thread-rule-payload). Backfilling a thread rule over historical data. | Run automation rules. |
| Public thread sharing | Sharing a whole thread with a public link. | Sharing a single trace with a public link. |
| Large trace actions | The paginated trace tree for large traces, downloading a whole trace as JSON, and deleting a whole trace from the trace details page. | Viewing traces, downloading individual runs, and existing deletion workflows. |
| [LLM Gateway usage](llm-gateway-monitoring.md) | The **Usage** dashboard: spend summary, charts, breakdowns, filters, and drilldowns. | Gateway routing and [policies](llm-gateway-spend-policies.md). |
| Agent trace volume | Trace-count sparklines on agent overview cards and the trace volume chart on an agent's overview. | Agent deployment, management, and other agent statistics. |
| [Feedback in bulk exports](data-export.md#limit-exported-fields) | Exporting the `feedbacks` field, which holds feedback keys and comments. | Bulk exports of every other field. |

Tracing, thread listing, datasets, and experiments work on either datastore.

## See also

* [Enable SmithDB on self-hosted LangSmith](self-host-smithdb.md)
* [Install SmithDB](self-host-smithdb-install.md)
* [Migrate ClickHouse history to SmithDB](self-host-smithdb-migrate.md)
* [Migrate to SmithDB-backed SDK methods](smithdb-sdk-migration.md)

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-smithdb-features.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
