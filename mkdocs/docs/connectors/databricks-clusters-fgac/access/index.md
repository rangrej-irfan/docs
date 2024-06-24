---
title: Access Management for Databricks all-purpose compute clusters with Fine-Grained Access Control (FGAC)
---

# Access Management for Databricks all-purpose compute clusters with Fine-Grained Access Control (FGAC)


## Introduction

For Databricks all-purpose compute clusters with Fine-Grained Access Control (FGAC), Privacera provides seamless
integration to enforce data access policies, monitor data usage, and ensure compliance with regulatory requirements.
This document provides an overview of the key features, benefits, and configuration steps for integrating Databricks
all-purpose compute clusters with Privacera.

## Connector Details

| Topic                                  | Detail                                                                                                                       |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Integration methodology                | Apache Ranger Plugin                                                                                                         |
| Access Tools                           | Databricks Console, JDBC                                                                                                     |
| Supported User Identities for Policies | <ul><li>AD/SCIM User</li><li>AD/SCIM Groups</li><li>Privacera Roles</li>                                                     |
| Data Source User Identities            | <ul><li>SAML</li><li>Databricks Login using Email Address</li><li>Databricks Token</li><li>Databricks Service Principal</li> |


## Supported Access Management Features

| Feature                         | Supported | Native | Using SecureView |
|---------------------------------|-----------|--------|------------------|
| :green_circle: Database Access Control | Yes       | Yes    | N/A |
| :green_circle: Table Access Control | Yes       | Yes    | N/A |
| :green_circle: View Access Control | Yes       | Yes    | N/A |
| :green_circle: Column Access Control | Yes       | Yes    | N/A |
| :green_circle: Row Access Control | Yes       | Yes    | N/A |
| :green_circle: Dynamic Column Data Masking | Yes       | Yes    | N/A |
| :green_circle: Dynamic Column Data Encryption | Yes       | Yes    | N/A |
| :green_circle: Centralized Access Audit | Yes       | N/A    | N/A |
| :green_circle: Granular Access Audit Record   | Yes       | N/A    | N/A |

## Limitations for Access Management Features

1. Scala shouldn't be enabled on the cluster. Only Object Level Access Control (OLAC) is supported for scala. Refer to the
   [OLAC documentation](../../databricks-clusters-olac/index.md) for more information.

## How it Works

The Privacera integration with Databricks all-purpose compute clusters with FGAC is achieved using the Apache Ranger
plugin. The Apache Ranger plugin is deployed as part of the Databricks Spark process using init scripts while creating
the clusters. The plugin fetches the policies from the Privacera Policy Server and when the SQL queries are executed by
the Databricks users, the plugin intercepts the queries and enforces the policies.


## User Identity Mapping

The policies in Privacera configured for the users and groups from AD/LDAP or SCIM and roles created in Privacera. 
These identities are mapped to the Databricks user identities as follows:

| Privacera Identity | Databricks Identity                          | Notes |
|--------------------|----------------------------------------------|-------|
| AD/SCIM User       | Email Address/ Databricks Service Principals |       |
| AD/SCIM Group      | N/A                                          | |
| Privacera Role     | N/A                                          | |

The Apache Ranger plugin which runs as part of the Databricks Spark process maps the email address of the user to the
AD/SCIM user. The groups and roles corresponding to the user are dynamically fetched from Privacera and used to enforce
group and roles based policies in the Databricks clusters.

Any attribute based access control (ABAC) and tag based policies configured in Privacera are enforced by the Apache Ranger plugin at 
runtime.

<div class="grid cards" markdown>
-   :material-page-previous: Prev topic: [About Databricks Clusters - FGAC](../index.md)
-   :material-page-next: Next topic: [Prerequisites](prerequisites.md)
</div>
