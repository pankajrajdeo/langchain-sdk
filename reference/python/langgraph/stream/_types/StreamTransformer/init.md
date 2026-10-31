---
title: "init"
description: "Return the projection dict."
source: "https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/init"
category: "reference"
tags: [reference, langgraph, stream, types, streamtransformer, init]
---

# init

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/init)

Return the projection dict.

Keys become entries in `run.extensions`. If the transformer has
`_native = True`, keys are also set as direct attributes on the
run stream.

StreamChannel instances in the return value are automatically
wired by the StreamMux for protocol event auto-forwarding.

## Signature

```python
init(
    self,
) -> dict[str, Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/stream/_types.py#L127)
