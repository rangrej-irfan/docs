---
title: Access Management for EMR cluster
---

# Access Management for EMR cluster


## Introduction

Amazon EMR [(Amazon Elastic MapReduce)](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html){:target="_blank"} is an cloud-based platform service that is designed for the effective scaling and
processing of large-volume datasets. It facilitates the users in quickly setting up, configuring, and scaling
virtual server clusters for analyzing and processing vast amounts of data efficiently. EMR supports a wide range of
open-source big data frameworks, including Hadoop, Spark, Hive and Trino giving users the flexibility to choose the
tools that best fit their needs.

Privacera provides a comprehensive access control solution for Amazon EMR clusters. The solution enables users to define
and enforce Fine-Grained Access Control policies for Spark, Hive and Trino and also Object-Level Access Control(OLAC)
for Spark.


## Connector Details


| Topic                                                                        | Detail                                                                                                                                                              |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integration methodology                                                      | [Apache Ranger Plugin](../../../resources/design/access-management/integrations/apache_ranger_plugin.md)                                                            |
| [Access Tools](../../../resources/design/access-management/access_tools.md)  | <ul>Spark FGAC<li>spark-sql</li>Spark OLAC<li>pyspark, spark-shell spark-submit</li>Hive<li>beeline</li>Trino<li>trino-cli</li>Others<li>Hue</li><li>Livy</li></ul> |
| Supported User Identities for Policies                                       | <ul><li>AD/SCIM User</li><li>AD/SCIM Groups</li><li>Privacera Roles</li>                                                                                            |
| Data Source User Identities                                                  | <ul><li>Kerberos User</li><li>JWT (only for Spark)</li></ul>                                                                                                        |


## Supported Access Management Features

| Feature                                       | Spark OLAC | Spark FGAC | Hive | Trino  |
|-----------------------------------------------|------------|:-----------|------|--------|
| :green_circle: Object Level Access Control    | Yes        | No         | No   | No     |
| :green_circle: Database Level Access Control  | No         | Yes        | Yes  | Yes    |
| :green_circle: Table Access Control           | No         | Yes        | Yes  | Yes    |
| :green_circle: View Access Control            | No         | Yes        | Yes  | Yes    |
| :green_circle: Column Access Control          | No         | Yes        | Yes  | Yes    |
| :green_circle: Row Access Control             | No         | Yes        | Yes  | Yes    |
| :green_circle: Dynamic Column Data Masking    | No         | Yes        | Yes  | Yes    |
| :green_circle: Dynamic Column Data Encryption | No         | Yes        | Yes  | Yes    |
| :green_circle: Centralized Access Audit       | No         | Yes        | Yes  | Yes    |
| :green_circle: Granular Access Audit Record   | No         | Yes        | Yes  | Yes    |


## Limitations for Access Management Features
1. Kerberos is required for Privacera to enforce access control policies.
2. JWT is supported for only Spark Plugin.

## How it Works

The Privacera integration with EMR clustes is achieved using the Apache Ranger
plugin. The Apache Ranger plugin is deployed as part of the EMR Spark/Hive/Trino process using bootstrap actions while creating
the clusters. The plugin fetches the policies from the Privacera Policy Server and when the commands are executed by
the users, the plugin intercepts the queries and enforces the policies.
Any attribute based access control (ABAC) and tag based policies configured in Privacera are enforced by the Apache Ranger plugin at
runtime.

## User Identity Mapping

The policies in Privacera configured for the users and groups from Kerberos or JWT and roles created in Privacera.
These identities are mapped to the Databricks user identities as follows:

| Privacera Identity | EMR Identity        |
|--------------------|---------------------|
| AD/SCIM User       | Kerberos User / JWT |
| AD/SCIM Group      | N/A                 |
| Privacera Role     | N/A                 |

The Apache Ranger plugin which runs as part of the Databricks Spark process maps the email address of the user to the
AD/SCIM user. The groups and roles corresponding to the user are dynamically fetched from Privacera and used to enforce
group and roles based policies in the Databricks clusters.



<div class="grid cards" markdown>
-   :material-page-previous: Prev topic: [About Databricks Clusters - FGAC](../index.md)
-   :material-page-next: Next topic: [Prerequisites](prerequisites.md)
</div>
