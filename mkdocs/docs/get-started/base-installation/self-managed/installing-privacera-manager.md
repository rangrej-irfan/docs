# Installing Privacera Manager

!!! note "Prerequisites"
    You will be installing Privacera Manager after you have met the prerequisites. If you have not done so, 
    please refer to the [Prerequisites](prerequisites/index.md) section and follow the steps for your 
    cloud provider.

!!! note "Air-gap Installation"
    If you are installing in an air-gap environment, you will need to download the docker images and host them in your 
    docker registry, and host the Privacera Manager tar ball. 
    Please refer to the [Air-gap Installation](air-gap-installation.md) section for more details.

## Overview 
You will be installing Privacera Manager on the compute instance that you have created as part of the 
Prerequisites and it is associated with your Kubernetes cluster. These steps are common for all cloud providers.

## Installation Information
=== "Normal"
    You will need the following information to install Privacera Manager, obtain these from Privacera Sales Representative:
    
    --8<-- "docs/get-started/base-installation/self-managed/snippets/installation-information.ext"

=== "Air-gap"

    You will need the following information to install Privacera Manager in an air-gap environment.
    Obtain these from [Air-gap Installation](air-gap-installation.md#air-gap-installation-information):
    
    --8<-- "docs/get-started/base-installation/self-managed/snippets/air-gap-installation-information.ext"

## Air-gap Installation
An air-gap installation is done in an environment where the compute instances do not have access to the internet.
If you are installing in an air-gap environment, [follow these steps](./air-gap-installation.md) first and then continue with 
the installation.

## Download and Extract
On the compute instance where you want to install Privacera Manager, perform the following steps:

=== "Normal"
    ```bash
    # log into Privacera docker hub and enter the Privacera hub password
    docker login <PRIVACERA_HUB_HOSTNAME> -u <PRIVACERA_HUB_USER> # (1)
    # Enter your PRIVACERA_HUB_PASSWORD when prompted
    
    # pull the Privacera Manager docker image, this also verifies the credentials
    docker pull <PRIV_MGR_IMAGE> # (2)
    
    # Create folders for downloading tarball and download the tarball
    mkdir -p ~/privacera/downloads # (3)
    wget <PRIV_MGR_PACKAGE> -O privacera-manager.tar.gz # (4)
    
    # extract the tarball
    cd ~/privacera
    tar -zxf ~/privacera/downloads/privacera-manager.tar.gz # (5)
    
    # create a shell script that is used internally
    cd ~/privacera/privacera-manager/config 
    echo '#!/bin/bash' > pm-env.sh # (6)
    echo "export PRIV_MGR_PACKAGE=<PRIV_MGR_PACKAGE>" >> pm-env.sh 
    echo "export PRIV_MGR_IMAGE=<PRIV_MGR_IMAGE>" >> pm-env.sh
    ```

    1. Login into Privacera docker hub using the credentials provided to you
    2. Pull the Privacera Manager docker image from Privacera docker hub
    3. Create a folder for Privacera. Preferably keep the folder name as given above so that it is easy to follow the 
       guide. Under this folder we have the download folder where the tar ball is downloaded
    4. Download the privacera-manager tar ball and save it in the downloads folder
    5. Extract the tarball in the Privacera folder. From now on you will run all command from 
       `~/privacera/privacera-manager` folder
    6. Create a script called pm-env.sh that has the download URL and Privacera Manager docker image name in it.

=== "Air-gap"
    ```bash
    # log into your docker hub and enter the hub password
    docker login <AIRGAP_HUB_HOSTNAME> -u <AIRGAP_HUB_USER> # (1)
    # Enter your AIRGAP_HUB_PASSWORD when prompted
    
    # pull the Privacera Manager docker image, this also verifies the credentials
    docker pull <AIRGAP_PRIV_MGR_IMAGE> # (2)
    
    # Create folders for downloading tarball and download the tarball
    mkdir -p ~/privacera/downloads # (3)
    wget <AIRGAP_PRIV_MGR_PACKAGE> -O privacera-manager.tar.gz # (4)
    
    # extract the tarball
    cd ~/privacera
    tar -zxf ~/privacera/downloads/privacera-manager.tar.gz # (5)
    
    # create a shell script that is used internally
    cd ~/privacera/privacera-manager/config 
    echo '#!/bin/bash' > pm-env.sh # (6)
    echo "export PRIV_MGR_PACKAGE=<AIRGAP_PRIV_MGR_PACKAGE>" >> pm-env.sh 
    echo "export PRIV_MGR_IMAGE=<AIRGAP_PRIV_MGR_IMAGE>" >> pm-env.sh
    ```

    1.  Login into your docker hub using the credentials provided to you
    2.  Pull the Privacera Manager docker image from your docker hub
    3.  Create a folder for Privacera. Preferably keep the folder name as given above so that it is easy to follow the 
        guide. Under this folder we have the download folder where the tar ball is downloaded.
    4.  Download the privacera-manager tar ball from your object store and save it in the downloads folder
    5.  Extract the tarball in the Privacera folder. From now on you will run all command from 
        `~/privacera/privacera-manager` folder
    6.  Create a script called pm-env.sh that has the download URL and Privacera Manager docker image name in it.
 

## Name your deployment

Come up with a name for your deployment. This name will be used as a namespace in Kubernetes and 
will be visible in the Privacera Portal. As such, this name will become part of the service endpoint
host names generated by Privacera Manager. 

It should be a short user-friendly name that follows these rules:

- contain at most 63 characters
- contain only lowercase alphanumeric characters or '-'
- start with an alphanumeric character
- end with an alphanumeric character

Run the following commands, where you can name your deployment environment as you like along with 
the Privacera Manager image tag and download URL base-path.

=== "Normal"
    ```bash
    cd ~/privacera/privacera-manager
    cp config/sample.vars.privacera.yml config/vars.privacera.yml 
    
    vi config/vars.privacera.yml
    
    # Give a short user-friendly name for your installation that follows these rules, 
    # - contain at most 63 characters
    # - contain only lowercase alphanumeric characters or '-'
    # - start with an alphanumeric character
    # - end with an alphanumeric character
    # It will be visible in Privacera Portal and will be used as a namespace in Kubernetes.
    DEPLOYMENT_ENV_NAME: "privacera-dev"
    
    privacera_hub_user: "<PRIVACERA_HUB_USER>"
    privacera_hub_password: "<PRIVACERA_HUB_PASSWORD>"
    
    # this should be only the IMAGE_TAG out of HUB_HOST/IMAGE_NAME:IMAGE_TAG
    PRIVACERA_IMAGE_TAG: "<PRIV_MGR_IMAGE_TAG>"
    
    # only the download URL without the file name privacera-manager.tar.gz, example: https://<domain>/<filepath>
    PRIVACERA_BASE_DOWNLOAD_URL: "<PRIV_MGR_BASE_URL>"
    ```

=== "Air-gap"
    ```bash
    cd ~/privacera/privacera-manager
    cp config/sample.vars.privacera.yml config/vars.privacera.yml 
    
    vi config/vars.privacera.yml
    
    # Give a short user-friendly name for your installation that follows these rules, 
    # - contain at most 63 characters
    # - contain only lowercase alphanumeric characters or '-'
    # - start with an alphanumeric character
    # - end with an alphanumeric character
    # It will be visible in Privacera Portal and will be used as a namespace in Kubernetes.
    DEPLOYMENT_ENV_NAME: "privacera-dev"
    
    privacera_hub_url: "<AIRGAP_HUB_HOST>"
    privacera_hub_user: "<AIRGAP_HUB_USER>"
    privacera_hub_password: "<AIRGAP_HUB_PASSWORD>"
    
    # this should be only the IMAGE_TAG out of HUB_HOST/IMAGE_NAME:IMAGE_TAG
    PRIVACERA_IMAGE_TAG: "<PRIV_MGR_IMAGE_TAG>"
    
    # only the download URL without the file name privacera-manager.tar.gz, example: https://<domain>/<filepath>
    PRIVACERA_BASE_DOWNLOAD_URL: "<AIRGAP_PRIV_MGR_BASE_URL>"
    ```
Now you are all set to continue with configuring the Privacera Manager.

## Exploring Privacera Manager

Privacera Manager consists of two parts - the tar ball containing various template files and scripts, 
and the docker image containing the Privacera Manager templating software. The privacera-manager.sh 
script is the driver script and provides the command line interface.

Under ~/privacera/privacera-manager, you will find the following folders of interest
```bash
# installation folder of Privacera Manager
ls -l ~/privacera/privacera-manager

# Custom config vars folder of Privacera Manager
ls -l ~/privacera/privacera-manager/config/custom-vars

# Sample config vars folder of Privacera Manager
ls -l ~/privacera/privacera-manager/config/sample-vars

# Config SSL folder of Privacera Manager
ls -l ~/privacera/privacera-manager/config/ssl

# Output folder of Privacera Manager. This is created after your first run.
ls -l ~/privacera/privacera-manager/output

# Log folder of Privacera Manager. This is created after your first run.
ls -l ~/privacera/privacera-manager/logs
```

<div class="grid cards" markdown>
-  :material-page-previous: Prev [Prerequisites](index.md)
-  :material-page-next: Next [Basic Configuration](basic-configuration.md)
</div>