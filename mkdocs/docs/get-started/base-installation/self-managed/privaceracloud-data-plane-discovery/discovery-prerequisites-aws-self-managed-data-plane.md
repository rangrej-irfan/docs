
## Overview

When running Privacera Discovery in AWS, the following cloud resources are required - 

- AWS S3 bucket and path - to store the Privacera meta-data - Mandatory with read/write permissions
- AWS DynamoDB tables - to store the Privacera meta-data - Mandatory with read/write permissions
- AWS SQS - to store the Privacera meta-data - Optional, only for real-time discovery of S3 buckets
- AWS IAM roles for Service Accounts - to provide access to the AWS resources for the Privacera Discovery pods

Privacera Manager has the ability to create the S3 bucket, DynamoDB tables and SQS using Terraform. 
This means the instance role of the Privacera Manager host needs the permissions to create these resources.
If this is not allowed then you can create these cloud resources and configure Privacera Manager to use
these resources.

The AWS IAM roles for Service Accounts have to be created by you and the ARN of these roles have to be provided
to Privacera Manager. 


| Prerequisite                                                                                       | Description                                                                                                                                  |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [Discovery S3 Configuration Bucket](#discovery-s3-configuration-bucket)                           | AWS S3 bucket and path - to store the Privacera meta-data - Mandatory with read/write permissions.                                           |
| [Discovery DynamoDB Tables](#discovery-dynamodb-tables)                                             | AWS DynamoDB tables - to store the Privacera meta-data - Mandatory with read/write permissions.                                              |
| [Discovery SQS](#discovery-sqs)                                                                     | AWS SQS - to store the Privacera meta-data - Optional, only for real-time discovery of S3 buckets.                                           |
| [Discovery scan buckets](#discovery-scan-buckets)                                                   | AWS S3 buckets to be scanned by Privacera Discovery.                                                                                        |
| [Additional IAM policy on PM EC2 instance](#additional-iam-policy-on-pm-ec2-instance)                                           | Additional IAM policies in the Privacera Manager EC2 host to be able to create AWS resources for Discovery such as DynamoDB tables and SQS.  |
| [IAM Role for Service Account for Discovery Driver and Executor Pods](#iam-role-for-service-account-for-discovery-drivera-and-executor-pods) | IAM Role for Service Account used by Discovery Driver and Executor Pods to access AWS resources.                                             |
| [IAM Role for Service Account for Discovery Consumer Pod](#iam-role-for-service-account-for-discovery-consumer-pod)    | IAM Role for Service Account used by Discovery Consumer Pod to access AWS resources.                                                         |
| [IAM Role for Service Account for Portal pod](#iam-role-for-service-account-for-portal-pod)                            | IAM Role for Service Account used by Portal pod to access AWS resources.                                                                     |


## Appendix

### Discovery S3 Configuration Bucket

```json
BUCKET 
or BUCKET/PATH
The IRSA for discovery driver and executor needs read/write permission 
to this bucket and path
```

### Discovery DynamoDB Tables
```bash
explain the tables naming convention and give list of tables
so that customer can create them manually or verify afterwards if PM is going
to creat them
```
### Discovery SQS

```bash 
explain the SQS naming convention and give list of SQS
```

### Discovery scan buckets

```bash
explain why the discovery pods require listing and read permission on these buckets
and how to enable events for real-time scanning
```

### Additional IAM policy on PM EC2 instance

??? note "Additional IAM policy on PM EC2 instance"
    The following additional IAM policy needs to be attached to the Privacera Manager EC2 instance to be able to create AWS resources for Discovery such as DynamoDB tables and SQS.
    
    ```json
         {
        "Version":"2012-10-17",
        "Statement":[
            {
                "Sid":"CreateDynamodb",
                "Effect":"Allow",
                "Action":[
                    "dynamodb:CreateTable",
                    "dynamodb:DescribeTable",
                    "dynamodb:ListTables",
                    "dynamodb:TagResource",
                    "dynamodb:UntagResource",
                    "dynamodb:UpdateTable",
                    "dynamodb:UpdateTableReplicaAutoScaling",
                    "dynamodb:UpdateTimeToLive",
                    "dynamodb:DescribeTimeToLive",
                    "dynamodb:ListTagsOfResource",
                    "dynamodb:DescribeContinuousBackups"
                ],
                "Resource":"arn:aws:dynamodb:${AWS_REGION}:*:table/privacera*"
            },
            {
                "Sid":"CreateS3Bucket",
                "Effect":"Allow",
                "Action":[
                    "s3:CreateBucket",
                    "s3:ListAllMyBuckets",
                    "s3:GetBucketLocation"
                    
                ],
                "Resource":[
                    "arn:aws:s3:::<DISCOVERY_BUCKET>"
                ]
            },
            {
                "Sid":"CreateSQSMessages",
                "Effect":"Allow",
                "Action":[
                    "sqs:CreateQueue",
                    "sqs:ListQueues"
                ],
                "Resource":[
                    "arn:aws:sqs:<AWS_REGION>:<ACCOUNT_ID>:privacera*"
                ]
            }
        ]
        }
    ```

### IAM Role for Service Account for Discovery Drivera and Executor Pods

```bash
this should have read/write access to the discovery bucket
and listing and read permission to the scan buckets
and read/write access to the dynamodb tables
```
### IAM Role for Service Account for Discovery Consumer Pod
```bash 
and read/write access to the dynamodb tables
```

### IAM Role for Service Account for Portal Pod
```bash
and read/write access to the dynamodb tables
and read/write access to the discovery bucket
```