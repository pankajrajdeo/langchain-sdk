---
title: "Building Evidence-Grounded Agent Memory with OpenWiki and Graphs"
description: "LangChain used OpenWiki, its open-source wiki compiler, and an evidence graph to build a persistent memory layer that preserves knowledge for agents to reuse across tasks. Learn how."
source: "https://www.langchain.com/blog/building-agent-memory-openwiki-graphs"
category: "blog"
published: "2026-10-28T17:24:00.000Z"
author: "LangChain Accounts"
tags: [blog, building-agent-memory-openwiki-graphs]
---

# Building Evidence-Grounded Agent Memory with OpenWiki and Graphs

- **A compiled wiki gives agents domain context that retrieval alone must reconstruct.** On questions spanning multiple sources, an agent using OpenWiki as a memory layer was 5x more accurate than one using grep tools alone.
- **Adding an evidence graph helps agents follow the wiki back to supporting evidence.** We turned citations and document references into explicit graph edges agents could follow. Compared with the wiki alone, this doubled how consistently the agent cited the same evidence, improved accuracy by 27%, and cut cost per correct answer by 58%.
- **Save compiled memory for repeated cross-source reasoning.** The wiki captures domain knowledge and complex relationships. Adding an evidence graph improves accuracy and retrieval consistency. For simple lookups, however, the agent without memory was just as accurate and faster.
