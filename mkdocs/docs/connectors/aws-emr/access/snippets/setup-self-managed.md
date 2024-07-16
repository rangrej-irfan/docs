Perform following steps to configure EMR connector:

1.  SSH to the instance where Privacera is installed.

2.  Run the following command to navigate to the */config* directory.
```shell
cd ~/privacera/privacera-manager/config
```

3. Run the following command to copy the sample vars:
```shell
cp sample-vars/vars.emr.yml custom-vars/
```

4. Run the following command to open the *.yml* file to be edited.
```shell
vi custom-vars/vars.emr.yml
```

5. Modify the following properties:

    | Variable                                                     | Definition                                                              |
    |--------------------------------------------------------------|-------------------------------------------------------------------------|
    | EMR_CLUSTER_NAME                                             | Enter unique name for the EMR cluster.                                  |
    | EMR_VERSION                                                  | Enter the emr version (ex: emr-7.1.0)                                   |
    | **Security group config**                                    | 
    | EMR_MASTER_SG_ID                                             | Set Security Group ID for EMR Master Node Group.                        |
    | EMR_SLAVE_SG_ID                                              | Set Security Group ID for EMR Slave Node Group.                         |
    | EMR_SERVICE_ACCESS_SG_ID                                     | Set Security Group ID for EMR Service Access                            |
    | **Instance config**                                          | 
    | EMR_SUBNET_ID                                                | Subnet ID for the instance.                                             |
    | EMR_KEYPAIR                                                  | Existing EC2 key pair to SSH into the master node.                      |
    | EMR_EC2_MARKET_TYPE                                          | EC2 instance market type. Supported: SPOT, ON_DEMAND                    |
    | EMR_EC2_INSTANCE_TYPE                                        | EC2 instance type. ex: m5.xlarge                                        |
    | EMR_MASTER_NODE_COUNT                                        | Number of master node instances in the cluster.                         |
    | EMR_CORE_NODE_COUNT                                          | Number of core node instances in the cluster.                           |
    | **Security config**                                          |
    | EMR_SECURITY_CONFIG                                          | Name of the Security Configurations created for EMR.                    |
    | EMR_KERBEROS_ENABLE                                          | Enable kerberos, this should be set to 'true'.                          |
    | EMR_KDC_ADMIN_PASSWORD                                       | Cluster KDC admin password.                                             |
    | EMR_CROSS_REALM_PASSWORD                                     | Cross realm principle password.                                         |
    | EMR_KERB_REALM                                               | Specifies the Kerberos realm name.                                      |
    | EMR_KERB_DOMAIN                                              | Specifies the domain name of the other realm.                           |
    | EMR_KERB_ADMIN_SERVER                                        | Specifies the FQDN or IP address of the admin server.                   |
    | EMR_KERB_KDC_SERVER                                          | Specifies the FQDN or IP address of the KDC server.                     |
    | **AWS Account & IAM config**                                 |
    | EMR_AWS_ACCT_ID                                              | AWS Account ID where EMR Cluster will be created.                       |
    | EMR_DEFAULT_ROLE                                             | Role attached to EMR Cluster for performing cluster related activities. |
    | EMR_ROLE_FOR_CLUSTER_NODES                                   | IAM Role which will be attached to each node in the EMR Cluster.        |
    | EMR_ROLE_FOR_APPS                                            | IAM Role name which will be used by all EMR Apps.                       |
    | **Spark OLAC / FGAC config**                                 |
    | EMR_APP_SPARK_OLAC_ENABLE                                    | Set to enable Object-Level Access Controle (OLAC) for EMR Spark.        |
    | EMR_APP_SPARK_FGAC_ENABLE                                    | Set to enable Fine-Grained Access Controle (FGAC) for EMR Spark.        |
    | **Trino config**                                             |
    | EMR_APP_PRESTO_SQL_ENABLE                                    | Set to enable trino plugin for EMR Trino.                               |
    | EMR_APP_PRESTO_DB_ENABLE                                     | Set to enable prestodb plugin for EMR PrestoDB.                         |
    | **Other config**                                             |
    | EMR_LOGS_PATH                                                | S3 location for storing EMR cluster logs.                               |


6. Once the properties are configured, run the following commands to
    update your Privacera Manager platform instance:
```shell
cd ~/privacera/privacera-manager

./privacera-manager.sh update
```

7. After the update is finished, all the cloud-formation JSON template files will be available at the path:
```shell
~/privacera/privacera-manager/output/emr/
```

## Create EMR cluster
To create EMR cluster any one of the following approach can be followed:

- [Using AWS CLI](#using-aws-cli)
- [Using AWS Console](#using-aws-console)

### Using AWS CLI
  1. Run the following command to create the EMR cluster:
```shell
aws cloudformation create-stack --stack-name privacera-emr-creation --template-body file://<emr_template_json_file> --region <aws_region>
```

### Using AWS Console
   1. Navigate to the AWS CloudFormation console.
   2. Click on **Create stack**.
   3. Select **Upload a template file**.
   4. Click on **Choose file** and select the JSON template file.
   5. Click on **Next**.
   6. Enter the stack name and click on **Next**.
   7. Click on **Next**.
   8. Click on **Create stack**.