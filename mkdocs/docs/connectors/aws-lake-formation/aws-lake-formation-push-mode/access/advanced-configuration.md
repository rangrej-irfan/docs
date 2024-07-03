---
title: Advanced Configuration for LakeFormation Connector in Push Mode - Access Management
---

# Advanced Configuration for LakeFormation Connector in Push Mode - Access Management

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
