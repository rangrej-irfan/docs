# AWS Cloud Resources

## Overview
Following AWS cloud resources need to be created before installing the Privacera Manager software:

| Prerequisite | Description                                                                                                                                                                                                                                                                         |
| --- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AWS EC2 instance](#aws-ec2-instance-for-running-privacera-manager) | EC2 instance to run the Privacera Manager software. Refer [here](#aws-ec2-instance) for more details<br>:green_circle: Self-managed: Required<br>:green_circle: PrivaceraCloud Data-plane: Required<br>:green_circle: PrivaceraCloud Data-plane + Privacera Discovery: Required.    |
| [AWS EKS cluster](#aws-eks-cluster-for-running-privacera-software) | EKS cluster to run the Privacera software. Refer [here](#aws-eks-cluster) for more details<br>:green_circle: Self-managed: Required<br>:green_circle: PrivaceraCloud Data-plane: Required<br>:green_circle: PrivaceraCloud Data-plane + Privacera Discovery: Required.              |
| [AWS RDS AuroraDB](#aws-rds-auroradb) | RDS AuroraDB instance for the Privacera database. Refer [here](#aws-rds-auroradb) for more details<br>:green_circle: Self-managed: Required<br>:no_entry_sign: PrivaceraCloud Data-plane: Not Required<br>:green_circle: PrivaceraCloud Data-plane + Privacera Discovery: Required. |
| [AWS ACM certificate](#aws-acm-certificate) | ACM certificate for the domain name used for the Privacera service endpoints. Refer [here](#aws-acm-certificate) for more details<br>:green_circle: Self-managed: Required<br>:green_circle: PrivaceraCloud Data-plane: Required<br>:green_circle: PrivaceraCloud Data-plane + Privacera Discovery: Required.                          |


## Appendix
### AWS EC2 instance for running Privacera Manager
??? note "EC2 instance"

    Privacera Manager is ran from an EC2 instance which has access to Kubernetes and other cloud resources that 
    are needed for installating and managing Privacera. For that, from the this EC2 instance it should be able to 
    connect and managed EKS cluster. And it should have an instance role as per this section.    

    !!! note 
        The Privacera Manager installation on this EC2 instance will contain self-signed certificates and 
        terraform state. These are needed for subsequent upgrades. So it is recommended that this EC2 is not 
        deleted and protected for termination. It is also strongly recommended to backup the contents of the 
        Privacera Manager folder on regular basis.
    
        You don't need to run this instance 24x7. You can stop the instance when not in use.

    ??? note "EC2 configuration"
        An AWS EC2 instance needs to be provisioned to run the Privacera Manager software. At the minimum, the instance 
        should have the following specifications:  
        
        - AWS Linux 2 AMI
        - Minimum 1 vCPUs
        - Minimum 4 GB RAM
        - Minimum 50 GB disk space  
        - SELinux should be disabled

    
    ??? note "Permissions to access the EKS cluster for running kubectl commands"
        In addition to the following IAM policy, you would need to do additional 
        steps to authorize your EC2 instance to access the EKS cluster.

        ```{.json title="privacera-manager-eks-policy"}
        {
         "Version": "2012-10-17",
         "Statement": [
           {
             "Effect": "Allow",
             "Action": [
               "eks:describeCluster"
             ],
             "Resource": "*"
           }
         ]
        }
        ```
    ??? note "Permissions to write to the S3 bucket (optional)"
        You will need a S3 bucket policy if you are going to configure Privacera Discovery module. You need to 
        update the ==bucket-name== and ==path== in the policy below.
        ```{.json title="privacera-manager-s3-policy"}
        {
         "Version": "2012-10-17",
         "Statement": [
           {
             "Effect": "Allow",
             "Action": [
               "s3:PutObject",
               "s3:GetObject",
               "s3:ListBucket",
               "s3:DeleteObject"
             ],
             "Resource": [
               "arn:aws:s3:::<bucket-name>/<path>/*",
               "arn:aws:s3:::<bucket-name>"
             ]
           }
         ]
        }
        ```
    ??? note "Permissions to update the Route53 DNS entries (optional)"
        Privacera Manager can optionally add the DNS records using Route53 for the Privacera service endpoints.
        Update the ==hosted-zone-id== in the policy below. You can find the hosted zone ID in the Route53 console.
        ```{ .json title="privacera-manager-route53-policy"}
        {
         "Version": "2012-10-17",
         "Statement": [
           {
             "Sid": "AllowRoute53Update",
             "Effect": "Allow",
             "Action": [
               "route53:ChangeResourceRecordSets",
               "route53:ListResourceRecordSets",
               "route53:GetHostedZone",
               "route53:GetChange"
             ],
             "Resource": [
               "arn:aws:route53:::hostedzone/<hosted-zone-id>",
               "arn:aws:route53:::change/*"
             ]
           }
         ]
        }
        ```
    ??? note "Permissions to run eksctl to create IAM role for Service Account (optional)"
        You can use the IAM role [from this link](https://eksctl.io/usage/minimum-iam-policies/){:target="_blank"}.

    Following software should be installed on the EC2 instance:

    ??? note "docker"
        ```bash
        sudo yum update -y
        sudo amazon-linux-extras install docker
        sudo service docker start
        sudo usermod -a -G docker ec2-user
        
        # log out and log back into the EC2 instance to activate the new group
        docker ps
        ```
    
    ??? note "kubectl"
        Follow the instructions [on this link](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html){:target="_blank"}.

    ??? note "helm"
        Follow the instructions [on this link](https://helm.sh/docs/intro/install/){:target="_blank"}.
        ```bash
        curl -fsSL -o get_helm.sh \
          https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
        chmod 700 get_helm.sh
        ./get_helm.sh
        ```


### AWS EKS cluster for running Privacera Software
??? note "AWS EKS"

    AWS EKS cluster with the following specifications:

    - Kubernetes version - For supported version check [Privacera release notes](../../../../resources/releases/index.md)
    - Node type - r5.2xlarge or similar
    - Auto-scaling node group - min 3 to max 10 nodes
    - EFS is recommended for multi-availability zone setup, [follow these instructions](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html){:target="_blank"}
    - AWS load balancer for the EKS cluster [follow these instructions](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html){:target="_blank"}

### AWS RDS AuroraDB
??? note "AWS RDS AuroraDB"

    AWS RDS AuroraDB instance with the following specifications:
    
    - RDS AuroraDB (MySQL 5.7) 2.11.2  (MySQL 8 is also fine)
    - Minimum db.r6g.2xlarge = 8 cpu, 64 gb
    - Only password authentication is supported
    - Set default charset to latin1, collation latin1_swedish_ci
    - create privacera_db as the database by following these commands
        ```sql
        create database privacera_db character set latin1 collate latin1_swedish_ci;
        ```
### AWS ACM certificate
??? note "AWS ACM certificate"
    AWS ACM certificate for the domain name that you will use for the Privacera service endpoints.
    This should one of these:

    - Wild-card certificate
    - Certificate with specific host names generated by Privacera Manager
    - Certificate with specific host names generated by you for the service endpoints.

<div class="grid cards" markdown>
-  :material-page-previous: Prev [Prerequisites](index.md)
-  :material-page-next: Next [Setup](../setup.md)
</div>

