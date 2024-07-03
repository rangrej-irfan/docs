# Overview 

!!! note
    You should follow the instructions on this page if you are installing PrivaceraCloud Data-plane.
    You should have successfully done the [Basic Configuration](../basic-configuration/index.md) before proceeding with 
    the instructions on this page.

As part of setting up PrivaceraCloud Data-plane, after you have done the 
[Basic Configuration](../basic-configuration/index.md), continue with the instructions on this page.
At a high level this involves configuring the PrivaceraCloud Portal and the Privacera Manager as follows,

1. Configuration on PrivaceraCloud Portal and download an artifact.
2. Configuration in Privacera Manager using the artifact downloaded from the PrivaceraCloud Portal.
3. Run Privacera Manager to generate an artifact and upload it to the PrivaceraCloud Portal.

## Prerequisites

You need the following information to configure PrivaceraCloud Data-plane:

1. Administration access to the PrivaceraCloud Portal.
2. Access to the Privacera Manager installation host.
3. Ensure that you have worked with your Privacera sales representative to enable the data-plane feature on your PrivaceraCloud account.

## Configuration on PrivaceraCloud Portal

| # | Required for      | Configuration Step                                                                                                           | Description                                                                                                                                                                                                                                                                                                                              | 
|---|-------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Access, Discovery | [Create Access service user, Ranger Admin URL and API key](#create-ranger-service-user-admin-url-and-api-key)                | Create a an Access service user in your PrivaceraCloud account which will be used by the Privacera Access connectors in the Data-plane to connect to your PrivaceraCloud account.<br>Note these as RANGER_ADMIN_URL, RANGER_SERVICE_USERNAME, RANGER_SERVICE_PASSWORD and API_KEY which will be used in Privacera Manager configuration. |
| 2 | Access            | [Enable the Ranger Service Definitions for Access Connectors](#enable-the-ranger-service-definitions-for-access-connectors)  | If you know which Privacera Access connectors you are going to use, then do this step or wait till Connector on-boarding.                                                                                                                                                                                                                |
| 3 | Encryption        | [Enable Privacera Encryption module](#enable-privacera-encryption-module)           | Required for Privacera Encryption else skip.<br>Download the `vars.data-plane.config.yml` from PrivaceraCloud portal which is used in Privacera Manager configuration.                                                                                                                                                                   |
| 4 | Discovery         | [Create Ranger Service user for Discovery Compliance policies](#create-ranger-service-user-for-discovery-compliance-policies) | Required for Privacera Discovery Compliance policies, else skip. Also, requires Privacera Encryption to be enabled.<br>Note the credentials which will be used in Privacera Manager configuration.                                                                                                                                       |

## Configuration in Privacera Manager

Make sure you have done the configuration on the PrivaceraCloud Portal as given above, 
and have these handy,

- RANGER_ADMIN_URL
- RANGER_SERVICE_USERNAME
- RANGER_SERVICE_PASSWORD
- API_KEY
- `vars.data-plane.config.yml`

Run the following commands,
```bash
# Download the vars.data-plane.config.yml from PrivaceraCloud Portal 
# in 'Configuration on PrivaceraCloud Portal - step 3' above

# Upload the vars.data-plane.config.yml to Privacera Manager host and copy 
# to `~/privacera-manager/config/custom-vars/vars.data-plane.config.yml`
```
```bash
# Confirm it's presence by running `
ls -l ~/privacera-manager/config/custom-vars/vars.data-plane.config.yml
```
```bash
# Copy the sample vars.privacera-cloud.yml file from sample-vars folder
cd ~/privacera/privacera-manager
cp config/sample-vars/vars.privacera-cloud.yml config/custom-vars/
```

```bash
# Edit the file
cd ~/privacera/privacera-manager
vi config/custom-vars/vars.privacera-cloud.yml
```
```bash
# Edit the file as follows,

# Obtain the Ranger Admin URL, API Key, Ranger service 
# username, password from 
# 'Configuration on PrivaceraCloud Portal -step #1' above. 
# Set the base URL, that is the host name, to this variable as follows

# Example - if the Ranger Admin URL is of this format - 
# https://api.privaceracloud.com/api/XYZ then 
# set the variable to https://api.privaceracloud.com
PRIVACERA_CLOUD_BASE_URL: "<BASE_URL of RANGER_ADMIN_URL>"
PRIVACERA_CLOUD_API_KEY: "<API_KEY>"

CONNECTOR_RANGER_USER_NAME: "<RANGER_SERVICE_USERNAME>"
CONNECTOR_RANGER_USER_PASSWORD: "<RANGER_SERVICE_PASSWORD>"

PRIVACERA_USERSYNC_RANGER_USERNAME: "<RANGER_SERVICE_USERNAME>"
PRIVACERA_USERSYNC_RANGER_PASSWORD: "<RANGER_SERVICE_PASSWORD>"

# Set these variables, if not using Privacera Discovery on data-plane
RANGER_ENABLE: "false"
PORTAL_ENABLE: "false"
PORTAL_INSTALL: "false"
SOLR_ENABLE: "false"
ZOOKEEPER_ENABLE: "false"
AUDITSERVER_ENABLE: "false"
MARIADB_ENABLE: "false"
DB_INSTALL_MARIADB: "false"

# Set these variables, if you plan to use Privacera Discovery on data-plane
RANGER_ENABLE: "false"
PORTAL_ENABLE: "true"    # Enable for Privacera Discovery on data-plane
PORTAL_INSTALL: "true"   # Enable for Privacera Discovery on data-plane
SOLR_ENABLE: "true"      # Enable for Privacera Discovery on data-plane
ZOOKEEPER_ENABLE: "true" # Enable for Privacera Discovery on data-plane
AUDITSERVER_ENABLE: "false"
MARIADB_ENABLE: "false"
DB_INSTALL_MARIADB: "false"
```

```bash
# Edit the vars.ssl.yml file
vi config/custom-vars/vars.ssl.yml
``` 
```bash
# Add or edit the following variable
RANGER_SSL_ENABLE: "false"
```


## Appendix
### Create Ranger service user, Admin URL and API key
??? note "Create Ranger service user, Admin URL and API key"
    Perform following steps in the PrivaceraCloud control plane portal:
    
    1. Log in to PrivaceraCloud Portal. 

    2. Perform following steps to create Ranger Admin Username and Password:

        1. Go to **Access Management** > **Users/Groups/Roles**.

        2. Click **ADD** to create a new user.
        
        3. Under **Add User** , provide values in the following fields:
    
            * **User Name** : Provide value for the user name. Privacera suggests to use `ranger_dataplane_user` as a user name value.
            
            * **First Name** : Provide value for the first name. Privacera suggests to use `ranger_dataplane_user` as a first name value.
            
            * **Role** : Select `Admin` from the drop-down list.
            
            * **New Password** : Provide a strong password
            
            * **Confirm Password** : Provide the same value as provided in the preceding step.
            
            !!! note
                Make a note of values provided in the **User Name** and **New Password**
                fields. These values are needed as a `RANGER_SERVICE_USERNAME` and 
                `RANGER_SERVICE_PASSWORD` in the Privacera Manager configuration.
        
        4. Click **SAVE**.

    3. Generate and copy the Ranger Admin URL and API key for use by data plane, see [Generate Ranger Admin URL and API Key](apache-ranger-api-on-privaceracloud.html#generate-a-ranger-admin-api-url-and-api-key "Generate a Ranger Admin API URL and API Key") for more instructions.

    !!! note
        Make a note of the `RANGER_ADMIN_URL` and `API_KEY` values. These values are needed in the Privacera Manager configuration.


### Enable the Ranger Service Definitions for Access Connectors
??? note "Enable the Ranger Service Definitions for Access Connectors"
    Activate the Access data-source applications by enabling and disabling them for the first time as follows:

    This step is needed to activate the third-party application such as, Vertica,
    Databricks in PrivaceraCloud portal.

    You can skip this step if the third-party application is already activated in
    the PrivaceraCloud portal. Go to **Settings** > **Application**. If the third-
    party application is visible in the **Connected Applications** list that means
    the application is already activated.

    1. Go to **Settings** > **Applications**.

        1. In the Applications section, select the application you wish to connect. If you don’t see the application you wish to connect, contact [Privacera Support](../../../../resources/support/support_how_to.md). For example, If you are planning to use Vertica application, then select Vertica.

        2. Enter the application name and description in the **Name** and **Description** fields respectively.

        3. Click the toggle button to enable **Access Management** for the application.

        4. Since the application will be disabled in the subsequent steps, therefore temporarily input dummy placeholder values into the mandatory fields and then click **SAVE** to activate the application.
        
        5. Select the same application that you enabled in the preceding step. Click the edit icon.
        
        6. Click the toggle button to disable **Access Management** for the application.

        !!! note
            Do not disable application if it is one of the following applications for
            which access is managed by DataServer: Databricks (OLAC), EMR (OLAC), S3, Athena, DynamoDB, Glue, Kinesis, Lambda or Textract

        7. Click **SAVE** to disable the application.

    2. Click **Access Management** > **Resource Policies**.
    
        3. Click the edit icon of newly added Application.
    
        4. Click the Active Status to enable **Access Management** for the application.
    
        5. Click **SAVE**.


### Enable Privacera Encryption module
??? note "Enable Privacera Encryption module"
    1. Go to **Settings** > **Account** > **Encryption Settings**. Click **ENABLE**.

    2. Under **BASIC** tab, enter the value for the **Secret** field. Click **SAVE**.

        !!! note
            Make a note of the `Secret` value, as it will be necessary to use the same
            value when enabling PEG in the data plane for the
            `SCHEME_SERVER_SHARED_SECRET` property.

    3. Download Distributed Data Plane configuration from PrivaceraCloud:

        1. Go to **Settings** > **Account**.

        2. Under **Distributed Data Plane** , click **DOWNLOAD**.

            !!! note
    
                If you do not see the **Distributed Data Plane** option under **Account** ,
                contact [Privacera Support]((../../../../resources/support/support_how_to.md) to
                enable **Distributed Data Plane**.
    
        3. Download the `vars.data-plane.config.yml` from PrivaceraCloud portal which is used in Privacera Manager configuration.

    4. Create System Generated Schemes:

        !!! note
            This step is optional and required only if the user wants to configure
            Encryption on Discovery Compliance policies.

        1. Go to **Encryption & Masking** > **ENCRYPTION**.
    
        2. Click **GENERATE SYSTEM SCHEME**.
    
        3. Confirm generation by clicking **Yes** in the **Confirm Create** pop up.

        You can see the System schemes generated on the user interface.

### Create Ranger Service user for Discovery Compliance policies

??? note "Create Ranger Service user for Discovery Compliance policies"

    !!! note
        This step is optional and required only if the user wants to configure
        Encryption on Discovery Compliance policies.

    1. Go to **Access Management** > **User/Groups/Roles**.

    2. Click **Add**.

    3. Under **Add User** , provide values in the following fields:
        
        1. **User Name** : Provide value for the user name. Privacera suggests to use `privacera_service_discovery` as a user name value.
        
        2. **First Name** : Provide value for the first name. Privacera suggests to use `privacera_service_discovery` as a first name value.
        
        3. **Role** : Select `USER` from the drop-down list.
        
        4. **New Password** : Provide value for the password.

            !!! note
                Remember the password value provided, as it will be used in the Discovery configuration later.

        5. **Confirm Password** : Provide the same value as provided in the preceding step.

    4. Click **SAVE**. A new user has been created.

    5. Go to **Access Management** > **Scheme Policies**.

    6. Click on the **privacera_peg** service.

    7. Locate the **all - encryption-scheme, presentation-scheme** policy and Click the edit icon to edit it.

    8. Under **Allow Conditions** , add **privacera_service_discovery** user in the **Select User** field which has user permissions: _Protect, Unprotect, Get Scheme, Impersonate_

    9. Click **Save**.


## Next steps

Depending upon your deployment type and choice of Privacera modules , you can proceed to the next steps -

| #  | Deployment type           | Module     | Next step                                                                                |
|----|---------------------------|------------|------------------------------------------------------------------------------------------|
| 1. | PrivaceraCloud Data-plane | Access     | [Connectors](../../../../connectors/index.md)                                            |
| 2. | PrivaceraCloud Data-plane | Discovery  | [PrivaceraCloud Data-plane Discovery](../privaceracloud-data-plane-discovery/index.md)   |
| 3. | PrivaceraCloud Data-plane | Encryption | [PrivaceraCloud Data-plane Encryption](../privaceracloud-data-plane-encryption/index.md) |
