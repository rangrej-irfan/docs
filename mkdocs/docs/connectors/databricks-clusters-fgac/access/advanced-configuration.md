---
title: Advanced Configuration for Access Management for Databricks all-purpose compute clusters with Fine-Grained Access Control (FGAC)
---

# Advanced Configuration for Access Management for Databricks all-purpose compute clusters with Fine-Grained Access Control (FGAC)

# JWT Auth Configuration

### Overview

  1. TODO

### Configuration

#### Prerequisite:

  - User name used in the client_id and Group names used in the scope payload of JWT token should be created in the Users/Groups/Roles section of the Privacera Access Management Portal.
  - These users or groups should be given the required permissions in the Ranger Policies for access control.


=== "Self Managed and Data Plane"

     Need to set below common properties in Spark configuration of databricks cluster:
      ```shell
      spark.hadoop.privacera.jwt.oauth.enable true
	  spark.hadoop.privacera.jwt.token /tmp/jwttoken.dat
      ```

     SSH to the instance where Privacera is installed.
    
     To enable JWT copy vars.jwt-auth.yaml from sample-vars to custom-vars
       ```shell
       cd ~/privacera/privacera-manager/config
	   cp sample-vars/vars.jwt-auth.yaml custom-vars
	   vi custom-vars/vars.jwt-auth.yaml
	   ```

    #### Static public key JWT:

    1.  Configure static public key 
        - Add below properties in vars.jwt-auth.yaml file. For a single static key, use only one entry in `JWT_CONFIGURATION_LIST`.For multiple static keys, add multiple entries:
          ```yaml
          JWT_CONFIGURATION_LIST:
		  - index: 0
		    issuer: "https://example.com/issuer"
		    # subject: "<PLEASE_CHANGE>"
		    # secret: "<PLEASE_CHANGE>"
		    userKey: "client_id"
		    groupKey: "scope"
		    parserType: "PING_IDENTITY"
		    publickey: "jwttoken1.pub"

		  - index: 1
	        issuer: "https://example.com/issuer2"
	        # subject: "<PLEASE_CHANGE>"
	        # secret: "<PLEASE_CHANGE>"
	        userKey: "client_id"
	        groupKey: "scope"
	        parserType: "PING_IDENTITY"
	        publickey: "jwttoken2.pub"
          ```
        - Add public keys in JWT token files in `config/custom-properties`:
          ```shell
	      cd ~/privacera/privacera-manager/config/custom-properties
		 
		  vi jwttoken1.pub
		  vi jwttoken2.pub
	      ```
	    - For a single static key, you only need to create one `jwttoken.pub` file.
        - Once the property is configured, run the following commands to generate and upload configuration 
	      ```shell
	      cd ~/privacera/privacera-manager

	      ./privacera-manager.sh post-install
	      ```
	    - Use the updated `ranger_enable.sh` script in Databricks cluster creation.
	    - Click on Start or, if the cluster is running, click on Confirm and Restart.

    #### Dynamic Public Key JWT:

    1.  Configure Dynamic Public Key

        - Add the following properties in the `vars.jwt-auth.yaml` file:
          ```yaml
          JWT_CONFIGURATION_LIST:
		  - index: 0
		    issuer: "https://example.com/issuer"
            # subject: "<PLEASE_CHANGE>"
            # secret: "<PLEASE_CHANGE>"
            userKey: "client_id"
            groupKey: "scope"
            parserType: "PING_IDENTITY"

            pubKeyProviderEndpoint: "https://<JWKS-provider>/get_public_key?kid="
            pubKeyProviderAuthType: "BASIC"
            pubKeyProviderAuthUserName: "<username>"
            pubKeyProviderAuthTypePassword: "<password>"
            pubKeyProviderJsonResponseKey: "x5c"
            jwtTokenProviderKeyId: "kid"
		  ```

        - Once the properties are configured, run the following commands to generate and upload the configuration:
          ```shell
          cd ~/privacera/privacera-manager

          ./privacera-manager.sh post-install
          ```

        - Use the updated `ranger_enable.sh` script in Databricks cluster creation.
        - Click on Start or, if the cluster is running, click on Confirm and Restart.

    #### Static and Dynamic public keys JWT:

	1.  Configure Static and Dynamic public keys 
        - Add below properties in vars.jwt-auth.yaml file:
          ```yaml
          JWT_CONFIGURATION_LIST:
          - index: 0
		    issuer: "https://example.com/issuer"
		    # subject: "<PLEASE_CHANGE>"
		    # secret: "<PLEASE_CHANGE>"
		    userKey: "client_id"
		    groupKey: "scope"
		    parserType: "PING_IDENTITY"
		    publickey: "jwttoken.pub"

		  - index: 1
		    issuer: "https://example.com/issuer"
		    # subject: "<PLEASE_CHANGE>"
		    # secret: "<PLEASE_CHANGE>"
		    userKey: "client_id"
		    groupKey: "scope"
		    parserType: "PING_IDENTITY"

		    pubKeyProviderEndpoint: "https://<JWKS-provider>/get_public_key?kid="
		    pubKeyProviderAuthType: "BASIC"
		    pubKeyProviderAuthUserName: "<username>"
		    pubKeyProviderAuthTypePassword: "<password>"
		    pubKeyProviderJsonResponseKey: "x5c"
		    jwtTokenProviderKeyId: "kid"
          ```
        - Add static JWT public key in jwt token file in config/custom-properties
          ```shell
	      cd ~/privacera/privacera-manager/config/custom-properties
		 
		  vi jwttoken.pub
	      ```
        - Once the property is configured, run the following commands to generate and upload configuration 
	      ```shell
	      cd ~/privacera/privacera-manager

	      ./privacera-manager.sh post-install
	      ```
	    - Use the updated `ranger_enable.sh` script in Databricks cluster creation.
	    - Click on Start or, if the cluster is running, click on Confirm and Restart.


