---
title: Advanced Configuration for LakeFormation Connector in Push Mode
---



# Advanced Configuration for LakeFormation Connector in Push Mode

## Connectivity Configuration

Privacera's LakeFormation connector uses AWS services like AWS LakeFormation, AWS Glue, and AWS IAM to get
the user identities and manage privileges in Lake Formation.. To configure the connector, you need AWS Policies which 
has the permissions to read the meta data from AWS Glue, AWS IAM Roles from AWS IAM and update permissions to update 
AWS Lake Formation. For detailed permissions, refer to the [prerequisites](prerequisites.md).

- IAM Role - The IAM role should have the necessary permissions to read the metadata from AWS Glue, read the IAM roles. Refer to the [prerequisites](prerequisites.md) for detailed permissions.
- Access Key and Secret Key
- AWS Account ID - This is the AWS account ID where the AWS Lake Formation is running. E.g. 123456789012
- AWS Region - The AWS region where the AWS Lake Formation is running. E.g. us-west-2

=== "Self Managed and Data Plane"

    In Privacera Manager, set the following properties in `privacera/privacera-manager/config/custom-vars/connectors/lakeformation/push/vars.connector.lakeformation.push.yml`
    
      ```yaml
      CONNECTOR_LAKEFORMATION_AWS_ACCOUNT_ID: ""
      CONNECTOR_LAKEFORMATION_AWS_REGION: ""
      ```

=== "PrivaceraCloud"

---


## Native Row Filtering

Redshift supports native row filtering. When you add a row filter policy in Ranger with a row filter condition, it
creates a data filter with the same row filter condition inside RedShift DB for the users, groups and/or roles. To 
enable this behavior, set the following properties:

=== "Self Managed and Data Plane"

      In Privacera Manager, set the following properties in redshiftdb.yaml file:

      ```yaml
      CONNECTOR_REDSHIFT_ENABLE_ROW_FILTER: "true"
      
      CONNECTOR_REDSHIFT_ENABLE_VIEW_BASED_MASKING: "false"
      CONNECTOR_REDSHIFT_ENABLE_VIEW_BASED_ROW_FILTER: "false"
      
      CONNECTOR_REDSHIFT_ENABLE_DATA_ADMIN: "false"
      
      CONNECTOR_REDSHIFT_SECURE_VIEW_CREATE_FOR_ALL: "false"
      ```

=== "PrivaceraCloud"
          
      In PrivaceraCloud, go to the Redshift application and set the following properties:
      Enable Row Filter: `true`



---

=== "Self Managed and Data Plane"

      In Privacera Manager, set the following properties in redshiftdb.yaml file:

      ```yaml
      CONNECTOR_REDSHIFT_ENABLE_ROW_FILTER: "true"
      
      CONNECTOR_REDSHIFT_ENABLE_VIEW_BASED_MASKING: "false"
      CONNECTOR_REDSHIFT_ENABLE_VIEW_BASED_ROW_FILTER: "false"
      
      CONNECTOR_REDSHIFT_ENABLE_DATA_ADMIN: "false"
      
      CONNECTOR_REDSHIFT_SECURE_VIEW_CREATE_FOR_ALL: "false"
      ```

=== "PrivaceraCloud"

      In PrivaceraCloud, go to the Redshift application and set the following properties:
      Enable Row Filter: `true`

---

/// details | CONNECTOR_LAKEFORMATION_AWS_ACCOUNT_ID <br> Specifies the AWS account id for the AWS Lake formation.                   

| Topic | Description |
| --- |----------------------------------------------------------|
| **Description** | Specifies the AWS account id for the AWS Lake formation. |
| **PrivaceraCloud Field Name** | AWS Account ID                                           |
| **Self Managed/Data Plane** | CONNECTOR_LAKEFORMATION_AWS_ACCOUNT_ID                   |
| **Property Type** | Basic                                                    |
| **Mandatory** | Yes                                                      |
| **Type** | String                                                   |
| **Default** | *None*                                                   |
| **Example** | `123456789012`                                           |
///

**aws.account.id** - Specifies the AWS account id for the AWS Lake formation. (1)
{ .annotate }

1.  - **PrivaceraCloud Field Name:** AWS Account ID
- **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_ACCOUNT_ID
- **Property Type:** Basic
- **Mandatory:** Yes
- **Type:** String
- **Default:** *None*
- **Example:** `123456789012`


