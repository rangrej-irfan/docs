## Steps to get installation logs and version file: 

Here are the steps to get Installation logs and Privacera plugin version files from DBFS: 


- Privacera init script generate two files in dbfs at location dbfs:/privacera/cluster-logs/&lt;CLUSTER_NAME&gt;/
- Commands to list files from dbfs location 
```shell
dbfs ls dbfs:/privacera/cluster-logs/<CLUSTER_NAME>/
```

	- Folder will have two files 
		- **privacera.out** : Installation log 
		- **privacera_version.txt** : Privacera plugin version details.

- Command to get files on local: 
```shell
dbfs cp dbfs:/privacera/cluster-logs/<CLUSTER_NAME>/  . --recursive
```