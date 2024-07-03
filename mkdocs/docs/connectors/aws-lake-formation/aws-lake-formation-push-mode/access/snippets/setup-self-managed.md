Perform following steps to configure AWS Lake Formation connector using Push mode:

1.  SSH to the instance where Privacera is installed.

2.  Run the following command to navigate to the */config* directory.
```shell
cd ~/privacera/privacera-manager/config
```
        

3.  Run the following command to create a new directory:
```shell
mkdir -p custom-vars/connectors/lakeformation/instance1
```

4.  Run the following command to copy the sample vars:
```shell
cp sample-vars/vars.connector.lakeformation.push.yml custom-vars/connectors/lakeformation/instance1/
```

5.  Run the following command to open the *.yml* file to be edited.
```shell
vi custom-vars/connectors/lakeformation/instance1/vars.connector.lakeformation.push.yml
```

6.  Modify the following properties:

    -   `CONNECTOR_LAKEFORMATION_AWS_ACCOUNT_ID` - Enter the AWS Account
        ID of the account you will be running the AWS Lake Formation
        connector.

    -   `CONNECTOR_LAKEFORMATION_AWS_REGION` - Set AWS region to connect
        to your AWS Lake Formation instance.

    -   `CONNECTOR_LAKEFORMATION_ENABLE_PUSH_POLICIES_TO_RANGER` - Set
        this to true, if you want to push policies to other policy
        repositories.

    -   `CONNECTOR_LAKEFORMATION_SINK_HIVE_SERVICE_APP_ID` - Set the
        policy repository name where you want the connector to push
        policies for the hive.


7.  Once the properties are configured, run the following commands to
    update your Privacera Manager platform instance:
```shell
cd ~/privacera/privacera-manager

./privacera-manager.sh update
```