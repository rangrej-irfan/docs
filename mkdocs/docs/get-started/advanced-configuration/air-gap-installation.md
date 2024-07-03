# Air-gap installation

!!! note
    This section is applicable only if you are installing Privacera Manager in an air gap (no Internet access) network.
    This is not a typical setup.
    You also need to do the Self Managed Prerequisites before you can proceed with this section. Refer to the [Prerequisites](../base-installation/self-managed/setup/prerequisites/index.md) section.

## Overview

An air gap network is a secure network environment that is isolated from the Internet. If you plan 
to install Privacera software in an air gap (no Internet access) network, then you have to download the Privacera docker 
images and host them in your docker registry. You also have to host the Privacera Manager tarball in an object store 
accessible to the compute host in air gap network. A script, `pm-airgap-installation.sh`, is provided to facilitate 
this process.


### Prerequisites

1. You need a Linux host that has access to the Internet where you will run the pm-air-gap-installation.sh script.
2. Your local docker registry where you will host the Privacera docker images. We need the URL of the registry 
   and the credentials to push the images to the registry.
3. Access to the compute host in air gap (no Internet access) network from where you plan to run Privacera Manager. This host should have 
   access to the local docker registry where the Privacera docker images are hosted.

## Installation Information
You will need the following information to install Privacera Manager, obtain these from Privacera Sales Representative:

--8<-- "docs/get-started/base-installation/self-managed/snippets/installation-information.ext"

### Download script

Run the following wget command 
```bash 
wget <PRIV_MGR_BASE_URL>/pm-airgap-installation.sh
chmod +x pm-airgap-installation.sh
```

### Download packages and images of Privacera Manager

Run the following comands - 
```bash
./pm-airgap-installation.sh

Enter Privacera Base Download URL:
<PRIV_MGR_BASE_URL>

Download Privacera Core Components ? Y/N

Download Internal Mariadb Database Image  ? Y/N

Download Privacera Access Manager Component Images  ? Y/N

Download Privacera Discovery Component Images  ? Y/N

Download Encryption & Masking Component Images  ? Y/N

Download Statistics & Monitoring Component Images  ? Y/N

Download Privacera Diagnostics Component Images  ? Y/N
 
```
The scripts lists the packages and images downloaded and saved in
`${PWD}/privacera/downloads` and `${PWD}/privacera/downloads/images` locations
respectively.

### Push images to internal repository

Run the script again with push action to upload the images to your private
Repository and copy (.tar) packages to your Privacera Manager host.

```bash
./pm-airgap-installation.sh push

Enter Privacera Docker Hub URL:
Enter Privacera Image Tag:
Enter Docker login URL:
Enter Docker user:
Enter Docker password:
```
Once the images are pushed to the internal repository, it will clean up images in the 
`${PWD}/privacera/downloads/images` directory and prompts to copy packages to Privacera Manager host.
At this point, you can exit from the script by typing Ctrl-C.

Copy the `${PWD}/privacera/downloads/packages/privacera-manager.tar.gz` to an object store from where
it can be accessed by the Privacera Manager host.

## Air-gap Installation Information

Now you should be ready with this set of properties. Here AIRGAP refers to your object store location
for the privacera-manager tar ball and your docker registry location for the Privacera docker images.

--8<-- "docs/get-started/base-installation/self-managed/snippets/air-gap-installation-information.ext"

<div class="grid cards" markdown>
-  :material-page-next: Next [Privacera Manager Setup](../base-installation/self-managed/setup/privacera-manager-setup.md)
</div>