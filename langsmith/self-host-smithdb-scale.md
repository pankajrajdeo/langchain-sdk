---
title: "Configure SmithDB for scale"
description: "Choose tested SmithDB resource tiers and size Kubernetes workloads and the PostgreSQL metastore."
source: "https://docs.langchain.com/langsmith/self-host-smithdb-scale"
category: "docs"
tags: [docs, langsmith, self-host-smithdb-scale]
---

# Configure SmithDB for scale

> Choose tested SmithDB resource tiers and size Kubernetes workloads and the PostgreSQL metastore.

> [!NOTE]
> For non-SmithDB LangSmith services, see [Configure LangSmith for scale](self-host-scale.md).

Use these tested tiers as starting configurations for SmithDB. Connect SmithDB to your monitoring stack before you tune capacity, so you can observe the effect of each change. See [Configure SmithDB observability](self-host-smithdb-observability.md).

## Choose and scale a tier

The tiers are not throughput limits or prescribed configurations. CPU, memory, and cache size are per replica. Cache size is the volume each replica gets: the claim size on a network-attached disk, or the `emptyDir` limit on local SSD.

Choose the tier whose tested ingestion and query rates most closely match or exceed your expected steady-state load. To estimate your current trace volume, open **Settings > Usage** in LangSmith. See [Granular billable usage](granular-usage.md).

If you cannot measure your load, start at `small` and scale up. Under-sizing shows up as slower ingestion and queries rather than data loss.

Apply the per-replica resources and starting replica counts from the selected tier. If the workload later outgrows that starting point, you can scale SmithDB compute horizontally.

> [!NOTE]
> SmithDB query, ingestion, and compaction-worker HPAs are enabled by default. They require Kubernetes Metrics Server or another `metrics.k8s.io` provider. Verify availability with `kubectl get --raw /apis/metrics.k8s.io/v1beta1`.

### Scale with KEDA instead

> [!NOTE]
> KEDA scaling for SmithDB compaction workers requires Helm chart `0.17.0` or later.

SmithDB compaction workers can scale on queue depth through [KEDA](https://keda.sh/) rather than the CPU-based HPA. This suits bursty compaction backlogs, where queue depth rises before CPU does. LangSmith uses the same KEDA installation for its own queues; see [KEDA autoscaling for LangSmith queues](self-host-scale.md#keda-autoscaling-for-langsmith-queues) to install and configure it.

Enable the KEDA scaler for compaction workers:

```yaml
smithdb:
  compactionWorker:
    autoscaling:
      hpa:
        enabled: false
      keda:
        enabled: true
```

Use either the HPA or KEDA for a component, not both.

## Baseline tiers

| Component | Small<br />10 ingest / 10 query QPS | Medium<br />100 ingest / 40 query QPS | Large<br />1000 ingest / 100 query QPS |
| - | - | - | - |
| Ingestion | 1 replica<br />4 CPU<br />8 Gi memory<br />100 Gi cache | 1 replica<br />16 CPU<br />32 Gi memory<br />100 Gi cache | 2 replicas<br />56 CPU<br />150 Gi memory<br />1000 Gi cache |
| Query | 1 replica<br />4 CPU<br />8 Gi memory<br />200 Gi cache | 1 replica<br />28 CPU<br />48 Gi memory<br />200 Gi cache | 4 replicas<br />28 CPU<br />50 Gi memory<br />1000 Gi cache |
| Compaction | 1 replica<br />2 CPU<br />4 Gi memory | 1 replica<br />4 CPU<br />8 Gi memory | 1 replica<br />8 CPU<br />16 Gi memory |
| Compaction worker | 1 replica<br />8 CPU<br />16 Gi memory<br />100 Gi cache | 1 replica<br />16 CPU<br />32 Gi memory<br />100 Gi cache | 4 replicas<br />28 CPU<br />50 Gi memory<br />300 Gi cache |
| Cluster manager | 1 replica<br />250m CPU<br />256 Mi memory | 1 replica<br />250m CPU<br />256 Mi memory | 1 replica<br />2 CPU<br />2 Gi memory |

## Configure resources with Helm

The chart defaults to `small`. Select `small`, `medium`, or `large`:

```yaml
smithdb:
  resourceTier: medium
```

On LangSmith 0.17 the tier's cache size becomes the generated claim's capacity. On 0.16 it is the `ephemeral-storage` request and limit, which also sizes the generated `emptyDir`. Replica counts and autoscaling are configured separately.

An explicit component `resources` block replaces the tier's CPU and memory. On 0.17 it does not change the cache size; pick a different tier or override `deployment.volumes` for that. For local SSD values, see [Cache storage](self-host-smithdb-infrastructure.md#cache-storage).

See [SmithDB resource tiers](https://github.com/langchain-ai/helm/tree/main/charts/langsmith#smithdb-resource-tiers) for current values and chart details.

<details>
<summary>Example explicit resource configuration</summary>

This example overrides the query component at medium-tier sizes.

#### LangSmith 0.17
The cache claim stays at the tier size. These values request no node storage.

```yaml
smithdb:
  resourceTier: medium
  query:
    deployment:
      resources:
        requests:
          cpu: "28"
          memory: "48Gi"
        limits:
          cpu: "28"
          memory: "48Gi"
```

#### LangSmith 0.16
The storage limit also sizes the default `emptyDir`.

```yaml
smithdb:
  resourceTier: medium
  query:
    deployment:
      resources:
        requests:
          cpu: "28"
          memory: "48Gi"
          ephemeral-storage: "200Gi"
        limits:
          cpu: "28"
          memory: "48Gi"
          ephemeral-storage: "200Gi"
```

</details>

## Metastore capacity

The baseline tiers cover SmithDB Kubernetes workloads only. They do not include the PostgreSQL metastore. Use these starting points for a dedicated metastore:

| Tier | vCPU | Memory |
| - | - | - |
| Small | 2 | 16 GiB |
| Medium | 4 | 32 GiB |
| Large | 8 | 64 GiB |

Choose the nearest supported PostgreSQL instance shape from your provider and monitor database resource use and transaction latency during rollout.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-smithdb-scale.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
