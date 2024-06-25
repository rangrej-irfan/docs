Perform following steps to configure Vertica connector for PolicySync.

1. SSH to the instance where Privacera is installed.

1. Run the following command to navigate to the */config* directory.
```shell
cd ~/privacera/privacera-manager/config
```

1. Run the following command to create a new directory:
```shell
mkdir -p custom-vars/connectors/vertica/instance1`
```

1. Copy the sample connector configuration file to your custom directory:
```shell
cp sample-vars/vars.connector.vertica.yml custom-vars/connectors/vertica/instance1/
```

1. Open the `.YAML` file for editing to customize it according to your configurations:
```shell
vi custom-vars/connectors/vertica/instance1/vars.connector.vertica.yml
```

1. Modify the following properties:
      - `CONNECTOR_VERTICA_JDBC_URL` - Enter the JDBC URL for connecting to the Vertica database
      - `CONNECTOR_VERTICA_JDBC_DB` - Enter the database where the connection will be established within Vertica.
      - `CONNECTOR_VERTICA_JDBC_USERNAME` - Enter the username for the Vertica database with admin privileges.
      - `CONNECTOR_VERTICA_JDBC_PASSWORD` - Enter the password for the Vertica database user used for connection.
      - `CONNECTOR_VERTICA_DEFAULT_USER_PASSWORD` - The default password assigned to new users created by Privacera in Vertica. If SSO is used for Vertica, set this value to *none*.
      - `CONNECTOR_VERTICA_OWNER_ROLE` - User to be set as owner for all the Vertica resources managed by privacera. Generally value of this should be same as Vertica JDBC username.

 To know more about property details and their description, see [Properties for
Vertica Connector](properties-for-vertica-connector.html "Properties for
Vertica Connector").

1. Make the required changes in the file, save and exit the text editor.

1. Once the properties are configured, run the following commands to apply your changes through Privacera Manager:
```shell
cd ~/privacera/privacera-manager
./privacera-manager.sh update
```
