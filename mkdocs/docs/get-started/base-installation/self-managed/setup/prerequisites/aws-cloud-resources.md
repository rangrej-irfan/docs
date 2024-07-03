# AWS Cloud Resources

## Overview
Following AWS cloud resources need to be created before installing the Privacera Manager software:

| Prerequisite | Description                                                                                                                                                                                                                                               |
| --- |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AWS EC2 instance](#aws-ec2-instance) | EC2 instance to run the Privacera Manager software.<br>:green_circle: Self-managed: Required<br>:green_circle: PrivaceraCloud Data-plane: Required<br>:green_circle: PrivaceraCloud Data-plane + Privacera Discovery: Required.                           |
| [AWS EKS cluster](#aws-eks-cluster) | EKS cluster to run the Privacera software.<br>:green_circle: Self-managed: Required<br>:green_circle: PrivaceraCloud Data-plane: Required<br>:green_circle: PrivaceraCloud Data-plane + Privacera Discovery: Required.                                    |
| [AWS RDS AuroraDB](#aws-rds-auroradb) | RDS AuroraDB instance for the Privacera database.<br>:green_circle: Self-managed: Required<br>:no_entry_sign: PrivaceraCloud Data-plane: Not Required<br>:green_circle: PrivaceraCloud Data-plane + Privacera Discovery: Required.                        |
| [AWS ACM certificate](#aws-acm-certificate) | ACM certificate for the domain name used for the Privacera service endpoints.<br>:green_circle: Self-managed: Required<br>:green_circle: PrivaceraCloud Data-plane: Required<br>:green_circle: PrivaceraCloud Data-plane + Privacera Discovery: Required. |


## Appendix
### AWS EC2 instance
??? note "EC2 instance"

    An AWS EC2 instance needs to be provisioned to run the Privacera Manager software. The instance should have the
    following specifications:  
    
    - AWS Linux 2 AMI
    - Minimum 1 vCPUs
    - Minimum 4 GB RAM
    - Minimum 50 GB disk space  
    - SELinux should be disabled

    Only an AWS EC2 instance with the above configuration is supported for running the Privacera Manager software.   

    It should be associated with your EKS cluster so that you can run kubectl command.

    It should have an instance role with following IAM permissions:    
    
    ??? note "Permissions to access the EKS cluster for running kubectl commands"
        In addition to the following IAM policy, you would need to do additional 
        steps to authorize your EC2 instance to access the EKS cluster.

        ```json
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
    ??? note "Permissions to write to the S3 bucket"
        You will need a S3 bucket policy if you are going to configure Privacera Discovery module.
        ```json
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
        ```json
        ```
    ??? note "Permissions to update the Route53 DNS entries (optional)"
        For this policy you need the AWS hosted zone ID. You can find the hosted zone ID in the Route53 console.
        This policy is optional if you want do not want Privacera Manager to update the Route53 DNS entry .
        ```json
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

    !!! note 
        The Privacera Manager installation on this EC2 instance will contain self-signed certificates and 
        terraform state. As such, the contents of the Privacera Manager folder should be backed up regularly.
    
        You don't need to run this instance 24x7. You can stop the instance when not in use.

### AWS EKS cluster
??? note "AWS EKS"

    AWS EKS cluster with the following specifications:

    - Kubernetes version (look this TBD-link)
    - Node type - r5.2xlarge or similar
    - Auto-scaling node group - min 3 to max 10 nodes
    - EFS is recommended for multi-availability zone setup, [follow these instructions](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html){:target="_blank"}
    - AWS load balancer for the EKS cluster [follow these instructions](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html){:target="_blank"}

### AWS RDS AuroraDB
??? note "AWS RDS AuroraDB"

    AWS RDS AuroraDB instance with the following specifications:
    
    - RDS AuroraDB (MySQL 5.7) 2.11.2  (MySQL 8 is also fine)
    - db.r6g.2xlarge = 8 cpu, 64 gb
    - only password authentication
    - default charset to latin1, collation latin1_swedish_ci
    - create privacera_db as the database by following these commands
        ```sql
        create database privacera_db character set latin1 collate latin1_swedish_ci;
        ```
### AWS ACM certificate
??? note "AWS ACM certificate"
    AWS ACM certificate for the domain name that you will use for the Privacera service endpoints.
    This should either be a wild-card certificate or a certificate with specific host names generated by 
    Privacera Manager or a certificate with specific host names generated by you for the service endpoints.

<div class="grid cards" markdown>
-  :material-page-previous: Prev [Prerequisites](index.md)
-  :material-page-next: Next [Privacera Manager Setup](../privacera-manager-setup.md)
</div>