=== "PrivaceraCloud"

    Need to set below common properties in Spark configuration of databricks cluster:
    ```shell
    spark.hadoop.privacera.jwt.oauth.enable true
    spark.hadoop.privacera.jwt.token /tmp/jwttoken.dat
    ```


    #### Static public key JWT:

    1.  Copy JWT Public Keys to Local Cluster File Path
        - Upload the JWT Public Key:
             - First, upload the `jwttoken.pub` file containing JWT public key to the DBFS or workspace location.
             - For example, upload the key to `/dbfs/user/jwt/keys`.
        - Update the Init Script:
             - To copy the public keys to the local cluster file path, update the init script with the following commands:
	           ```sh
	           export JWT_TOKEN_PUBLIC_KEY_DBFS_PATH="/dbfs/user/jwt/keys/."
	           export JWT_TOKEN_PUBLIC_KEY_LOCAL_PATH="/tmp"

	           cp -r ${JWT_TOKEN_PUBLIC_KEY_DBFS_PATH} ${JWT_TOKEN_PUBLIC_KEY_LOCAL_PATH}
	           ```
	         - This script sets the paths for the public keys in DBFS and the local cluster, then copies the keys from DBFS to the local path.


    2.  Configure single static public key 
        - Add below properties in Spark configuration of databricks cluster along with common properties:
          ```shell
          spark.hadoop.privacera.jwt.0.token.parserType PING_IDENTITY
	      spark.hadoop.privacera.jwt.0.token.userKey client_id
	      spark.hadoop.privacera.jwt.0.token.groupKey scope
		  spark.hadoop.privacera.jwt.0.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.0.token.publickey /tmp/jwttoken0.pub
          ```
        - Save the changes and click on Start or, if the cluster is running, click on Confirm and Restart.


    3.  Configure multiple static public keys 
        - Add below properties in Spark configuration of databricks cluster along with common properties:
          ```shell
          spark.hadoop.privacera.jwt.0.token.parserType PING_IDENTITY
		  spark.hadoop.privacera.jwt.0.token.userKey client_id
		  spark.hadoop.privacera.jwt.0.token.groupKey scope
		  spark.hadoop.privacera.jwt.0.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.0.token.publickey /tmp/jwttoken.pub

		  spark.hadoop.privacera.jwt.1.token.parserType PING_IDENTITY
		  spark.hadoop.privacera.jwt.1.token.userKey client_id
		  spark.hadoop.privacera.jwt.1.token.groupKey scope
		  spark.hadoop.privacera.jwt.1.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.1.token.publickey /tmp/jwttoken1.pub

		  spark.hadoop.privacera.jwt.2.token.parserType KEYCLOAK
		  spark.hadoop.privacera.jwt.2.token.userKey client_id
		  spark.hadoop.privacera.jwt.2.token.groupKey scope
		  spark.hadoop.privacera.jwt.2.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.2.token.publickey /tmp/jwttoken2.pub
          ```
        - Save the changes and click on Start or, if the cluster is running, click on Confirm and Restart.

    #### Dynamic public key JWT:

    1.  Configure single dynamic public key 
        - Add below properties in Spark configuration of databricks cluster along with common properties:
          ```shell
          spark.hadoop.privacera.jwt.0.token.parserType PING_IDENTITY
		  spark.hadoop.privacera.jwt.0.token.userKey client_id
		  spark.hadoop.privacera.jwt.0.token.groupKey scope
		  spark.hadoop.privacera.jwt.0.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.url https://<JWKS-provider>/get_public_key?kid=
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.auth.type basic
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.auth.username <username>
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.auth.password <password>
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.response.key x5c
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.key.id kid
          ```
        - Save the changes and click on Start or, if the cluster is running, click on Confirm and Restart.


    2.  Configure multiple dynamic public keys 
        - Add below properties in Spark configuration of databricks cluster along with common properties:
          ```shell
          spark.hadoop.privacera.jwt.0.token.parserType PING_IDENTITY
		  spark.hadoop.privacera.jwt.0.token.userKey client_id
		  spark.hadoop.privacera.jwt.0.token.groupKey scope
		  spark.hadoop.privacera.jwt.0.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.url https://<JWKS-provider>/get_public_key?kid=
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.auth.type basic
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.auth.username <username>
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.auth.password <password>
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.response.key x5c
		  spark.hadoop.privacera.jwt.0.token.publickey.provider.key.id kid

		  spark.hadoop.privacera.jwt.1.token.parserType PING_IDENTITY
		  spark.hadoop.privacera.jwt.1.token.userKey client_id
		  spark.hadoop.privacera.jwt.1.token.groupKey scope
		  spark.hadoop.privacera.jwt.1.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.url https://<JWKS-provider>/get_public_key?kid=
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.auth.type basic
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.auth.username <username>
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.auth.password <password>
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.response.key x5c
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.key.id kid
          ```
        - Save the changes and click on Start or, if the cluster is running, click on Confirm and Restart.

    #### Static and Dynamic public keys JWT:

    1.  Configure static and dynamic public keys
        - Add below properties in Spark configuration of databricks cluster along with common properties:
          ```shell
          spark.hadoop.privacera.jwt.0.token.parserType PING_IDENTITY
		  spark.hadoop.privacera.jwt.0.token.userKey client_id
		  spark.hadoop.privacera.jwt.0.token.groupKey scope
		  spark.hadoop.privacera.jwt.0.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.0.token.publickey /tmp/jwttoken0.pub

		  spark.hadoop.privacera.jwt.1.token.parserType PING_IDENTITY
		  spark.hadoop.privacera.jwt.1.token.userKey client_id
		  spark.hadoop.privacera.jwt.1.token.groupKey scope
		  spark.hadoop.privacera.jwt.1.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.url https://<JWKS-provider>/get_public_key?kid=
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.auth.type basic
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.auth.username <username>
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.auth.password <password>
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.response.key x5c
		  spark.hadoop.privacera.jwt.1.token.publickey.provider.key.id kid

		  spark.hadoop.privacera.jwt.2.token.parserType PING_IDENTITY
		  spark.hadoop.privacera.jwt.2.token.userKey client_id
		  spark.hadoop.privacera.jwt.2.token.groupKey scope
		  spark.hadoop.privacera.jwt.2.token.issuer https://example.com/issuer
		  spark.hadoop.privacera.jwt.2.token.publickey /tmp/jwttoken1.pub
          ```
        - Save the changes and click on Start or, if the cluster is running, click on Confirm and Restart.


