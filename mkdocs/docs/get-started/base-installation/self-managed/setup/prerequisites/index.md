# Prerequisites
The following prerequisites are required for a Self-managed deployment or a PrivaceraCloud
Data-plane deployment:

1. **Cloud Provider** - Privacera supports the following cloud providers: AWS, Azure and Google Cloud
1. **Kubernetes Cluster** - Privacera supports the following managed Kubernetes distributions: AWS EKS, Azure AKS, 
  Google Cloud GKE. The versions for the supported Kubernetes distributions are provided TBD-versions-link.
1. **Cloud resources** - Various cloud resources are required for Privacera deployment. These include:
    - Managed RDBMS - to store policies and metadata
    - Managed NoSQL - to store Privacera Discovery metadata (only if you are using Privacera Discovery module
    - Object store bucket - to store configuration and audit logs
    - Kubernetes cluster 
    - Cloud compute to run Privacera Manager software
    - IAM policies and roles 
    - Network Setup - VPC, subnets, security groups, VPC peering or transit gateways. As Privacera will be 
      connecting to your data-sources you will need to think about the network connectivity.
    - Load balancer, DNS entries, TLS certificates - for securing the service endpoints
1. **Privacera Manager** - This is the installation software used to configure and install Privacera software. Your Privacera Sales representative will give you the following, 
       - Credentials for Privacera docker registry
       - Download URL of Privacera Manager software
1. **Air gap network (optional)** - If you are in an air gap (no Internet access) network, you will need to host the docker
   images in your own docker registry. Refer to [Air-gap Installation](../air-gap-installation.md)

For the installation, there are two parallel tracks - Creating Cloud Resources and Installing Privacera using 
Privacera Manager. In most organizations, these two are done by different teams or same person with
different privileges. Most cloud resources need to be created before Privacera installation ca   

<div class="grid cards" markdown>
-  :material-page-previous: Prev [Self Managed](../index.md)
-  :material-page-next: Next
    -   [AWS Cloud Resources](aws-cloud-resources.md)
    -   [Azure Cloud Resources](azure-cloud-resources.md)
    -   [Google Cloud Resources](google-cloud-resources.md)
    -   [Air gap network](../../advanced-configuration/air-gap-installation.md)
    -   [Privacera Manager Setup](../privacera-manager-setup.md)
</div>
