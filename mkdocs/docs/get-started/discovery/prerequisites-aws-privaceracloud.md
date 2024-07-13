
## Overview
Following AWS cloud resources need to be created before installing the Privacera Manager software:

```bash
discovery scan buckets and events for real-time discovery
IAM role for scanning buckets and trust-relation with PrivaceraCloud role
```

| Prerequisite                                             | Description                                                                                                                                 |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [Additional IAM policy on PM EC2 instance](#aws-account) | Additional IAM policies in the Privacera Manager EC2 host to be able to create AWS resources for Discovery such as DynamoDB tables and SQS. |

### Additional IAM policy on PM EC2 instance