## AWS Account Configuration

**aws.account.id** - Specifies the AWS account id for the AWS Lake formation. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** AWS Account ID
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_ACCOUNT_ID
      - **Property Type:** Basic
      - **Mandatory:** Yes
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789012`

**aws.assume.iam.role.arn** - Specifies the AWS assume IAM role ARN for the AWS Lake formation. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** AWS Assume IAM Role ARN
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_ASSUME_IAM_ROLE_ARN
      - **Property Type:** Basic
      - **Mandatory:** Yes
      - **Type:** String
      - **Default:** *None*
      - **Example:** `arn:aws:iam::123456789012:role/MyRole`

**aws.assume.iam.role.external.id** - Specifies the AWS assume IAM role external id for the AWS Lake formation. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** AWS Assume IAM Role External ID
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_ASSUME_IAM_ROLE_EXTERNAL_ID
      - **Property Type:** Basic
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `ExternalId123`

**aws.access.key** - Specifies the AWS access key for the AWS Lake formation connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_ACCESS_KEY
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `AKIAIOSFODNN7EXAMPLE`

**aws.secret.key** - Specifies the AWS secret key for the AWS Lake formation connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_SECRET_KEY
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

**aws.session.token** - Specifies the AWS session token for the AWS Lake formation connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_SESSION_TOKEN
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `AQoDYXdzEJr...<remainder of security token>`

**aws.region** - Specifies the AWS region for the AWS Lake formation connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** AWS Region
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_REGION
      - **Property Type:** Basic
      - **Mandatory:** Yes
      - **Type:** String
      - **Default:** *None*
      - **Example:** `us-west-2`

**saml.provider.arn** - Specifies the SAML provider ARN for the AWS Lake formation connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** SAML Provider ARN
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SAML_PROVIDER_ARN
      - **Property Type:** Basic
      - **Mandatory:** Yes
      - **Type:** String
      - **Default:** *None*
      - **Example:** `arn:aws:iam::123456789012:saml-provider/MyProvider`

## Load keys and intervals

**sync.resource.enable** - Specifies whether to enable resources to be synced from AWS Lake Formation to Lake Formation Connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RESOURCE_SYNC_ENABLE
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**sync.servicepolicy.enable** - Specifies whether to do policy synchronization periodically from LakeFormation for reconciliation with Privacera policies. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Not applicable
      - **Self Managed/Data Plane:** Not applicable
      - **Property Type:** Basic
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**sync.interval.sec** - Specifies the interval in seconds for PolicySync to wait before checking for new resources or changes to existing resources. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RESOURCE_SYNC_INTERVAL
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *60*
      - **Example:** `300`

**sync.tagdef.enable** - Specifies whether to sync tags from AWS Lake Formation to Lake Formation Connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable Tags Sync
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SYNC_TAGDEF_ENABLE
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**sync.resourcetag.enable** - Specifies whether to sync tag resource mapping from AWS Lake Formation to Lake Formation Connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable Tag Resource mapping Sync
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SYNC_RESOURCE_TAG_ENABLE
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**sync.resourcepolicy.enable** - Specifies whether to sync resource policies from AWS Lake Formation to Lake Formation Connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable Resource Permissions Sync
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SYNC_RESOURCE_POLICY_ENABLE
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**sync.tagpolicy.enable** - Specifies whether to sync tag policies from AWS Lake Formation to Lake Formation Connector. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable Tag Permissions Sync
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SYNC_TAG_POLICY_ENABLE
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**sync.iam.role.enable** - Specifies whether to sync IAM roles from AWS IAM to Privacera Roles. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable AWS IAM Roles Sync
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SYNC_IAM_ROLE_ENABLE
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**reconcile.resourcepolicy.enable** - Specifies whether to reconcile resource policies between AWS Lake Formation and Lake Formation Connector at certain intervals. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable Reconcile Resource Policies from Ranger
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RECONCILE_RESOURCE_POLICY_ENABLE
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**reconcile.tagpolicy.enable** - Specifies whether to reconcile tag policies between AWS Lake Formation and Lake Formation Connector at certain intervals. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable Reconcile Tag Policies from Ranger
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RECONCILE_TAG_POLICY_ENABLE
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**reconcile.resourcetags.enable** - Specifies whether to reconcile tag resource mapping between AWS Lake Formation and Lake Formation Connector at certain intervals. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable Reconcile Tag Resource mapping from Ranger
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RECONCILE_RESOURCETAGS_ENABLE
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**tagdef.interval.sec** - Specifies the time interval for loading tag defs from Lake formation into Policy Sink services. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_TAGDEF_SYNC_INTERVAL
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *3600*
      - **Example:** `1800`

**resourcetag.interval.sec** - Specifies the time interval for loading tag resource mapping from Lake formation into Policy Sink services. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RESOURCE_TAG_SYNC_INTERVAL
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *3600*
      - **Example:** `1800`

**resourcepolicy.interval.sec** - Specifies the time interval for loading resource permissions from Lake formation into Policy Sink services. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RESOURCE_POLICY_SYNC_INTERVAL
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *3600*
      - **Example:** `1800`

**tagpolicy.interval.sec** - Specifies the time interval for loading tag permissions from Lake formation into Policy Sink services. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_TAG_POLICY_SYNC_INTERVAL
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *3600*
      - **Example:** `1800`

**iam.role.interval.sec** - Specifies the time interval for loading AWS IAM Roles from Lake formation into Policy Sink services. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IAM_ROLE_SYNC_INTERVAL
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *3600*
      - **Example:** `1800`

**reconcile.resourcepolicy.interval.sec** - Specifies the time interval for reconcile resource policies from Policy Sink services. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RECONCILE_RESOURCE_POLICY_INTERVAL
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *3600*
      - **Example:** `1800`

**reconcile.tagpolicy.interval.sec** - Specifies the time interval for reconcile tag policies from Policy Sink services. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RECONCILE_TAG_POLICY_INTERVAL
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *3600*
      - **Example:** `1800`

**reconcile.resourcetags.interval.sec** - Specifies the time interval for reconcile tag resource mapping from Policy Sink services. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_RECONCILE_RESOURCETAGS_INTERVAL
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *3600*
      - **Example:** `1800`

## Resource Management

**manage.catalog.list** - Specifies a comma-separated list of AWS Catalogs for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Catalogs to set access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_CATALOG_LIST
      - **Property Type:** Basic
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX, 987654321XXX, 1234*`

