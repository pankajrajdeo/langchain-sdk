# LangSmith Engine on Self-hosted

> How LangSmith Engine runs in a self-hosted deployment, what it depends on outside your environment, and how it handles your data.

> [!NOTE]
> Self-hosted Engine requires LangSmith Helm chart `0.16.0` or later and a license that includes the Engine entitlement. It is not available on earlier chart versions. [Contact your account team](https://www.langchain.com/contact-sales) to have the entitlement added to your order.

LangSmith Engine is an agent within LangSmith that monitors your production traces, clusters them into issues, diagnoses each issue against your source code, proposes a fix as a PR, and identifies ground truth evals to add to your datasets. For a product overview, see [Engine](engine-overview.md).

In self-hosted LangSmith, Engine's orchestration, including its detect, fix, and verify loop, runs inside your VPC as part of LangSmith. Model work cannot run entirely in your VPC: Engine sends the content it needs to LangSmith Intelligence (LSI), a LangChain-managed zero data retention (ZDR) service. This page explains what that means for your data.

To install Engine, see [Enable Engine](deploy-self-hosted-full-platform.md#enable-engine). To connect Engine to your source code, create and configure your own GitHub App as described in [Connect Engine to GitHub](engine-github.md).

Engine works with three kinds of data:

* **Code** (optional)**:** Your agent's source, which Engine reads to diagnose issues and propose fixes.
* **Traces:** Runtime data from your agents, which can include user messages, tool outputs, and PII.
* **Model:** The LLM calls Engine makes to run diagnosis, generate fixes, and write evaluators.

## Availability by cloud and region

Engine is available where LSI is available:

| Cloud | Region | Status    |
| ----- | ------ | --------- |
| AWS   | US     | Available |
| GCP   | US     | Available |

For availability in other regions, contact your account team.

## How it works

LSI is the LangChain-managed service that powers Engine.

The flow:

* Your self-hosted Engine sends an HTTPS request to the LSI gateway for its cloud, listed in the per-cloud sections on this page.
* Engine authenticates with a short-lived license JWT obtained during LangSmith license verification. You do not provide separate model-provider credentials.
* LSI validates the JWT and routes the request to the model provider over private networking inside LangChain's environment.
* LSI returns the response to your self-hosted Engine.

Each request carries the trace content, code, and intermediate outputs Engine needs to do its work. LSI and the model provider process that content to serve the request.

Your cluster must allow outbound HTTPS to that gateway. The connection can use public egress or private connectivity. On AWS, follow [Connect with AWS PrivateLink](#connect-with-aws-privatelink) to keep Engine traffic on private networking.

If the connection to LSI is unavailable, Engine stops and returns an error rather than degrading to lower-quality output. There is no in-cluster model and no secondary provider to fall back on. The rest of your LangSmith deployment is unaffected, and Engine tries again on its next scheduled scan.

## What LangSmith Intelligence retains

LSI does not persist the content of prompts or model responses. It retains the following metadata for usage attribution and billing:

* Account, workspace, and project identifiers used to attribute usage.
* Model and token-usage metadata used for billing.

For model-provider retention and training commitments, see [Engine security](engine-security.md).

## Connect by cloud

### AWS (available in US)

The gateway host is [`beacon.aws.langchain.com`](deploy-self-hosted-full-platform.md#allow-egress-to-langsmith-intelligence). LSI routes requests to AWS Bedrock in LangChain's AWS environment.

#### Connect with AWS PrivateLink

Before configuring PrivateLink, complete [Enable Engine](deploy-self-hosted-full-platform.md#enable-engine), including its Helm and egress configuration.

[AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/) routes Engine traffic from your VPC to LSI without exposing that traffic to the public internet. The LSI endpoint service is hosted in `us-east-2`, and AWS supports access from VPCs in other regions.

Before you begin, collect your AWS account ID, VPC ID, private subnet IDs, and a security group for the interface endpoint. Configure that endpoint security group to allow inbound TCP traffic on port 443 only from the security group attached to the nodes or workloads that run Engine, or from the smallest private CIDR that contains them. Do not allow `0.0.0.0/0`.

To connect your VPC to LSI:

### Request access
Contact your account representative or [sales@langchain.dev](mailto:sales@langchain.dev) with your AWS account ID. LangChain adds your account to the endpoint service's allowed principals list.

### Create the interface VPC endpoint
Configure the AWS provider for the region that contains your VPC. Keep `service_region` set to `us-east-2`, including when your VPC is in another region. Select one private subnet per availability zone.

> [!NOTE]
> The `service_region` argument requires HashiCorp AWS provider `5.82.0` or later.

```hcl
resource "aws_vpc_endpoint" "langsmith_intelligence" {
  vpc_id              = var.vpc_id
  service_name        = "com.amazonaws.vpce.us-east-2.vpce-svc-054f37092752bff6b"
  service_region      = "us-east-2"
  vpc_endpoint_type   = "Interface"
  subnet_ids          = var.private_subnet_ids
  security_group_ids  = [var.security_group_id]
  private_dns_enabled = false
}
```

### Wait for LangChain to accept the connection
The endpoint status changes from `pendingAcceptance` to `available` after LangChain accepts the connection. Allow a few minutes for the change to propagate before testing connectivity.

### Route the LSI hostname to the endpoint
Enable DNS resolution and DNS hostnames for your VPC. Then, create a Route 53 private hosted zone and alias record so `beacon.aws.langchain.com` resolves to the VPC endpoint inside your VPC. Keep this hostname unchanged so TLS certificate validation succeeds. The private hosted zone also prevents fallback to public DNS when the endpoint is unavailable.

```hcl
resource "aws_route53_zone" "langsmith_intelligence" {
  name = "beacon.aws.langchain.com"

  vpc {
    vpc_id = var.vpc_id
  }
}

resource "aws_route53_record" "langsmith_intelligence" {
  zone_id = aws_route53_zone.langsmith_intelligence.zone_id
  name    = "beacon.aws.langchain.com"
  type    = "A"

  alias {
    name                   = aws_vpc_endpoint.langsmith_intelligence.dns_entry[0].dns_name
    zone_id                = aws_vpc_endpoint.langsmith_intelligence.dns_entry[0].hosted_zone_id
    evaluate_target_health = true
  }
}
```

If workloads use a corporate DNS resolver instead of the Amazon-provided resolver, configure conditional forwarding to Route 53 Resolver or create an equivalent private DNS override for `beacon.aws.langchain.com` that points to the endpoint DNS name.

### Verify private connectivity
From a node or container that runs Engine, resolve the gateway hostname:

```bash
getent ahostsv4 beacon.aws.langchain.com
```

Confirm that the result contains the private IP addresses assigned to the endpoint network interfaces. Then [enable Engine](deploy-self-hosted-full-platform.md#enable-engine), start an analysis, and confirm that it completes successfully. If the analysis does not complete, review the Engine installation and egress configuration.

<img src="https://mintcdn.com/langchain-5e9cc07a/ry58UzmmALISsnzO/langsmith/images/engine-self-hosted-aws.png?fit=max&auto=format&n=ry58UzmmALISsnzO&q=85&s=ae209b16e4cf2ad7199e7ea6bb333f84" alt="Architecture diagram of self-hosted LangSmith in your VPC connected by AWS PrivateLink to LangSmith Intelligence and Bedrock in LangChain's AWS environment." width="2240" height="1540" data-path="langsmith/images/engine-self-hosted-aws.png" />

### GCP (available in US)

The gateway host is [`beacon.langchain.com`](deploy-self-hosted-full-platform.md#allow-egress-to-langsmith-intelligence). LSI routes requests to Vertex in LangChain's GCP environment.

> [!NOTE]
> This is the same host self-hosted LangSmith uses for license verification and billing telemetry, so a GCP deployment adds a path rather than a new egress destination. See [Configure egress](self-host-egress.md).

<img src="https://mintcdn.com/langchain-5e9cc07a/I8T-TucKLNgYMiUb/langsmith/images/engine-self-hosted-gcp.png?fit=max&auto=format&n=I8T-TucKLNgYMiUb&q=85&s=d4769b8b4ed0e80f425e0a1dd615a5e9" alt="Architecture diagram of self-hosted LangSmith in your GCP project connected to LangSmith Intelligence and Vertex in LangChain's GCP environment." width="2240" height="1540" data-path="langsmith/images/engine-self-hosted-gcp.png" />

## Model selection and quality

Engine uses different models, each tuned for its role, to cluster issues, diagnose root causes against your code, generate fixes, and write evaluators that verify them. LangChain tunes these models for quality and token efficiency, and updates them as better models become available.

Engine uses managed inference, not a bring-your-own-key setup. This keeps Engine behavior consistent and improves it as LangChain updates the models. With a bring-your-own-key setup, model selection, tuning, and token efficiency can vary between requests.

## Where Engine processes data

In a self-hosted deployment, Engine separates data handling between your environment and LangChain's:

* **Your environment:** Engine orchestration and LangSmith-stored traces remain in your self-hosted environment.
* **LangChain's environment:** LSI and the model provider process content that Engine sends. LSI retains the billing metadata described above.

Engine's deployment-independent data handling, including zero data retention with every model provider and no use of customer data to train or fine-tune models, is described in [Engine security](engine-security.md).

## See also

* [Engine](engine-overview.md)
* [Configure Engine](engine.md)
* [Engine security](engine-security.md)
* [Engine webhooks](engine-webhooks.md)

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/engine-self-hosted.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
