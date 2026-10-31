---
title: "LangSmith Sandboxes"
description: "Use LangSmith managed sandboxes to safely execute code and interact with the filesystem in isolated environments."
source: "https://docs.langchain.com/langsmith/sandboxes"
category: "docs"
tags: [docs, langsmith, sandboxes]
---

# LangSmith Sandboxes

> Use LangSmith managed sandboxes to safely execute code and interact with the filesystem in isolated environments.

Sandboxes are isolated environments that allow agents to safely execute potentially risky operations, like running arbitrary code or interacting with the filesystem, without affecting your main infrastructure.

From the [LangSmith homepage](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-sandboxes), select **Sandboxes** to manage all your sandbox resources.

![Sandboxes overview page](https://mintcdn.com/langchain-5e9cc07a/5nd3ca6haxRbnJZj/images/langsmith/sandboxes/sb-overview.png?fit=max\&auto=format\&n=5nd3ca6haxRbnJZj\&q=85\&s=6c2848ea69c0a99cbdd0930ceb91daa5)

## Environment availability

| Environment | Status |
| - | - |
| GCP US (`smith.langchain.com`) | Generally available |
| GCP EU (`eu.smith.langchain.com`) | Generally available |
| GCP APAC (`apac.smith.langchain.com`) | Generally available |
| AWS US (`aws.smith.langchain.com`) | Generally available |
| [BYOC](byoc.md) (your data plane URL) | Generally available |

> [!WARNING]
>
> On BYOC, use an API key that belongs to a BYOC workspace.

For self-hosted LangSmith deployments, see [Enable Sandboxes on self-hosted deployments](enable-self-hosted-sandboxes.md). For the infrastructure model, scaling, and upgrades, see [Self-hosted Sandbox architecture](self-host-sandbox-architecture.md).

## Network access

Restricted egress applies to non-Enterprise organizations by default and to organizations that request it. Organizations with an approved exemption can use unrestricted egress. Restricted sandboxes use a managed allowlist for common package registries, source repositories, and model APIs. LangSmith blocks destinations outside the allowlist, even if you add them to a sandbox's proxy configuration.

If you need unrestricted egress, [file a support ticket](https://support.langchain.com) with your organization or workspace ID, region, required destinations and ports, and use case. For more information, see [restricted egress and access requests](sandbox-auth-proxy.md#organization-level-restricted-egress).

## Get started

### 1. Install the SDK

**Python**

```bash
# uv
uv add langsmith

# pip
pip install langsmith
```

**TypeScript**

```bash
npm install langsmith
```

### 2. Set your API key

```bash
export LANGSMITH_API_KEY="<your-api-key>"
```

### 3. Create and run a sandbox

**Python**

```python
from langsmith.sandbox import SandboxClient

client = SandboxClient()

with client.sandbox() as sb:
    result = sb.run("python3 -c 'print(2 + 2)'")
    print(result.stdout)  # "4\n"
```

**TypeScript**

```ts
import { SandboxClient } from "langsmith/sandbox";

const client = new SandboxClient();
const sandbox = await client.createSandbox();
const result = await sandbox.run("node -e 'console.log(2 + 2)'");
console.log(result.stdout); // "4\n"
await sandbox.delete();
```

> [!TIP]
>
> Prefer the command line? The [Sandbox CLI](sandbox-cli.md) lets you create sandboxes, run commands, and open interactive shells without writing any code.

### 4. Use sandboxes with your agents

To wire sandboxes into agent code, see the Open Source docs:

* **Deep Agents**: [Use `LangSmithSandbox` as a backend](../integrations/sandboxes/langsmith.md), covering installation, backend creation, and cleanup.
* **Sandboxes as agent backends**: [Configure any sandbox as the execution backend](../deepagents/sandboxes.md) to give your agent `execute` and filesystem tools automatically.
* **LangChain / LangGraph integrations**: Use LangSmith sandboxes as a first-party option, or [connect third-party providers](../integrations/sandboxes.md) such as AgentCore, Daytona, E2B, Modal, Runloop, and Vercel.

## Resources

> [card] [Snapshots](sandbox-snapshots.md)
>
> Build filesystem images from Docker images or capture a running sandbox, then boot sandboxes from them.

> [card] [Service URLs](sandbox-service-urls.md)
>
> Access HTTP services running inside sandboxes via authenticated URLs.

> [card] [Auth proxy](sandbox-auth-proxy.md)
>
> Inject credentials into outbound API requests without hardcoding secrets.

> [card] [Mounts](sandbox-mounts.md)
>
> Attach S3 buckets, GCS buckets, and public Git repositories to a sandbox filesystem.

> [card] [Permissions](sandbox-permissions.md)
>
> Control which workspace members can interact with a sandbox after it is created.

> [card] [CLI](sandbox-cli.md)
>
> Build snapshots, manage sandboxes, open consoles, and tunnel TCP ports from the command line.

> [card] [SDK usage](sandbox-sdk.md)
>
> Create and manage sandboxes programmatically with the Python or TypeScript SDK.

> [card] [Self-hosted setup](enable-self-hosted-sandboxes.md)
>
> Enable Sandboxes on self-hosted LangSmith deployments with Helm or Terraform.

> [card] [Harbor](harbor-integrations.md#sandboxes)
>
> Run Harbor evaluations and rollouts on LangSmith sandboxes.

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandboxes.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
