# Configure Privacera Manager

!!! note "Prerequisites"
    Before you begin, ensure that you have the installed Privacera Manager by following the steps in 
    the [Installing Privacera Manager](installing-privacera-manager.md) section.

## Overview

Privacera Manager takes a set of configuration variables that are defined in YAML files. Out of 
the box, several sample variable YAML files are provided that you can use to configure Privacera Manager.
These are in the `config/sample-vars` folder. The process of configuring Privacera Manager involves
copying these sample variable YAML files to the `config/custom-vars` folder and modifying them to suit your 
environment. In some cases, you will create new configuration YAML files and add properties as given in the
documentation. The files under `config/custom-vars` are not overwritten during upgrades.

After you have configured Privacera Manager, you can run the `privacera-manager.sh` script as 
given in the [Using Privacera Manager](using-privacera-manager.md) section.

## Configuration Steps

The following are the mandatory configuration steps that you need to perform before you can start using 
Privacera Manager.

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

### Configure Load Balancer (optional)
??? note "Configure Load Balancer (optional)"


<div class="grid cards" markdown>
-  :material-page-previous: Prev [Installing Privacera Manager](installing-privacera-manager.md)
-  :material-page-next: Next [Using Privacera Manager](using-privacera-manager.md)
</div>