**manage.data_location.list** - Specifies a comma-separated list of Data locations for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Data Locations to set access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_DATA_LOCATION_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.demo-s3-bucket/test_data*`

**manage.database.list** - Specifies a comma-separated list of database names for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_DATABASE_LIST
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.testdb1, 123456789XXX.us-east-1.testdb2, 123456789XXX.us-east-1.sales_db*`

**manage.database_resource_link.list** - Specifies a comma-separated list of database resource links for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Database Resource Links to set access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_DATABASE_RESOURCE_LINK_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.testdb1, 123456789XXX.us-east-1.testdb2, 123456789XXX.us-east-1.sales_db*`

**manage.table.list** - Specifies a comma-separated list of table names for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_TABLE_LIST
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.testdb1.test_table1, 123456789XXX.us-east-1.testdb2.test_table2, 123456789XXX.us-east-1.sales_db.sales_data*`

**manage.table_resource_link.list** - Specifies a comma-separated list of table resource links for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_TABLE_RESOURCE_LINK_LIST
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.testdb1.test_table1, 123456789XXX.us-east-1.testdb2.test_table2, 123456789XXX.us-east-1.sales_db.sales_data*`

**manage.tag.list** - Specifies a comma-separated list of tags for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_TAG_LIST
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.test_tag1, 123456789XXX.us-east-1.test_tag2, 123456789XXX.us-east-1.sales_db_tag*`

**ignore.catalog.list** - Specifies a comma-separated list of AWS catalog ids that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Catalogs to ignore for access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_CATALOG_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX, 987654321XXX, 1234*`

**ignore.data_location.list** - Specifies a comma-separated list of data locations that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Data Locations to ignore for access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_DATA_LOCATION_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.demo-s3-bucket/test_data*`

