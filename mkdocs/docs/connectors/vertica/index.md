# Vertica

## Introduction

Vertica is a high-performance, scalable SQL analytics database that is designed to handle large volumes of data and complex queries. Privacera provides seamless integration with Vertica to enable organizations to enforce data access policies, monitor data usage, and ensure compliance with regulatory requirements. This document provides an overview of the key features, benefits, and configuration steps for integrating Vertica with Privacera.

## Access Management


| Topic                     | Detail               |
|---------------------------|----------------------|
| Integration methodology   | Privacera PolicySync |
| Access Tools              | JDBC                 |
| Supported User Identities | Username, Password   |

## Supported Access Management Features


| Feature                                      | Supported | Native | Using SecureView |
|----------------------------------------------|-----------|--------|------------------|
| :green_circle: Database Access Control       | Yes       | Yes    | Yes              |
| :green_circle: Table Access Control          | Yes       | Yes    | Yes              |
| :green_circle: View Access Control [^1]      | Yes       | Yes    | Yes              |
| :green_circle: Column Access Control         | Yes       | No     | Yes              |
| :green_circle: Row Access Control            | Yes       | Yes    | Yes              |
| :no_entry_sign: Cell Access Control          | No        | No     | N/A              |
| :no_entry_sign: Column Data Masking          | No        | No     | N/A              |
| :no_entry_sign: Column Data Encryption       | No        | No     | N/A              |
| :green_circle: Centralized Access Audit      | Yes       | N/A    | N/A              |
| :no_entry_sign: Granular Access Audit Record | No        | N/A    | N/A              |

[^1]: **Note**: Column access control, Masking and Row Level Filter not supported for Vertica views.

### Limitations for Access Management Features

The following are the limitations with Vertica connector.

1. The CREATE DATABASE permission cannot be directly assigned to users or roles. Vertica does not provide a user permission to create new databases.

2. Views in Vertica do not support native column masking. When a value is masked in the original table, the masking is also applied to the view.

3. Native row filtering is not supported for views in Vertica. When a row filter is applied on the original table, the same filtering is extended to the view.

4. Using the native row filter might be inefficient when analysing queries that involve a large number of users.

## Discovery Features

Discover features are not supported in Lake Formation connectors


## Data Encryption Features

Data encryption features are not supported in Lake Formation connectors

<div class="grid cards" markdown>
-   :material-page-previous: Prev topic: [About Lake Formation](../index.md)
-   :material-page-next: Next topic: [Prerequisites](prerequisites.md)
</div>
