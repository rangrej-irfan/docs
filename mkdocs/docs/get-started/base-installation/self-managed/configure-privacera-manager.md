# Configure Privacera Manager

!!! note "Prerequisites"
    Before you begin, ensure that you have the installed Privacera Manager by following the steps in 
    the [Installing Privacera Manager](installing-privacera-manager.md) section.

## Overview

Privacera Manager provides several sample variable YAML files that are in the `config/sample-vars` folder.
The process of configuring Privacera Manager involves copying these sample variable YAML files to the 
`config/custom-vars` folder and modify them to suit your environment. The files under `config/custom-vars`
are not overwritten during upgrades.

??? note "Enable Vault"
??? note "Configure Cloud Provider"
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


??? note "Configure Kubernetes"
??? note "Configure EFS"
??? note "Configure External RDBMS"
??? note "Configure TLS"
??? note "Configure Ingress Controller (optional)"
??? note "Configure Load Balancer (optional)"

<div class="grid cards" markdown>
-  :material-page-previous: Prev [Installing Privacera Manager](installing-privacera-manager.md)
-  :material-page-next: Next [Using Privacera Manager](using-privacera-manager.md)
</div>
