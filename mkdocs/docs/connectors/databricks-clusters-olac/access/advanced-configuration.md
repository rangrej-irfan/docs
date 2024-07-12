

# JWT Auth Configuration 
By Default Privacera use databricks login user for authorization however we also support JWT (JSON Web Token) integration too and user user/group from payload of JWT instead of databricks login user. 

Here are the steps to configure JWT token integration : 


=== "Self Managed and Data Plane"

    1. asdad

=== "PrivaceraCloud"

    1. asdad 



# Use Service Principal id for Authorization 

By Default Privacera use display name for [Service Principal](https://docs.databricks.com/en/admin/users-groups/service-principals.html){:target="_blank"}, If you want to use Service Principal Id then below configuration:

=== "Self Managed and Data Plane"

	1.  SSH to the instance where Privacera is installed.

	2.  Run the following command to navigate to the */config* directory.
	```shell
	cd ~/privacera/privacera-manager/config
	```
	3. Open dataserver yml file 
	```shell
	vi custom-vars/vars.dataserver.aws.yml 
	```   
	4. Modify/ADD the following properties: 
	```shell 
	DATASERVER_DBX_OLAC_USE_DISPLAY_NAME: "false"
	```
	6.  Once the properties are configured, Run the following commands to generate configuration 
	```shell
	cd ~/privacera/privacera-manager
	./privacera-manager.sh setup 
	```
	7. Deploy changes : 
	```shell
	cd ~/privacera/privacera-manager
	./pm_with_helm.sh install
	```

=== "PrivaceraCloud"
	1. In PrivaceraCloud, go to **Settings** -> **Applications** -> **S3** -> **S3** 
	2. Click on  **Access Management** ->  **Advanced** 
    4. Under **Add New Custom Properties** put below properties 
	```shell 
	dataserver.dbx.olac.use.displayname=false  
	```


<div class="grid cards" markdown>
-   :material-page-previous: Prev topic: [Setup](setup.md)
-   :material-page-next: Next topic: [Troubleshooting ](troubleshooting.md)
</div>