**ignore.database.list** - Specifies a comma-separated list of database names that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_DATABASE_LIST
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.testdb1, 123456789XXX.us-east-1.testdb2, 123456789XXX.us-east-1.sales_db*`

**ignore.database_resource_link.list** - Specifies a comma-separated list of database resource links that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Database Resource Links to ignore for access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_DATABASE_RESOURCE_LINK_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.testdb1, 123456789XXX.us-east-1.testdb2, 123456789XXX.us-east-1.sales_db*`

**ignore.table.list** - Specifies a comma-separated list of table names that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_TABLE_LIST
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.testdb1.test_table1, 123456789XXX.us-east-1.testdb2.test_table2, 123456789XXX.us-east-1.sales_db.sales_data*`

**ignore.table_resource_link.list** - Specifies a comma-separated list of table resource links that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_TABLE_RESOURCE_LINK_LIST
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.testdb1.test_table1, 123456789XXX.us-east-1.testdb2.test_table2, 123456789XXX.us-east-1.sales_db.sales_data*`

**ignore.tag.list** - Specifies a comma-separated list of tag names that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_TAG_LIST
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `123456789XXX.us-east-1.test_tag1, 123456789XXX.us-east-1.test_tag2, 123456789XXX.us-east-1.sales_db_tag*`

**lf.manage.database.list** - Specifies a comma-separated list of database names for which PolicySync manages access control across the specified regions. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Database names to set access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_LF_MANAGE_DATABASE_LIST
      - **Property Type:** Basic
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `testdb1, testdb2, sales_db*`

**lf.ignore.database.list** - Specifies a comma-separated list of database names that PolicySync does not provide access control across specified regions. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Database names to ignore for access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_LF_IGNORE_DATABASE_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `testdb1, testdb2, sales_db*`

## Users/Groups management

**manage.service.user** - Set this to true if you want PolicySync to handle LakeFormation users create/update/delete based on portal users create/update/delete. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_SERVICE_USER
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**manage.service.group** - Set this to true if you want PolicySync to handle LakeFormation groups create/update/delete based on portal groups create/update/delete. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_SERVICE_GROUP
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**manage.service.group.members** - Set this to true if you want PolicySync to handle LakeFormation group members create/update/delete based on portal group members create/update/delete. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_SERVICE_GROUP_MEMBERS
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**manage.service.role** - Set this to true if you want PolicySync to handle LakeFormation roles create/update/delete based on portal roles create/update/delete. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_SERVICE_ROLE
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**manage.service.role.members** - Set this to true if you want PolicySync to handle LakeFormation role members create/update/delete based on portal role members create/update/delete. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_SERVICE_ROLE_MEMBERS
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**manage.user.list** - Specifies a comma-separated list of user names for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Users to set access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_USER_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `user1,user2,dev_user*`

**manage.group.list** - Specifies a comma-separated list of group names for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Groups to set access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_GROUP_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `group1, group2, dev_group*`

**manage.role.list** - Specifies a comma-separated list of role names for which PolicySync manages access control. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Roles to set access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_MANAGE_ROLE_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `role1, role2, dev_role*`

**ignore.user.list** - Specifies a comma-separated list of user names that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Users to be ignored by access control policies


      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_USER_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `user1,user2,dev_user*`

**ignore.group.list** - Specifies a comma-separated list of group names that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Groups to be ignored by access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_GROUP_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `group1, group2, dev_group*`

**ignore.role.list** - Specifies a comma-separated list of role names that PolicySync does not provide access control for. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Roles to be ignored by access control policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_IGNORE_ROLE_LIST
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `role1, role2, dev_role*`

**use.native.public.group** - Set this property to true if you want PolicySync to use LakeFormation native public group for access grants whenever there is a policy created referring to a public group inside it. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Use lake formation native public group for public group access policies
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_USE_NATIVE_PUBLIC_GROUP
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

## Access control management

**enable.row.filter** - Specifies whether to use native row filtering. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enforce lakeformation native row filter
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_ENABLE_ROW_FILTER
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *true*
      - **Example:** `true`

**perform.grant.updates** - Specifies whether PolicySync performs grants and revokes for access control and creates, updates, and deletes API calls for users, groups, and roles. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable policy enforcements and user/group/role management
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_ENABLE_GRANT_UPDATES
      - **Property Type:** Basic
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

