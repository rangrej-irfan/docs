---
title: Databricks Clusters - Fine-Grained Access Control (FGAC)
---

# Databricks Clusters - Fine-Grained Access Control (FGAC)

## Overview

Databricks [all-purpose compute](https://docs.databricks.com/en/compute/index.html#types-of-compute){:target="_blank"} clusters are designed for interactive use cases where multiple users can connect to the
same cluster to run ad hoc queries. For this clusters, Fine-Grained Access Controls (FGAC) are supported only when SQL, 
Python, and R are enabled on these clusters. Fine-Grained Access Control (FGAC) includes the following features:

- Table-level access control
- Column-level access control
- Row-level access control
- Dynamic column masking
- Dynamic column encryption
- Centralized access audit
- Granular access audit record

The policies can be defined using object-level policies, tag-based policies, and attribute-based policies (ABAC).

!!! info "Scala is not supported with FGAC"
    When Scala is enabled on the cluster, user written Scala code can bypass the guardrails and access the data directly.
    This is a limitation of the Databricks platform and not Privacera.


For this Databricks cluster type, Privacera supports:

| Feature                          | Supported |
|----------------------------------|-----------|
| :green_circle: Access Management | Yes       |
| :green_circle: Discovery         | Yes       |
| :green_circle: Encryption        | Yes       |


<div class="grid cards" markdown>
-   :material-page-next: [Access Management](access/index.md)
</div>

<div class="grid cards" markdown>
-   :material-page-next: [Discovery](discovery/index.md)
</div>

<div class="grid cards" markdown>
-   :material-page-next: [Encryption](encryption/index.md)
</div>