### Validation

  1. Prerequisites:
    - Running Databricks cluster secured in the above steps.
  2. Steps to Validate:
    - Login to Databricks.
    - Create or open an existing notebook. Associate the Notebook with the running Databricks cluster.
    - To use JWT in Privacera Databricks integration, we need to copy the JWT token file or string to the cluster local file. To do this, use following commands and change `<jwt_token>` with your actual jwt token value.
      ```python
      jwt_file_path="/tmp/jwttoken.dat"
	  token="<jwt_token>"
	  file1 = open(jwt_file_path,"w")
	  file1.write(token)
	  file1.close()

	  # Check the file content
	  f = open(jwt_file_path,"r")
	  print(f.read())
      ```
    - Use the following PySpark commands to verify S3 CSV file read access.
      ```python
      # Define the S3 path to your file
      s3_path = "s3a://your-bucket-name/path/to/your/file"

      # Read the CSV file from the specified S3 path
      df = spark.read.format("csv").option("header", "true").load(s3_path)

      # Display the first 5 rows of the dataframe
      df.show(5)
      ```
    - On Privacera portal, go to **Access Management** -> **Audits**
    - Check for the **User** which you mentioned in **Payload** while Creating a JWT Token E.g `jwt_user`.
    - Check for the success or failure of the resource policy. A successful access is indicated as **Allowed** and failure is indicated as **Denied**.


