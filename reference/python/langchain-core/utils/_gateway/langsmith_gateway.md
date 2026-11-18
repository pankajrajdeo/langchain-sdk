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

Treat invocation arguments, including `extra_headers`, as trusted application
input; gateway header precedence is not an authorization boundary.

## Signature

```python
langsmith_gateway(
    *,
    api_key: str | SecretStr,
    base_url: str = _LANGSMITH_GATEWAY_DEFAULT_BASE,
    headers: Mapping[str, str] | None = None,
) -> Iterator[None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_key` | `str \| SecretStr` | Yes | Key used to authenticate to the gateway. |
| `base_url` | `str` | No | Gateway host. The provider's path is appended per model. (default: `_LANGSMITH_GATEWAY_DEFAULT_BASE`) |
| `headers` | `Mapping[str, str] \| None` | No | Headers sent with every request to the gateway, such as a service key. They replace any header of the same name (case-insensitive) set on the model. They are kept in private model state and sent by the HTTP client, but are not serialized or traced. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/utils/_gateway.py#L57)
