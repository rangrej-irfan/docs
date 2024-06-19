# Basic Configuration for AWS Lake Formation Push Mode

## Connection Details
1. Account Id
2. AWS Region

## Synchronize with other Hive Metastore Data Sources like Databricks, Trino, etc.
1. Enable Push Policies to other services
2. Name of the service application id



---

* `CONNECTOR_LAKEFORMATION_ENABLE_PUSH_POLICIES_TO_RANGER` \- Set this to true, if you want to push policies to other policy repositories.

    * `CONNECTOR_LAKEFORMATION_SINK_HIVE_SERVICE_APP_ID` \- Set the policy repository name where you want the connector to push policies for the hive.


### **AWS Account ID**
=== "Self Managed and Data Plane"

    | Variable Name                        |
    |--------------------------------------|
    | CONNECTOR_LAKEFORMATION_AWS_REGION |

=== "PrivaceraCloud"

    | Field Name                        |
    |--------------------------------------|
    | AWS Account ID |

 /// details | This is the AWS Account ID of the account where the AWS Lake Formation
**Mandatory:** Yes  
**Type:** String  
**Default:** *None*  
**Example:** `123456789012`
///
