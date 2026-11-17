---
title: "langsmith/smith-api/sessions"
description: "Index of 6 pages and 0 subdirectories under langsmith/smith-api/sessions."
category: "index"
tags: [index, langsmith, smith-api, sessions]
---

# langsmith/smith-api/sessions

6 pages here.

## Files

- [Create a project or experiment](create-a-project-or-experiment.md) - Create a session, or update an existing session with the same name when upsert is true. Returns the refreshed session representation without optional run statistics.
- [Get a tracing project](get-a-tracing-project.md) - Returns one tracing project or experiment by ID. Pass include_stats=true to include run statistics.
- [List agent versions for a project](list-agent-versions-for-a-project.md) - Returns all agent versions (commit SHAs) seen in the given tracing project, ordered by first_seen_at descending.
- [List tracing projects](list-tracing-projects.md) - Returns a page of the workspace's tracing projects and experiments. Pass the response's next_cursor as cursor to fetch the next page; next_cursor is null on the last page. A cursor is valid only with...
- [Resolve an address to its tracing project](resolve-an-address-to-its-tracing-project.md) - Returns the tracing project (session) an address names. An address is an AGENT (id and environment), an EXPERIMENT (id), or an EVALUATOR (no id: evaluator traces share one project per workspace)...
- [Update a project](update-a-project.md) - Updates supplied fields and returns the refreshed resource without optional run statistics. Omitted fields remain unchanged. Null clears description, default_dataset_id, end_time, or extra. Extra...
