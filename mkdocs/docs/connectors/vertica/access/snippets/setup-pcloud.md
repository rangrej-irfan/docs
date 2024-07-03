1. In PrivaceraCloud, go to **Settings** -> **Applications**.

2. On the **Applications** screen, select **Vertica**.

3. Enter the application **Name** and **Description**. Click **Save**. Name could be any name of your choice. E.g. `Vertica Connector for account 123456`.

4. Open the Vertica application.

5. Enable the **Access Management** option with toggle button.

6. Under the **BASIC** tab, enter the values for:

   * **Vertica JDBC URL** : `jdbc:vertica://<vertica-host>:5433/<database-name>`
   * **Vertica database to connect** : `<database-name>` Database where the connection will be established within Vertica.
   * **Vertica JDBC username** : `vertica` Username for the Vertica database with admin privileges.
   * **Vertica JDBC password** : `password` Password for the Vertica database user used for connection.
   * **Default password for new vertica user** : `password` for new users created by Privacera in Vertica. If SSO is used for Vertica, set this value to *none*.
   * **Vertica owner role** : `vertica` User to be set as owner for all the Vertica resources managed by privacera. Generally value of this should be same as Vertica JDBC username.

7. Click **SAVE**.

8. The configured Vertica connector appears under **Applications**.

9. Once saved and enabled, the Vertica connector will start. Then you can hover on the **VIEW LOGS** button to check the status, either **Running** or **Stopped**.

10. Perform following steps to restart the Vertica connector application:

    1. Go to **Settings** → **Applications** → select the **Vertica** connector application.

    2. Edit the application → Disable it → and Save it.

    3. Open the same application again and then: Enable it → and Save it.
