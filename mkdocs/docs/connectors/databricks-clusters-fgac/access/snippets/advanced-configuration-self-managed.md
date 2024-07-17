There are two ways to include the custom repo name. You can choose any one of the following methods:

  1. **Manually update the ranger_enable.sh (init script):**
  	- Open the `ranger_enable.sh` script.
	  - Update below property with prefix you used for creating new service repo. E.g. `dev`. By default, it is `privacera`
   	   ```shell
       export SERVICE_NAME_PREFIX=dev
       ```
    - Save file and use it in Databricks cluster creation.
    - Click on Start or, if the cluster is running, click on Confirm and Restart.

  2. **Update the vars.databricks.plugin.yml file:**
    - SSH to the instance where Privacera is installed.
    - Run the following command to navigate to the */custom-vars* directory.
      ```shell
      cd ~/privacera/privacera-manager/config/custom-vars
      ```
    - Open vars.databricks.plugin.yml file.
      ```shell
      vi databricks.plugin.yml
      ```
    - Uncomment the **DATABRICKS_SERVICE_NAME_PREFIX** property and update your custom service name prefix.
      ```shell
      DATABRICKS_SERVICE_NAME_PREFIX: "dev"
      ```
    - Once the property is configured, run the following commands to generate and upload configuration 
      ```shell
      cd ~/privacera/privacera-manager

      ./privacera-manager.sh post-install
      ```
    - Use the updated `ranger_enable.sh` script in Databricks cluster creation.
    - Click on Start or, if the cluster is running, click on Confirm and Restart.