# Vertica

This document provides an overview of access management features supported by Privacera for Vertica.

## Access Management Methodology


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

### Recommended Configuration

To enhance performance, it is recommended to enable the following setting at
the database level.

Run below queries in Verica Database from SQL command line or using an SQL query editor such as DBeaver:

!!! Note "EnableAllRolesOnLogin Configuration"
    This configuration is a one-time requirement during the initial setup of the Vertica database.

```sql
SELECT parameter_name, current_value, default_value, allowed_levels, description FROM configuration_parameters WHERE parameter_name = 'EnableAllRolesOnLogin';

ALTER DATABASE <DATABASE_NAME> SET EnableAllRolesOnLogin = 1;
```

Enabling this setting eliminates the need for frequent SET ROLE commands,
ensuring a more streamlined access control process in Vertica. Policies
created at a specific role level are directly applied to the associated user.

<div class="grid cards" markdown>
-   :material-page-previous: Prev topic: [About Vertica Connector](../index.md)
-   :material-page-next: Next topic: [Prerequisites](prerequisites.md)
</div>
