Perform following steps to configure Databricks OLAC:

1.  SSH to the instance where Privacera is installed.

2.  Run the following command to navigate to the */config* directory.
```shell
cd ~/privacera/privacera-manager/config
```
        
3.  Run the following command to copy the sample vars:
```shell
cp sample-vars/vars.databricks.scala.yml custom-vars/vars.databricks.scala.yml
```

4. **[Optional]** Run the following command to copy the sample vars if not present in custom-vars.
```shell
cp sample-vars/vars.databricks.plugin.yml custom-vars/vars.databricks.plugin.yml
```

5. Modify the following properties: 


6.  Once the properties are configured, run the following commands to generate and upload configuration 
```shell
cd ~/privacera/privacera-manager

./privacera-manager.sh post-install
```