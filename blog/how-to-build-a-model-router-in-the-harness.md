---
title: "How to Build a Model Router in the Harness"
description: "How we built a model router into Open SWE&#39;s harness that cut median cost per coding task by 64% with no measurable drop in quality, and how to build your own."
source: "https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness"
category: "blog"
published: "2026-10-01T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, how-to-build-a-model-router-in-the-harness]
---

# How to Build a Model Router in the Harness

- **Many tasks don't need frontier intelligence.** In our experiments, model routing cut median cost per coding task by 64% compared with the baseline, with no noticeable change in quality.
- **An effective model router belongs in the harness, not a generic gateway. **Choosing the right model requires domain and task context that the harness already assembles, and a gateway typically lacks.
- **Effective router design is rooted in observability and evals.** It requires an understanding of an agent's task space, model performance research, and clear success criteria.
