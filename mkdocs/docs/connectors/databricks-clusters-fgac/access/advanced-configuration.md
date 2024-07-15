# Custom s3 ranger policy 

Perform following steps to create custom s3 ranger policy repo:

  1. Login to Privacera portal.
  2. Go to **Access Management** -> **Resource Policies**.
  3. Under s3, click more icon :material-dots-vertical:.
  4. Select **Add Service**.
  5. Under **Add Service**, provide values for the following fields:
  	- **Service Name**: Provide name for the service. For example, **'privacera-dev_s3'**.
  	- Click the toggle :fontawesome-solid-toggle-on: to turn on the **Active Status**.
  	- Under **Select Tag Service**, select **'privacera_tag'** from the drop-down list.
  	- In the **Common Name for Certificate** field, type **'Ranger'**.
  	- Under **Add New Configurations**, provide key as **'policy.download.auth.users'** and value as **'root'** in the respective fields.
  6. Click **SAVE**.


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