# Use Custom Service repo

### Creating a Service repo

!!! note "We have to add these custom services outside the security zone, inside the security zone this will not work."

Let’s assume you want to create a new service repo with prefix as “dev”. Perform following steps to create custom s3 ranger policy repo. Follow the same steps to add other custom services for Hive, Files, Adls etc.

  1. Login to Privacera portal.
  2. Go to **Access Management** -> **Resource Policies**.
  3. Under s3, click more icon :material-dots-vertical:.
  4. Select **Add Service**.
  5. Under **Add Service**, provide values for the following fields:
  	- **Service Name**: Provide name for the service. For example, **'dev_s3'**.
  	- Click the toggle :fontawesome-solid-toggle-on: to turn on the **Active Status**.
  	- Under **Select Tag Service**, select **'privacera_tag'** from the drop-down list.
  	- Provide username as **'s3'**.
  	- Provide **Common Name for Certificate** as **'Ranger'**.
  6. Click **SAVE**.


### Updating Custom Repo Name in Databricks

=== "Self Managed and Data Plane"

    --8<-- "docs/connectors/databricks-clusters-fgac/access/snippets/advanced-configuration-self-managed.md"

=== "PrivaceraCloud"

    --8<-- "docs/connectors/databricks-clusters-fgac/access/snippets/advanced-configuration-pcloud.md"


!!! note "When the custom service repo is not defined using any of these methods, the plugin will by default use the service repos starting “privacera_”."


### Validation/Verification

To confirm the successful association of Custom S3 Service repo, perform following steps. Follow the same steps to validate other custom services like Hive, Files, Adls etc.:

  1. Prerequisites:
    - Running Databricks cluster secured in the above steps.
  2. Steps to Validate:
    - Login to Databricks.
    - Create or open an existing notebook. Associate the Notebook with the running Databricks cluster.
    - Use the following PySpark commands to verify S3 CSV file read access.
      ```python
      # Define the S3 path to your file
      s3_path = "s3a://your-bucket-name/path/to/your/file"

      # Read the CSV file from the specified S3 path
      df = spark.read.format("csv").option("header", "true").load(s3_path)

      # Display the first 5 rows of the dataframe
      df.show(5)
      ```
    - On Privacera portal, go to **Access Management** -> **Audits**
    - Check for the **Service Name** which you mentioned in **Creating a Service repo** E.g `dev_s3`..
    - Check for the success or failure of the resource policy. A successful access is indicated as **Allowed** and failure is indicated as **Denied**.


