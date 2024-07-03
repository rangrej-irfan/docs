# Self-managed

## Overview
In self-managed deployment, you install the Privacera software in your cloud provider VPC. Privacera
has a microservices architecture and is deployed in a Kubernetes cluster. The docker images are 
hosted in Privacera docker registry.

## Installation tracks

The steps are common for Self Managed installation and PrivaceraCloud Data-plane installation. 
Refer to [Deployment Options](../../deployment-options/index.md) for more details.

### Basic Configuration

The Basic Configuration is same for both Self Managed and PrivaceraCloud Data-plane.

| Track                                                               | Description                   | Mandatory |
|---------------------------------------------------------------------|-------------------------------|-----------|
| - Self-Managed Deployment<br>- PrivaceraCloud Data-plane Deployment | Setup and Basic Configuration | Yes       |


### Self-Managed Installation Track

If you are installing Self Managed, after doing the Basic Configuration  you will move on to these items.

| Track | Description                                    | Mandatory |
| --- |------------------------------------------------|-----------|
| Self-Managed Deployment  | Self-Managed Privacera Access configuration    | No *      |
| Self-Managed Deployment  | Self-Managed Privacera Discovery configuration | No *      |
| Self-Managed Deployment  | Self-Managed Privacera Encryption configuration | No        |
| Self-Managed Deployment  | Self-Managed Dataserver configuration          | No        |
| Self-Managed Deployment  | Self-Managed Usersync configuration            | Yes       |

* You need to install either Privacera Access and/or Privacera Discovery.

### PrivaceraCloud Data-plane Installation Track

If you are installing PrivaceraCloud Data-plane, after doing the Basic Configuration  you will move on to these items.

| Track | Description | Mandatory |
| --- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| PrivaceraCloud Data-plane Deployment  | PrivaceraCloud Data-plane Privacera Discovery configuration | No        |
| PrivaceraCloud Data-plane Deployment  | PrivaceraCloud Data-plane Privacera Encryption configuration | No        |
| PrivaceraCloud Data-plane Deployment  | PrivaceraCloud Data-plane Dataserver configuration | No        |
| PrivaceraCloud Data-plane Deployment  | PrivaceraCloud Data-plane Usersync configuration | Yes       |

## Base Installation Process 

The installation process is divided into the following steps:

1. Prerequisites which includes creating and configuring cloud resources.
2. Setup - Installing Privacera Manager software which is used to install the Privacera software.
3. Doing the basic configuration for Privacera Manager. This is done by editing YAML files in Privacera Manager.
4. Using Privacera Manager to generate helm charts, apply the helm charts and do post-installation steps.
5. Verify the installation.

## Connector Installation Process 

After the basic installation of Privacera software has been done, you can do the following,

1. Install Connectors for your data-sources
2. Do Advanced configuration as required
3. Using Privacera Manager to generate helm charts, apply the helm charts and post-installation steps
4. Verify the installation

If you are running in an air gap (no Internet access) network, you will download the docker images
and host them in your docker registry.

<div class="grid cards" markdown>
-   :material-page-previous: Prev [Base Installation](../index.md)
-   :material-page-next: Next [Setup](setup/index.md)
</div>
