There are three ways to include the custom repo name. You can choose any one of the following methods:

  1. **Update the privacera_databricks.sh (init script):**
  	- Open the `privacera_databricks.sh` script.
	  - Add this after API_SERVER_URL="https://xxxxxxxx/api" to include the custom repo name:
   	   ```shell
       export SERVICE_NAME_PREFIX=dev
       ```
    - Save file and use it in Databricks cluster creation.
    - Click on Start or, if the cluster is running, click on Confirm and Restart.

  2. **Set an Environment Variable at the Databricks Cluster Level:**
  	- Login to Databricks workspace.
  	- Navigate to the cluster configuration.
  	- Click on Edit -> Advanced options.
  	- Click on the Spark tab and add below property in Environment variables
  	   ```shell
  	   SERVICE_NAME_PREFIX=dev
  	   ```
  	- Save and click on Start or, if the cluster is running, click on Restart.

  3. **Set an Environment Variable in the Databricks Cluster Policy:**
    - Create or update existing databricks cluster policy using below json block:
       ```json
       "spark_env_vars.SERVICE_NAME_PREFIX": {
       "type": "fixed",
       "value": "dev"
       }
       ```
    - Create or update a cluster with the above policy to set the environment variable on the cluster.
    - Set the Spark configuration done in step 2.
    - Save and click on Start or, if the cluster is running, click on Confirm and Restart.
