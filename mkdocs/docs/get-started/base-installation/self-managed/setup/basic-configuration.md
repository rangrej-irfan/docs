# Configure Privacera Manager

!!! note "Prerequisites"
    Before you begin, ensure that you have the installed Privacera Manager by following the steps in 
    the [Setup](setup.md) section.

## Overview

Privacera Manager takes a set of configuration variables that are defined in YAML files. Out of 
the box, several sample variable YAML files are provided that you can use to configure Privacera Manager.
These are in the `config/sample-vars` folder. The process of configuring Privacera Manager involves
copying these sample variable YAML files to the `config/custom-vars` folder and modifying them to suit your 
environment. In some cases, you will create new configuration YAML files and add properties as given in the
documentation. The files under `config/custom-vars` are not overwritten during upgrades.

After you have configured Privacera Manager, you can run the `privacera-manager.sh` script as 
given in the [Using Privacera Manager](using-privacera-manager.md) section.

## Self-Managed and PrivaceraCloud Data-plane

The following are the mandatory configuration steps that you need to perform before you can start using 
Privacera Manager. These steps are common for all cloud providers.

These steps are common for Self-Managed and PrivaceraCloud Data-plane installations.

| #  | Configuration Step                                                      | Description                                                                                                                                                                                                                                                                                  |
|----|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. | [Enable Vault in Privacera Manager](#enable-vault-in-privacera-manager) | Enable Vault in Privacera Manager to store credentials                                                                                        |
| 2. | [Enable Keystores](#enable-use-of-keystores-for-secrets)                | Enable use of keystores at runtime for storing credentials                                                                                  |
| 3. | [Configure Cloud Provider](#configure-your-cloud-provider)              | Configure your cloud provider whether it is AWS, Azure or Google Cloud                                                                         |
| 4. | [Configure Kubernetes](#configure-kubernetes)                           | Configure Kubernetes and Helm                                                                                                                  |
| 5. | [Configure AWS EFS](#configure-aws-efs-optional)                        | Configure AWS EFS (optional - only if you are in AWS and planning to use AWS EFS as Kubernetes volumes)                                        |
| 6. | [Configure External RDBMS](#configure-external-rdbms)                   | Configure External RDBMS to be used for Privacera policy store                                                                                |
| 7. | [Configure TLS](#configure-tls)                                         | Configure TLS                                                                                                                                  |
| 8. | [Configure AWS ALB Controller](#configure-aws-alb-controller-optional)  | Configure AWS ALB Controller (optional - only if you are in AWS and using AWS ALB Controller)                                                  |
| 9. | [Configure Load Balancer](#configure-load-balancer-optional)            | Configure Load Balancer (optional - only if you are in AWS and do not plan to use AWS ALB Controller, and if you are in Azure or Google Cloud) |


## Appendix - Self-Managed and PrivaceraCloud Data-plane

### Enable Vault in Privacera Manager
??? note "Enable Vault"

### Enable use of keystores for secrets
??? note "Enable Keystores"

### Configure your Cloud Provider 
??? note "Configure Cloud Provider"
    Run the following commands to configure your cloud provider. Select the tab
    that corresponds to your cloud provider.
    === "AWS"
        ```bash
        cd ~/privacera/privacera-manager/config
        cp sample-vars/vars.aws.yml custom-vars/
        vi custom-vars/vars.aws.yml
        # set to your AWS region such as us-east-1
        AWS_REGION: "<your AWS region>"
        ```
    === "Azure"
        ```bash
        cd ~/privacera/privacera-manager/config
        cp sample-vars/vars.azure.yml custom-vars/
        ```
    === "Google Cloud"
        ```bash
        cd ~/privacera/privacera-manager/config
        cp sample-vars/vars.gcp.yml custom-vars/
        vi custom-vars/vars.gcp.yml
        # Set the Project ID of your Google Cloud project, this value can be found in the Google Console.
        PROJECT_ID: "<your Google Cloud Project ID>"
        ```

### Configure Kubernetes
??? note "Configure Kubernetes and Helm"
    Run the following commands. This step is common for all cloud providers.

    ```bash
    cd ~/privacera/privacera-manager/config

    cp config/sample-vars/vars.helm.yml config/custom-vars/

    cp sample-vars/vars.kubernetes.yml custom-vars/
    vi custom-vars/vars.kubernetes.yml
    K8S_CLUSTER_NAME: "<cluster name>"
    ```

    In the vars.kubernetes.yml file in your custom-vars folder, you need to put the Kubernetes cluster 
    name that you can obtain by running the following command - 
    ```bash 
    kubectl config get-contexts
    ```

    The output of the above command will be different based on your cloud provider as follows -

    === "AWS"
        ```bash
        # In EKS, you will get the cluster name from the ARN of the cluster
        arn:aws:eks:<region>:<account>:cluster/<cluster-name>

        # The cluster name is the last part of the ARN.
        ```

    === "Azure"        
        ```bash
        # In AKS, you will get the cluster name from the context name
        <cluster-name>
        ```

    === "Google Cloud"
        ```bash
        # In GKE, you will get the cluster name from the context name
        gke_<project-name>_<region>_<cluster-name>
        ```


### Configure AWS EFS (optional)
??? note "Configure AWS EFS"
    This step is required if you are on AWS and plan to use AWS EFS for the storage volumes of pods.
    You will need the EFS ID from the EFS setup done on your EKS cluster for this step. 
    Do not proceed if you don't have the EFS ID.

    If you don't plan on using AWS EFS, but use AWS EBS storage volumes you can skip this step.

    If you are on Azure or Google Cloud, we currently don't support using a managed network file-system
    as a storage volume for the pods.

    Run the following commands - 
    ```bash
    cd ~/privacera/privacera-manager/config/ 
    cp sample-vars/vars.efs.yml custom-vars/
    
    vi custom-vars/vars.efs.yml
    EFS_FSID: "<your EFS ID>"
    ```
    

### Configure External RDBMS
??? note "Configure External RDBMS"
    Run the following commands to configure the external RDBMS that you plan to use with Privacera Manager.

    ```bash 
    cd ~/privacera/privacera-manager/config/
    cp sample-vars/vars.external.db.mysql.yml custom-vars/
    
    vi custom-vars/vars.external.db.mysql.yml
    # Edit these variables with your values. Do not change any other variable values.
    EXTERNAL_DB_HOST: "<PLEASE_CHANGE>"
    EXTERNAL_DB_NAME: "<PLEASE_CHANGE>"
    EXTERNAL_DB_USER: "<PLEASE_CHANGE>"
    EXTERNAL_DB_PASSWORD: "<PLEASE_CHANGE>"
    ```

### Configure TLS
??? note "Configure TLS"
    Run these commands - 
    ```bash 
    cd ~/privacera/privacera-manager/config/
    cp sample-vars/vars.ssl.yml custom-vars/
    
    vi custom-vars/vars.ssl.yml
    # Edit the file and modify these values
    SSL_SELF_SIGNED: "true"
    SSL_DEFAULT_PASSWORD: "welcome1"
    ```
    The above commands will enable TLS for inter-pod communication. 

    Configuring TLS for external access is covered in the Ingres Controller or Load Balancer 
    section below.
    
### Configure AWS ALB Controller (optional)
??? note "Configure Ingress Controller (optional)"
    To access the service endpoints from outside the Kubernetes cluster, you need to configure either
    an Ingress controller such as AWS Load Balancer Controller or an external Load Balancer.

    AWS Load Balancer Controller is supported in AWS.
    
    For Azure and Google Cloud, an ingress controller is not supported currently. You can use an external
    Load Balancer to access the service endpoints.

    If you are on AWS and have installed AWS Load Balancer Controller, then you can run the following commands.

    You will need the following values to configure the AWS ALB Controller -

    - Certificate ARN - a wild card certificate has to be created in ACM
    - Subnets
    - Security Groups
    - Internal (recommended) or Internet-facing load balancer (protected with security group)
    
    You can adjust the annotations as needed based on your requirements.

    Run the following commands to configure the AWS ALB ingress objects - 

    ??? note "vars.aws.alb.ingress.yml"
        ```bash
        cd ~/privacera/privacera-manager
        cp config/sample-vars/vars.aws.alb.ingress.yml config/custom-vars/
        vi vars.aws.alb.ingress.yml
        # Edit the file and modify these values
        AWS_ALB_DEFAULT_ANNOTATIONS:
        - "kubernetes.io/ingress.class: 'alb'"
        - "alb.ingress.kubernetes.io/target-type: 'ip'"
        - "alb.ingress.kubernetes.io/scheme: 'internal'"
        - "alb.ingress.kubernetes.io/backend-protocol: 'HTTPS'"
        - "alb.ingress.kubernetes.io/ssl-redirect: '443'"
        - "alb.ingress.kubernetes.io/listen-ports: '[{\"HTTP\": 80}, {\"HTTPS\":443}]'"
        - "alb.ingress.kubernetes.io/certificate-arn: 'arn:aws:acm:<REGION>:<ID>'"
        - "alb.ingress.kubernetes.io/subnets: '<subnet-1>, <subnet-2>'"
        - "alb.ingress.kubernetes.io/security-groups: '<sg-1234>'"
        - "alb.ingress.kubernetes.io/success-codes: '302,400,401,404'"
        - "alb.ingress.kubernetes.io/target-group-attributes: 'stickiness.enabled=true,stickiness.lb_cookie.duration_seconds=86400,stickiness.type=lb_cookie,deregistration_delay.timeout_seconds=30,slow_start.duration_seconds=0'"
        ```

    ALB is used for all HTTP endpoints. In addition to this a ranger-plugin service endpoint
    is created that requires a NLB. Run the following commands - 

    ??? note "vars.ranger-plugin.yml"
        ```bash
        cd ~/privacera/privacera-manager/config/custom-vars
        
        # create a new file 
        vi vars.ranger-plugin.yml
        
        RANGER_PLUGIN_SERVICE_ANNOTATIONS:
        - 'service.beta.kubernetes.io/aws-load-balancer-type: nlb'
        - 'service.beta.kubernetes.io/aws-load-balancer-backend-protocol: tcp'
        - 'service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled: "true"'
        - 'service.beta.kubernetes.io/aws-load-balancer-subnets: <subnet-xxxx>, <subnet-yyyy>'
        - 'service.beta.kubernetes.io/aws-load-balancer-security-groups: <sg-1234>'
        
        # for internal
        - 'service.beta.kubernetes.io/aws-load-balancer-internal: "true"'
        
        # For internetfacing
        - 'service.beta.kubernetes.io/aws-load-balancer-scheme: "internet-facing"'
        ```

    After you have run Privacera Manager setup and helm install steps, and the ingress objects have been created, this will create
    an AWS ALB with the specified annotations. You will then have to copy the DNS name of the ALB and
    update the following properties in the same file. You will need the AWS Route 53 Hosted Zone ID and
    the domain name that you have configured in Route 53.

    ```bash
    AWS_ALB_EXTERNAL_URL: "<PLEASE_CHANGE>"
    PRIVACERA_AWS_ZONE_ID: “<HOSTED_ZONE_ID>”
    AWS_ROUTE_53_DOMAIN_NAME: “<DOMAIN_NAME>”    
    ```

    Service end-point host names are generated by Privacera Manager using the deployment name as 
    the namespace. You will then run Privacera Manager post-install step which will create Route 53 
    entries for your service end-points.

    Privacera Manager setup, helm-install and post-install steps are explained in 
    [Using Privacera Manager](using-privacera-manager.md) section.

### Configure Load Balancer (optional)
??? note "Configure Load Balancer (optional)"
    If you are not using AWS ALB Controller then the kubernetes services will be created of type LoadBalancer.
    This will create Load Balancers in your cloud provider. 

    TBD: How do we assign TLS certificates to these Load Balancers? 
    You need to copy the cert and key into the config/ssl/custom_certificates folder and
    the load-balancers are of type classic loadbalancers or NLB with port level pass through
    and certificates are part of the individual services. To be confirmed

## Next steps

Depending upon your deployment type and choice of Privacera modules , you can proceed to the next steps -

| #   | Deployment type           | Module       | Next step                                                                                |
|-----|---------------------------|--------------|------------------------------------------------------------------------------------------|
| 1.  | Self-Managed              | Access       | [Self Managed Access](../self-managed-access.md)                                         |
| 2.  | Self-Managed              | Discovery    | [Self Managed Discovery](../self-managed-discovery/index.md)                             |
| 3.  | Self-Managed              | Encryption   | [Self Managed Encryption](../self-managed-encryption/index.md)                           |
| 4.  | Self-Managed              | Dataserver   | [Self Managed Dataserver](../self-managed-dataserver/index.md)                           |
| 5.  | Self-Managed              | Usersync     | [Self Managed Usersync](../self-managed-usersync/index.md)                               |
| 6.  | PrivaceraCloud Data-plane | Access       | [PrivaceraCloud Data-plane Access](../privaceracloud-data-plane-access.md)               |
| 7.  | PrivaceraCloud Data-plane | Discovery    | [PrivaceraCloud Data-plane Discovery](../privaceracloud-data-plane-discovery/index.md)   |
| 8.  | PrivaceraCloud Data-plane | Encryption   | [PrivaceraCloud Data-plane Encryption](../privaceracloud-data-plane-encryption/index.md) |
| 9.  | PrivaceraCloud Data-plane | Dataserver   | [PrivaceraCloud Data-plane Dataserver](../privaceracloud-data-plane-dataserver/index.md) |
| 10. | PrivaceraCloud Data-plane | Usersync     | [PrivaceraCloud Data-plane Usersync](../privaceracloud-data-plane-usersync/index.md)     |



<div class="grid cards" markdown>
-  :material-page-previous: Prev [Setup](setup.md)
</div>