## Access audits management
**enable.audit** - Specifies whether Privacera should retrieve access audit data from the LakeFormation. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable access audits
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_ENABLE_ACCESS_AUDITS
      - **Property Type:** Basic
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**audit.excluded.users** - Specifies a list of users to exclude when fetching access audits. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Users to exclude when fetching access audits
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AUDIT_EXCLUDED_USERS
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `user1,user2,user3`

**audit.excluded.access.types** - Specifies a list of access types to exclude when fetching access audits. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AUDIT_EXCLUDED_ACCESS_TYPES
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `StartQueryExecution, GetTable, DeleteTable, CreateTable, CreateDatabase`

**aws.athena.region** - Specifies AWS Athena region to create JDBC connection for LakeFormation audit logs database. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_ATHENA_REGION
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `us-west-2`

**aws.athena.endpoint** - Specifies AWS Athena endpoint to create JDBC connection for LakeFormation audit logs database. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_ATHENA_ENDPOINT
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `athena.us-west-2.amazonaws.com:443`

**aws.athena.workgroup** - Specifies AWS Athena workgroup to create JDBC connection for LakeFormation audit logs database. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AWS_ATHENA_WORKGROUP
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `Primary`

**audit.db.name** - Specifies AWS audit database to store LakeFormation audit logs. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Lake formation audit logs database
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AUDIT_DB_NAME
      - **Property Type:** Basic
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `lf_audit_db`

**audit.table.name** - Specifies AWS audit table to store LakeFormation audit logs. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Lake Formation audit logs table name
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AUDIT_TABLE_NAME
      - **Property Type:** Basic
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `lf_audit_table`

**aws.athena.s3.output.location** - Specifies S3 location to store the access audit logs query results. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** S3 output location for access audit logs query results
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_AUDIT_ATHENA_S3_OUTPUT_LOCATION
      - **Property Type:** Basic
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `s3://privacera-dev-XXX/<LF_audit_logs_folder>/athena_query_results/`

**enable.push.policies.ranger** - Specifies whether to enable pushing LakeFormation policies in other policy repositories. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable push policies to ranger
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_ENABLE_PUSH_POLICIES_TO_RANGER
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

## Reverse Sink Properties

**permissions.sink.type** - Specifies LakeFormation permissions sink type. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Lake formation permissions sink type
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_PERMISSION_SINK_TYPE
      - **Property Type:** Basic
      - **Mandatory:** Yes
      - **Type:** String
      - **Default:** *None*
      - **Example:** `reverse_sink`

**sink.maxindex** - Specifies LakeFormation sink max index is number of max services can be configured for reverse sink. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Custom Property
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SINK_MAX_INDEX
      - **Property Type:** Custom
      - **Mandatory:** No
      - **Type:** Integer
      - **Default:** *1*
      - **Example:** `2`

**sink.hive.enabled** - Specifies whether to enable policy sink to Hive Service. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Push Lake formation permissions to hive policy repository
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SINK_HIVE_ENABLED
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**sink.hive.ranger.service.appid** - Specifies the policy repository name for Hive service. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Policy repository name for hive service
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SINK_HIVE_SERVICE_APP_ID
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `hive_repo`

**sink.default.enabled** - Specifies whether to enable policy sink to LakeFormation Service. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Push Lake formation permissions to lake formation policy repository
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SINK_LAKEFORMATION_ENABLED
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`

**sink.default.ranger.service.appid** - Specifies the policy repository name for LakeFormation service. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Policy repository name for lake formation service
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SINK_LAKEFORMATION_SERVICE_APP_ID
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `lakeformation_repo`

**sink.default.ranger.tag.service.appid** - Specifies the policy repository name for Tag service. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Policy repository name for tag service
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_SINK_TAG_SERVICE_APP_ID
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** String
      - **Default:** *None*
      - **Example:** `tag_repo`

**create.readonly.policies** - Specifies whether policies created by PolicySync should be editable or not. (1)
{ .annotate }

  1.  - **PrivaceraCloud Field Name:** Enable read only policy creation
      - **Self Managed/Data Plane:** CONNECTOR_LAKEFORMATION_ENABLE_CREATE_READONLY_POLICIES
      - **Property Type:** Advanced
      - **Mandatory:** No
      - **Type:** Boolean
      - **Default:** *false*
      - **Example:** `true`
`
