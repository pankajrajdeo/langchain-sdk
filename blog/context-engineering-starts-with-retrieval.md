---
title: "Context Engineering Starts with Retrieval"
description: "Agents waste time and context on clumsy searches, oversized results and stale data. Learn the retrieval techniques LangChain&#39;s Deep Agents harness uses to get the right context in."
source: "https://www.langchain.com/blog/context-engineering-starts-with-retrieval"
category: "blog"
published: "2026-10-23T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, context-engineering-starts-with-retrieval]
---

# Context Engineering Starts with Retrieval

- Agents work with a limited context window, and information retrieval breaks in three ways: inefficient searching, too much context at once, and irrelevant or stale context.
- The Deep Agents harness keeps searches small out of the box. The built-in filesystem tools search before they read: glob matches file names, grep finds matching lines, and read_file reads a page at a time. Oversized tool results are offloaded: the full result is saved to files, but the agent gets just the path and a preview.
- For custom search tools (like RAG), use "retrieve, offload, delegate": save results to files, return the paths, and let subagents read them. The main agent only sees what's relevant.
