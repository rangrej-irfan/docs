Perform following steps to configure Databricks FGAC:

1.  SSH to the instance where Privacera is installed.

2.  Run the following command to navigate to the */config* directory.
```shell
cd ~/privacera/privacera-manager/config
```

3. Run the following command to copy the sample vars if not present in custom-vars.
```shell
cp sample-vars/vars.databricks.plugin.yml custom-vars/vars.databricks.plugin.yml
```

4. Modify the following properties: 
```shell
DATABRICKS_HOST_URL: "<PLEASE_UPDATE>"
DATABRICKS_TOKEN: "<PLEASE_UPDATE>"
```

5.  Once the properties are configured, run the following commands to generate and upload configuration 
```shell
cd ~/privacera/privacera-manager

./privacera-manager.sh post-install
```