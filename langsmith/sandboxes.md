# LangSmith Sandboxes
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/sandboxes)
Use LangSmith managed sandboxes to safely execute code and interact with the filesystem in isolated environments.

Sandboxes are isolated environments that allow agents to safely execute potentially risky operations, like running arbitrary code or interacting with the filesystem, without affecting your main infrastructure.

From the [LangSmith homepage](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-sandboxes), select **Sandboxes** to manage all your sandbox resources.

> **Image:** [Sandboxes overview page](https://docs.langchain.com/langsmith/sandboxes)

## Environment availability

| Environment                           | Status              |
| ------------------------------------- | ------------------- |
| GCP US (`smith.langchain.com`)        | Generally available |
| GCP EU (`eu.smith.langchain.com`)     | Generally available |
| GCP APAC (`apac.smith.langchain.com`) | Generally available |
| AWS US (`aws.smith.langchain.com`)    | Generally available |

For self-hosted LangSmith deployments, see [Enable Sandboxes on self-hosted deployments](https://docs.langchain.com/langsmith/deploy-self-hosted-full-platform#enable-sandboxes).

## Get started

### 1. Install the SDK

```bash
# uv
uv add "langsmith[sandbox]"

# pip
pip install "langsmith[sandbox]"
```

```bash
npm install langsmith
```

### 2. Set your API key

```bash
export LANGSMITH_API_KEY="<your-api-key>"
```

### 3. Create and run a sandbox

```python
from langsmith.sandbox import SandboxClient

client = SandboxClient()

with client.sandbox() as sb:
    result = sb.run("python -c 'print(2 + 2)'")
    print(result.stdout)  # "4\n"
```

```ts
import { SandboxClient } from "langsmith/sandbox";

const client = new SandboxClient();
const sandbox = await client.createSandbox();
const result = await sandbox.run("node -e 'console.log(2 + 2)'");
console.log(result.stdout); // "4\n"
await sandbox.delete();
```

> [!TIP]
> Prefer the command line? The [Sandbox CLI](https://docs.langchain.com/langsmith/sandbox-cli) lets you create sandboxes, run commands, and open interactive shells without writing any code.

### 4. Use sandboxes with your agents

To wire sandboxes into agent code, see the Open Source docs:

* **Deep Agents**: [Use `LangSmithSandbox` as a backend](https://docs.langchain.com/oss/python/integrations/sandboxes/langsmith), covering installation, backend creation, and cleanup.
* **Sandboxes as agent backends**: [Configure any sandbox as the execution backend](https://docs.langchain.com/oss/python/deepagents/sandboxes) to give your agent `execute` and filesystem tools automatically.
* **LangChain / LangGraph integrations**: Use LangSmith sandboxes as a first-party option, or [connect third-party providers](https://docs.langchain.com/oss/python/integrations/sandboxes) such as AgentCore, Daytona, E2B, Modal, Runloop, and Vercel.

## Resources

#### [Snapshots](https://docs.langchain.com/langsmith/sandbox-snapshots)
Build filesystem images from Docker images or capture a running sandbox, then boot sandboxes from them.

#### [Service URLs](https://docs.langchain.com/langsmith/sandbox-service-urls)
Access HTTP services running inside sandboxes via authenticated URLs.

#### [Auth proxy](https://docs.langchain.com/langsmith/sandbox-auth-proxy)
Inject credentials into outbound API requests without hardcoding secrets.

#### [Mounts](https://docs.langchain.com/langsmith/sandbox-mounts)
Attach S3 buckets, GCS buckets, and public Git repositories to a sandbox filesystem.

#### [Permissions](https://docs.langchain.com/langsmith/sandbox-permissions)
Control which workspace members can interact with a sandbox after it is created.

#### [CLI](https://docs.langchain.com/langsmith/sandbox-cli)
Build snapshots, manage sandboxes, open consoles, and tunnel TCP ports from the command line.

#### [SDK usage](https://docs.langchain.com/langsmith/sandbox-sdk)
Create and manage sandboxes programmatically with the Python or TypeScript SDK.

#### [Self-hosted setup](https://docs.langchain.com/langsmith/deploy-self-hosted-full-platform#enable-sandboxes)
Enable Sandboxes on self-hosted LangSmith deployments with Helm or Terraform.

#### [Harbor](https://docs.langchain.com/langsmith/harbor-integrations#sandboxes)
Run Harbor evaluations and rollouts on LangSmith sandboxes.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandboxes.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
