---
title: Release 9.1
hide:
  - navigation
---

# Release 9.1

## Updates in Product Names

| Product Name   | Date            | Version |
|----------------|-----------------|---------|
| PrivaceraCloud | June 24th, 2024 | 9.1     |

!!! note
    This release is not available for self-managed deployments.


## New Features and Enhancements

/// details | Enhanced performance for admin audits on the PrivaceraCloud Portal
For customers who have millions of Admin Audits, this change will improve the performance of the Admin Audits page on
the PrivaceraCloud Portal. The Admin Audits page will now load faster and provide a better user experience.
///


### :warning: Breaking Changes

/// details | Temporary unavailabilty of Admin Audits
- Old Admin Audits: Audits created before this release will not be visible temporarily on the PrivaceraCloud Portal  until the data migration to the new system is complete. This migration is necessary to ensure compatibility with the
new performance enhancements.
- New Admin Audits: Audits created after this release will be immediately visible.
- Authorization, policy management, and access audits will remain unaffected during the  migration process
///

## Supported Versions by Connectors

| Data Sources                                | Supported Versions                                                                      |
|---------------------------------------------|-----------------------------------------------------------------------------------------|
| Databricks Runtime Version                  | 9.1 LTS:warning:<br> 10.4 LTS<br> 11.3 LTS<br> 12.2 LTS<br> 13.3 LTS<br> 14.3 LTS :new: |
| EMR (Privacera Plug-In)                     | 6.14.0<br>6.15.0<br>7.0.0                                                               |
| EMR (Native Ranger Plug-In)                 | 6.3.1                                                                                   |
| Open Source Spark Plug-In                   | 3.5.1                                                                                   |
| Open Source Trino                           | 444                                                                                     |
| Spark Thrift Server                         | 2.4.4                                                                                   |
| Dremio Software (with PolicySync connector) | 22.0<br>23.0                                                                            |
| Dremio Software (with Ranger Plug-In)       | 21.7                                                                                    |
| Open Source Trino with Starburst Enterprise | 435 LTS                                                                                 |
| Kafka Confluent                             | 6.2<br>7.1                                                                              |


## Self-Managed and Data Plane Platform Support
| **Services where Privacera Platform is installed** | Version(s) |
|----------------------------------------------------|------------|
| AKS                                                | 1.28       |
| EKS                                                | 1.28       |
| GKE                                                | 1.25       |
