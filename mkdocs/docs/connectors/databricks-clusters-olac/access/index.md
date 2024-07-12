---
title: Access Management for Databricks all-purpose compute clusters with Object-Level Access Control (OLAC)
---


# Access Management for Databricks all-purpose compute clusters with Object-Level Access Control (OLAC)



## Introduction

For Databricks all-purpose compute clusters with Object-Level Access Control (OLAC), Privacera provides seamless
integration to enforce data access policies, monitor data usage, and ensure compliance with regulatory requirements.
This document provides an overview of the key features, benefits, and configuration steps for integrating Databricks
all-purpose compute clusters with Privacera.


## Connector Details


| Topic                                                                       | Detail                                                                                                                       |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Integration methodology                                                     | Dataserver Signature generation                   |
| [Access Tools](../../../resources/design/access-management/access_tools.md) | Databricks Console, JDBC                                                                                                     |
| Supported User Identities for Policies                                      | <ul><li>AD/SCIM User</li><li>AD/SCIM Groups</li><li>Privacera Roles</li>                                                     |
| Data Source User Identities                                                 | <ul><li>SAML</li><li>Databricks Login using Email Address</li><li>Databricks Token</li><li>Databricks Service Principal</li> |




## Supported Access Management Features

| Feature                         | Supported |
|---------------------------------|-----------|
| :green_circle: S3 Access control | Yes       | 
| :red_circle: DBFS Access control | No       | 

## How it Works

Privacera integrates with Databricks all-purpose compute clusters using the Privacera Spark plugin, deployed via init scripts during cluster creation. The plugin calls the dataserver to obtain a signature, which is then authorized based on the Apache Ranger plugin.

## User Identity Mapping

The policies in Privacera configured for the users and groups from AD/LDAP or SCIM and roles created in Privacera. 
These identities are mapped to the Databricks user identities as follows:

| Privacera Identity | Databricks Identity                          | Notes |
|--------------------|----------------------------------------------|-------|
| AD/SCIM User       | Email Address/ Databricks Service Principals |       |
| AD/SCIM Group      | N/A                                          | |
| Privacera Role     | N/A                                          | |

The Apache Ranger plugin which runs as part of the Dataserver maps the email address of the user to the
AD/SCIM user. The groups and roles corresponding to the user are dynamically fetched from Privacera and used to enforce
group and roles based policies in the Databricks clusters.

Any attribute based access control (ABAC) and tag based policies configured in Privacera are enforced by the Apache Ranger plugin at runtime.

<div class="grid cards" markdown>
-   :material-page-previous: Prev topic: [About Databricks Clusters - OLAC](../index.md)
-   :material-page-next: Next topic: [Prerequisites](prerequisites.md)
</div>