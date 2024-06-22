1. In PrivaceraCloud, go to **Settings** -> **Applications**.

2. On the **Applications** screen, select **Lakeformation Push Mode**.

3. Enter the application **Name** and **Description**. Click **Save**. Name could be any name of your choice. E.g. `AWS Lake Formation Connector for account 123456`.

4. Open the AWS Lake Formation application.

5. Enable the **Access Management** option with toggle button.

6. Under the **BASIC** tab, enter the values for:

   * **AWS Account ID** : `12345XXX`

   * **AWS Assume IAM Role ARN** : `Use the role ARN created for the AWS Lake Formation connector.`

   * **AWS Region** : e.g. `us-east-1`

7. Click **SAVE**.

8. The configured AWS Lake Formation connector appears under **Applications**.

9. Once saved and enabled, the AWS Lake Formation connector will start. Then you can hover on the **VIEW LOGS** button to check the status, either **Running** or **Stopped**.

10. Perform following steps to restart the AWS Lake formation connector application:

    1. Go to **Settings** → **Applications** → select the****Lake formation** connector application** .

    2. Edit the application → Disable it → and Save it.

    3. Open the same application again and then: Enable it → and Save it.