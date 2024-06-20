---
Title: Prerequisites for Lake Formation Push Mode
---

# Prerequisites for Lake Formation Push Mode

AWS Lake Formation connector with Privacera using the Push mode requires the following prerequisites:

## Mandatory Prerequisites

| Prerequisites                                                                                                                                              | Detail                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IAM policies for managing Lake Formation Policies. [Refer](#iam-policies-for-managing-lake-formation)                                                      | This is used to update the policies in AWS Lake Formation                                                                                                                                                                                                            |
| IAM policies to read from Glue Data Catalog [Refer](#iam-policies-to-read-from-glue-data-catalog)                                                          | This is used the retrieve the list of databases and tables from AWS Glue Catalog.                                                                                                                                                                                    |
| IAM policies to retrieve IAM Roles [Refer](#iam-policies-to-retrieve-iam-roles)                                                                            | This is used to retrieve the list of roles and users from AWS IAM. The permissions will be only managed for the users and roles in the IAM                                                                                                                           |
| IAM role for the Privacera Connector [Refer](#iam-role-for-the-privacera-connector)                                                                        | IAM Role which consists of all the IAM policies that are required by this connector                                                                                                                                                                                  |
| Allow Privacera to manage the policies in your AWS Lake Formation                                                                                          | Allow the IAM role used by the Privacera Lake Formation connector to be the administrator Lake Formation policies [Refer](#lake-formation-administrator-configuration)                                                                                                                                         |
| ==[Self Managed/Data Plane :material-wall-fire:]== Kubernetes pod with access to the IAM Role                                                              | If the Lake Formation connector is deployed in your VPC, then the Kubernetes pod should have access to the IAM role to manage the policies in AWS Lake Formation.                                                                                                    |
| ==[PrivaceraCloud :material-cloud-key-outline:]== Trust Policy to PrivaceraCloud for the IAM Role [Refer](#trust-policy-to-privaceracloud-for-the-iam-role) | If the Lake Formation connector is deployed in PrivaceraCloud, then the IAM Role should have a trust policy to PrivaceraCloud to manage the policies in your AWS Lake Formation. This should be attached to the role from the PrivaceraCloud. [check here](#trust-policy-to-privaceracloud-for-the-iam-role) |

## Optional Prerequisites

| Prerequisites                                                                                             | Detail                                                                                             |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| IAM policies for sharing resource across AWS Accounts. [Refer](#iam-policies-for-sharing-resource-across-aws-accounts) | This policy is required if you are managing policies in other AWS Accounts. [Additional Details](#iam-policies-for-sharing-resource-across-aws-accounts) |

## Appendix

### IAM Policies for managing Lake Formation

The following IAM policies are required to update the policies in AWS Lake Formation. You can name it `privacera-lf-push-policy`.

/// details | privacera-lf-push-policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
              "lakeformation:ListDataCellsFilter",
              "lakeformation:GetEffectivePermissionsForPath",
              "lakeformation:ListLFTags",
              "lakeformation:GetLFTag",
              "lakeformation:ListPermissions",
              "lakeformation:GetResourceLFTags",
              "lakeformation:DescribeResource",
              "lakeformation:ListResources",
              "lakeformation:GetTableObjects",
              "lakeformation:BatchGrantPermissions",
              "lakeformation:GrantPermissions",
              "lakeformation:DeleteDataCellsFilter",
              "lakeformation:RevokePermissions",
              "lakeformation:CreateDataCellsFilter",
              "lakeformation:BatchRevokePermissions"              
            ],
            "Resource": "*"
        }
    ]
}
```
///

### IAM policies to read from Glue Data Catalog

The following IAM policies are required to read from the Glue Data Catalog. You can name it 
`privacera-lf-glue-read-policy`. This connector doesn't require write access to the Glue Data Catalog.

/// details | privacera-lf-glue-read-policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "glue:GetTables",
        "glue:GetTableVersions",
        "glue:GetDatabases",
        "glue:GetTable",
        "glue:GetDatabase",
        "glue:GetTableVersion",
        "glue:GetColumnStatisticsForTable"
      ],
      "Resource": "*"
    }
  ]
}
```
///

### IAM policies to retrieve IAM Roles

The following IAM policies are required to retrieve the IAM roles. You can name it `privacera-lf-iam-read-policy`.
This connector doesn't require write access to the IAM roles and it will not create or modify any IAM roles.

/// details | privacera-lf-iam-read-policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:ListRoles",
        "iam:ListGroups",
        "iam:ListUsers"
      ],      
      "Resource": "*"
    }
  ]
}
```
///

### IAM policies for sharing resource across AWS Accounts

The following IAM policies are required to share resources across AWS Accounts. You can name it `privacera-lf-share-policy`.
If you are using the Data Mesh design pattern and/or sharing resources across AWS accounts, you need to add additional
permissions so that Privacera can manage the policies in the shared resources in other accounts also.

/// details | privacera-lf-share-policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ram:CreateResourceShare",
        "ram:GetResourceShares",
        "ram:AssociateResourceShare",
        "ram:DisassociateResourceShare",
        "ram:DeleteResourceShare"
      ],
      "Resource": "*"
    }
  ]
}
```
///

### IAM Role for the Privacera Connector

The following IAM role is required for the Privacera Connector. You can name it `privacera-lf-push-connector-role`.

/// details | privacera-lf-push-connector-role
Include the following policies in the IAM role:

- [x] privacera-lf-push-policy
- [x] privacera-lf-glue-read-policy
- [x] privacera-lf-iam-read-policy
- [ ] privacera-lf-share-policy [Optional]

///


### Lake Formation Administrator Configuration

The IAM Role used by the Privacera Lake Formation connector should have the administrator privileges to manage the policies Lake Formation

1. Log in to AWS Account and navigate to AWS Lake Formation > Administrative roles and tasks. 
2. Click ==[Add]== in the **Data lake administrators** section
3. For **Access Type** ==[Data lake administrator]== search for the role that was created for Privacera Lake Formation e.g. `privacera-lf-push-connector-role` and select it. 
3. Click ==[Confirm]==.

### Trust Policy to PrivaceraCloud for the IAM Role

If the Lake Formation connector is deployed in PrivaceraCloud, then the IAM Role should have a trust policy to
PrivaceraCloud to manage the policies in your AWS Lake Formation. This should be attached to the role from the
PrivaceraCloud. Go to the AWS IAM console and attach the following trust policy to the IAM Role you created for the
Privacera Lake Formation connector.

!!! info "Update <ROLE_ARN>"
    Please contact Privacera support to get the `<ROLE_ARN>` for the PrivaceraCloud.


/// details | Trust Policy to PrivaceraCloud for the IAM Role
```json
{
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "<ROLE_ARN>"
    ]
  },
  "Action": "sts:AssumeRole"
}

```
///


<div class="grid cards" markdown>
-   :material-page-previous: Prev topic: [Push Mode Overview](./index.md)
-   :material-page-next: Next topic: [Setup](setup.md)
</div>
