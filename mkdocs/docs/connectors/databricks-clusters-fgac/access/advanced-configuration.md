---
title: Advanced Configuration for Access Management for Databricks all-purpose compute clusters with Fine-Grained Access Control (FGAC)
---

# Advanced Configuration for Access Management for Databricks all-purpose compute clusters with Fine-Grained Access Control (FGAC)

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

To confirm the successful association of Custom Service repo, follow these steps:

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