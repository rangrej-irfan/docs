# Using Privacera Manager

!!! note "Prerequisites"
    You will be using Privacera Manager after you have met the prerequisites and done the basic
    configuration of vars YAML files. If you have not done so,
    please refer to the [Prerequisites](../base-installation/self-managed/prerequisites/index.md) section and carry out the steps for your
    cloud provider. Also do the [Basic Configuration](../base-installation/self-managed/configuration.md) of vars YAML files. 

## QuickStart
You will be using the following three commands after you have done the 
basic configuration. Every time, you modify the vars YAML files, you will need to run these 3 commands.

```bash
cd ~/privacera/privacera-manager

# step 1 - setup which generates the helm charts. 
# This step usually takes few minutes.
./privacera-manager.sh setup

# step 2 - install or upgrade the Privacera Manager helm charts
./pm_with_helm.sh [install|upgrade]

# step 3 - post-installation steps which generates Plugin tar ball, 
#   updates Route 53 DNS, etc.
./privacera-manager.sh post-install
```

