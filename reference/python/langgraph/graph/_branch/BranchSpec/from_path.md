---
title: "from_path"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/graph/_branch/BranchSpec/from_path"
category: "reference"
tags: [reference, langgraph, graph, branch, branchspec, from_path]
---

# from_path

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/_branch/BranchSpec/from_path)

## Signature

```python
from_path(
    cls,
    path: Runnable[Any, Hashable | list[Hashable]],
    path_map: dict[Hashable, str] | list[str] | None,
    infer_schema: bool = False,
) -> BranchSpec
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/graph/_branch.py#L88)
