1. In PrivaceraCloud, go to **Settings** -> **Applications**.

2. On the **Applications** screen, select **EMR**.

3. Enter the application **Name** and **Description**. Click **Save**. Name could be any name of your choice. E.g. `AWS EMR Connector for account 123456`.

4. Open the **EMR** application.

5. Enable the **Access Management** option with toggle button.


## Configure shared-secret
**Note:** This step is required only for EMR Spark OLAC.

1. In PrivaceraCloud, go to **Settings** -> **Applications**.
   - For more information about how to connect S3 application, see Connect S3 to PrivaceraCloud.
2. On the **Applications** screen, select **S3**.
3. On the screen click the edit icon and navigate to 'ADVANCED' tab. 4
4. Add the following property:
   dataserver.shared.secret=<shared_secret_value>
5. Click Save.

## Privacera Plugin Script
1. In PrivaceraCloud, go to **Settings** -> **Applications**.
2. On the **Applications** screen, select **EMR**.
3. From the screen, either copy the download url or download the script.
4. If you have downloaded the script, then follow the below steps:
    - Upload to specific s3 bucket location
    - Get the object url of the uploaded script file from s3

## EMR Bootstrap action

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