# Self-managed

In self-managed deployment, you install the Privacera software in your cloud provider VPC. Privacera
has a microservices architecture and is deployed as docker containers running
in a Kubernetes cluster. The docker containers are hosted in Privacera docker registry.

Privacera provides a command-line utility called Privacera Manager which generates various
installation artifacts such as helm charts, terraform and cloud formation templates
to install the Privacera components. Privacera Manager consists of a tar ball of various
template files and a docker image. Privacera Manager is common across all the cloud providers.

If you are running in an air-gapped environment, you will download the tar ball of docker images
and host them in your docker registry.

<div class="grid cards" markdown>
-   :material-page-previous: Prev [Base Installation](../index.md)
-   :material-page-next: Next [Prerequisites](prerequisites/index.md)
</div>
