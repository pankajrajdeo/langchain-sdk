---
title: "Introducing LangSmith Fine-Tuning"
description: "LangChain introduces LangSmith Fine-Tuning and SmithTune, a CLI built for post-training models. Train specialized models without building data pipelines by hand."
source: "https://www.langchain.com/blog/langsmith-fine-tuning"
category: "blog"
published: "2026-09-24T14:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, langsmith-fine-tuning]
---

# Introducing LangSmith Fine-Tuning

- Use the LangSmith Fine-Tuning CLI and skill - `smithtune` - to leverage agent trajectories stored in LangSmith to a fine-tuned model in one end-to-end workflow
- In addition to driving training, the `smithtune` CLI handles evaluating the fine-tuned model and uploads eval results to LangSmith for easy analysis
- We partnered with [Fireworks](https://fireworks.ai/) & [Baseten](https://www.baseten.co/) to create a seamless link between LangSmith trajectories and creation of a dataset for fine-tuning both the platforms
