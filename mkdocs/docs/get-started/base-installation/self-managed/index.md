# Self-managed

In self-managed deployment, you install the Privacera software in your cloud provider VPC. Privacera
has a microservices architecture and is deployed as docker containers running
in a Kubernetes cluster. The docker containers are hosted in Privacera docker registry.

Privacera provides a command-line utility called Privacera Manager which generates various
installation artifacts such as helm charts, terraform and cloud formation templates
to install the Privacera components. Privacera Manager consists of a tar ball of various
template files and a docker image. Privacera Manager is common across all the cloud providers.

If you are running in an air-gap environment, you will download the tar ball of docker images
and host them in your docker registry.

The installation process is divided into the following steps:

1. Prerequisites which includes creating and configuring cloud resources
2. Installing Privacera Manager software
3. Doing the basic configuration of vars YAML files of Privacera Manager
4. Using Privacera Manager to generate helm charts, apply the helm charts and post-installation steps
5. Verify the installation

The above steps gives you a basic installation of Privacera software. After this, you will do the 
following,

1. Install Connectors for your data-sources
2. Do Advanced configuration as required
3. Using Privacera Manager to generate helm charts, apply the helm charts and post-installation steps
4. Verify the installation

<div class="grid cards" markdown>
-   :material-page-previous: Prev [Base Installation](../index.md)
-   :material-page-next: Next [Prerequisites](prerequisites/index.md)
</div>
