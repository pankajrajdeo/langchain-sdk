---
title: "langsmith_gateway"
description: "Route chat models built in this context through the LangSmith gateway."
source: "https://reference.langchain.com/python/langchain-core/utils/_gateway/langsmith_gateway"
category: "reference"
tags: [reference, langchain-core, utils, gateway, langsmith_gateway]
---

# langsmith_gateway

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/_gateway/langsmith_gateway)

Route chat models built in this context through the LangSmith gateway.

Unlike the `LANGSMITH_GATEWAY` env var, which applies to the whole process,
this applies only to the current context (thread or asyncio task), so a
server can route some requests through the gateway and not others.

The gateway is resolved when a model is constructed, so wrap construction
(for example `load()` of a serialized model), not invocation.

While the context is active, the gateway URL and key take precedence over
any base URL or API key passed to the model or set in the environment. This
lets a caller load an untrusted serialized model without it redirecting the
gateway key to another host or bypassing the gateway.

## Signature

```python
langsmith_gateway(
    *,
    api_key: str | SecretStr,
    base_url: str = _LANGSMITH_GATEWAY_DEFAULT_BASE,
) -> Iterator[None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_key` | `str \| SecretStr` | Yes | Key used to authenticate to the gateway. |
| `base_url` | `str` | No | Gateway host. The provider's path is appended per model. (default: `_LANGSMITH_GATEWAY_DEFAULT_BASE`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/utils/_gateway.py#L56)