### Fallback to Default Service-Def

After using the custom service, you might need to revert to the default service definition. Follow these steps:

=== "Self Managed and Data Plane"

    1.  **Manually update the ranger_enable.sh (init script):**
        - Open the `ranger_enable.sh` script.
        - Update the property with the default prefix:
          ```shell
          export SERVICE_NAME_PREFIX=privacera
          ```
        - Save the file and use it in Databricks cluster creation.
        - Click on Start or, if the cluster is running, click on Confirm and Restart.

    2.  **Update the vars.databricks.plugin.yml file:**
        - SSH to the instance where Privacera is installed.
        - Run the following command to navigate to the */custom-vars* directory:
          ```shell
          cd ~/privacera/privacera-manager/config/custom-vars
          ```
        - Open the `vars.databricks.plugin.yml` file:
          ```shell
          vi vars.databricks.plugin.yml
          ```
        - Comment out the **DATABRICKS_SERVICE_NAME_PREFIX** property:
          ```shell
          DATABRICKS_SERVICE_NAME_PREFIX: "dev"
          ```
        - Once the property is configured, run the following commands to generate and upload the configuration:
          ```shell
          cd ~/privacera/privacera-manager

          ./privacera-manager.sh post-install
          ```
        - Use the updated `ranger_enable.sh` script in Databricks cluster creation.
        - Click on Start or, if the cluster is running, click on Confirm and Restart.


=== "PrivaceraCloud"

    1.  **Update the privacera_databricks.sh (init script):**
        - Open the `privacera_databricks.sh` script.
        - Remove the below property:
          ```shell
          export SERVICE_NAME_PREFIX=dev
          ```
        - Save the file and use it in Databricks cluster creation.
        - Click on Start or, if the cluster is running, click on Confirm and Restart.

    2.  **Remove an Environment Variable at the Databricks Cluster Level:**
        - Login to Databricks workspace.
        - Navigate to the cluster configuration.
        - Click on **Edit** -> **Advanced options**.
        - Click on the **Spark** tab and remove the following property in Environment variables:
          ```shell
          SERVICE_NAME_PREFIX=dev
          ```
        - Save and click on Start or, if the cluster is running, click on Restart.

    3.  **Remove an Environment Variable at the Databricks Cluster Policy:**
        - Update an existing Databricks cluster policy by removing the below JSON block:
          ```json
          "spark_env_vars.SERVICE_NAME_PREFIX": {
          "type": "fixed",
          "value": "dev"
          }
          ```
        - Create or update a cluster with the above policy.
        - Remove an Environment Variable at the Databricks Cluster Level done in step 2.
        - Save and click on Start or, if the cluster is running, click on Confirm and Restart.


# Use Service Principal id for Authorization

By Default Privacera use display name for [Service Principal](https://docs.databricks.com/en/admin/users-groups/service-principals.html){:target="_blank"}, if you want to use Service Principal Id then perform following steps:

  1. Login to Databricks workspace.
  2. In the left-hand sidebar, click on **Compute**.
  3. Choose the cluster where you want to configure the Service Principal Id.
  4. Click on **Edit** -> **Advanced options**.
  5. Click on the **Spark** tab.
  6. Add below property in **Spark config**
  	 ```shell
  	 spark.hadoop.privacera.fgac.use.displayname false
  	 ```
  7. Click on **Confirm**.
  8. Click on **Start** or if the cluster is running click on **Restart**.


<div class="grid cards" markdown>
-   :material-page-previous: Prev topic: [Setup](setup.md)
-   :material-page-next: Next topic: [Troubleshooting](troubleshooting.md)
</div>