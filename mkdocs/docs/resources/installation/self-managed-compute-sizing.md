---
title: Privacera Platform Compute Sizing
---

This section provides the compute sizing for the Privacera Platform deployment. The compute sizing is based on the
deployment size of the Privacera Platform. The deployment size is categorized into three sizes: small, medium, and
large. The compute sizing is provided for each pod in the Privacera Platform deployment.


!!! note
    The compute sizing is for reference only. The actual compute sizing may vary based on the workload and the
    deployment environment. You can adjust the compute sizing based on the workload and the deployment environment.

=== "Small Deployment (PoC)"

    | Pod                  | Memory | CPU  | Disk | Replication Factor |
    |----------------------|--------|------|------|---------------------|
    | Portal               | 2GB    | 0.5  | NA   | min=1 max=1         |
    | Maria DB             | 1GB    | 0.5  | 12   |                     |
    | Data Server          | 2GB    | 1    | NA   | min=1 max=1         |
    | Discovery - Driver   | 2GB    | 1    | 32   |                     |
    | Discovery - Executor | 2GB    | 1    | NA   |                     |
    | PolicySync           | 2GB    | 2    | 32   |                     |
    | Solr                 | 1.5GB  | 1    | 64   | 1                   |
    | Zookeeper            | 1GB    | 0.5  | 32   | 1                   |
    | Ranger KMS           | 1GB    | 0.5  | 12   | NA                  |
    | Ranger UserSync      | 1GB    | 0.5  | 12   | NA                  |
    | Grafana              | 1GB    | 0.5  | 1    |                     |
    | Graphite             | 1GB    | 0.5  | 32   |                     |
    | Kafka                | 1GB    | 0.5  | 32   |                     |
    | PEG                  | 1GB    | 0.5  | NA   | min=1 max=2         |
    | pkafka               | 1GB    | 0.5  | NA   |                     |
    | Ranger Admin         | 2GB    | 1    | NA   |                     |
    | Flowable             | 1GB    | 0.5  | NA   |                     |
    | Audit Server         | 1GB    | 1    | 32   |                     |
    | FluentD              | 1GB    | 1    | 32   |                     |

=== "Medium Deployment"

    | Pod                  | Memory | CPU  | Disk | Replication Factor |
    |----------------------|--------|------|------|---------------------|
    | Portal               | 4GB    | 2    | NA   |                     |
    | Maria DB             | 4GB    | 2    | 12   |                     |
    | Data Server          | 8GB    | 2    | NA   | min=2 max=4         |
    | Discovery - Driver   | 8GB    | 4    | 32   |                     |
    | Discovery - Executor | 2GB    | 2    | NA   |                     |
    | PolicySync           | 8GB    | 4    | 32   |                     |
    | Solr                 | 8GB    | 4    | 64   | 3                   |
    | Zookeeper            | 2GB    | 1    | 32   | 3                   |
    | Ranger KMS           | 2GB    | 2    | 12   | NA                  |
    | Ranger UserSync      | 4GB    | 2    | 12   | NA                  |
    | Grafana              | 4GB    | 2    | 1    |                     |
    | Graphite             | 4GB    | 2    | 32   |                     |
    | Kafka                | 4GB    | 2    | 32   |                     |
    | PEG                  | 4GB    | 2    | NA   | min=2 max=10        |
    | pkafka               | 4GB    | 2    | NA   |                     |
    | Ranger Admin         | 8GB    | 4    | NA   | min=2 max=4         |
    | Flowable             | 4GB    | 2    | NA   |                     |
    | Audit Server         | 4GB    | 2    | 32   |                     |
    | FluentD              | 4GB    | 2    | 32   |                     |


=== "Large Deployment"

    | Pod                  | Memory | CPU  | Disk | Replication Factor |
    |----------------------|--------|------|------|---------------------|
    | Portal               | 8GB    | 4    | NA   |                     |
    | Maria DB             | 8GB    | 4    | 12   |                     |
    | Data Server          | 8GB    | 2    | NA   | min=3 max=20        |
    | Discovery - Driver   | 16GB   | 8    | 32   |                     |
    | Discovery - Executor | 4GB    | 4    | NA   |                     |
    | PolicySync           | 32GB   | 8    | 32   |                     |
    | Solr                 | 32GB   | 8    | 64   | 3                   |
    | Zookeeper            | 4GB    | 2    | 32   | 3                   |
    | Ranger KMS           | 4GB    | 4    | 12   | NA                  |
    | Ranger UserSync      | 8GB    | 4    | 12   | NA                  |
    | Grafana              | 8GB    | 4    | 1    |                     |
    | Graphite             | 8GB    | 4    | 32   |                     |
    | Kafka                | 8GB    | 4    | 32   |                     |
    | PEG                  | 8GB    | 4    | NA   | min=3 max=20        |
    | pkafka               | 8GB    | 4    | NA   |                     |
    | Ranger Admin         | 16GB   | 8    | NA   | min=2 max=4         |
    | Flowable             | 8GB    | 4    | NA   |                     |
    | Audit Server         | 16GB   | 8    | 32   |                     |
    | FluentD              | 16GB   | 8    | 32   |                     |


<div class="grid cards" markdown>
-   :material-page-previous: [Prev](privacera-platform-installation-overview.md)
-   :material-page-next: [Next](privacera-platform-installation-prerequisites.md)
</div>
