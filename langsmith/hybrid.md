> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hybrid

> A LangSmith Deployment setup where you self-host Agent Servers in your infrastructure and send traces to LangSmith Cloud or a self-hosted LangSmith instance.

export const protocol_0 = undefined

export const prefix_0 = undefined

export const suffix_0 = undefined

Hybrid is a platform setup for [LangSmith Deployment](/langsmith/deployment), which **deploys and runs agents in production**.

In a hybrid platform setup, you self-host [Agent Servers](/langsmith/agent-server) in your own infrastructure and send their traces to LangSmith, where LangSmith can be either a [self-hosted](/langsmith/self-hosted) instance or [LangSmith Cloud](/langsmith/cloud).

This setup gives you control over where your agent workloads run while letting you choose the [LangSmith platform option](/langsmith/platform-setup) that best fits your observability and compliance requirements.

## Components

| Component                                                                                                                              | Where it runs                                         | Who manages it                        |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------- |
| <Tooltip tip="The server that runs your applications.">Agent Servers</Tooltip> <br />for [LangSmith Deployment](/langsmith/deployment) | Your infrastructure                                   | You                                   |
| LangSmith <br />(tracing, evaluation, prompts)                                                                                         | Self-hosted in your infrastructure, or LangSmith SaaS | You (self-hosted) or LangSmith (SaaS) |

<Note>
  Hybrid is a platform setup for LangSmith Deployment (agent serving). To set up LangSmith for observability, evaluation, and prompt engineering only, see [Set up LangSmith](/langsmith/platform-setup).
</Note>

## Workflow

1. Build and test your agent locally.
2. Deploy your agent to an [Agent Server running in your infrastructure](#self-host-your-agent-servers).
3. Send the agent's traces to [LangSmith (self-hosted or SaaS) for observability and evaluation](#choose-where-traces-are-sent).

### Self-host your Agent Servers

Deploy standalone Agent Servers using Docker, Docker Compose, or Kubernetes. See the [standalone server guide](/langsmith/deploy-standalone-server) for prerequisites, environment variables, and platform-specific instructions.

### Choose where traces are sent

Agent Servers send traces to LangSmith based on the `LANGSMITH_ENDPOINT` environment variable:

* **LangSmith SaaS**: Omit `LANGSMITH_ENDPOINT` to use the default (GCP US), or set it to the endpoint for your region:

  <table>
    <thead>
      <tr>
        <th>Region</th>

        <th>
          {protocol_0 === false ? "Host" : "URL"}
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>GCP US</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>GCP EU</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}eu.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>GCP APAC</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}apac.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>AWS US</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}aws.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>
    </tbody>
  </table>

* **Self-hosted LangSmith**: Set `LANGSMITH_ENDPOINT` to the hostname of your [self-hosted LangSmith](/langsmith/self-hosted) instance.

In both cases, authenticate with a [LangSmith API key](/langsmith/create-account-api-key) issued by the LangSmith instance you are tracing to.

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/hybrid.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
