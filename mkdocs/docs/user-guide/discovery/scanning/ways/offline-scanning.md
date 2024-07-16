## Offline Scan

You can conduct manual or on demand scans (Offline scan) of resources from the
**Data Sources** page.

Offline scan is supported on the following datasources:

Table 75. Supported Datasources for Offline Scan

<table>  
<tr>  
<th>

Cloud

</th>  
<th>

Application

</th></tr>  
<tr>  
<td>

AWS

</td>  
<td>

1. Databricks Unity Catalog

2. Databricks SQL

3. DynamoDB

4. EMR HIVE

5. MySQL

6. Oracle

7. Postgres

8. PrestoSQL

9. Redshift

10. S3

11. Snowflake

12. Starburst Trino

13. Vertica

</td></tr>  
<tr>  
<td>

Azure

</td>  
<td>

1. ADLS

2. Databricks SQL

3. MySQL

4. Oracle

5. PrestoSQL

6. Postgres

7. Starburst Trino

8. Synapse

9. Vertica

</td></tr>  
<tr>  
<td>

GCP

</td>  
<td>

1. Google BigQuery

2. Google Cloud Storage

</td></tr></table>



###### Prerequisites

Make sure following prerequisites are met before starting offline scan:

1. Application is configured, and a successful test connection has been established.

2. Ensure that the application is enabled for offline scanning.

###### Procedure for Offline Scan

1. Go to **Discovery** > **Data Sources**.

2. From the **Applications** list, select the application.

3. Click **ADD**.

4. For JDBC applications, add values for **Database Name** and **Table Name** fields under **Add Database or Table**.

For file systems, add file or folder as a **Resource**.

### Important

Ensure the value for the **Scan Type** field is set as `Scan`.

5. Click **SAVE**.

6. Under **Actions** column, click **SCAN RESOURCE** for the Database and the Table or file or folder added in the preceding step.

### Note

It may take few minutes to complete the Scan Resource process. The process of
Offline Scanning progresses through different stages, starting from "Pending"
and moving to "Listing," "Running," and finally "Success" on the Scan status
page.

7. Go to **Discovery** > **Scan Status**.

Ensure the status of the Scan Resource is **SUCCESS**.

8. Click Scan ID or Resource of the Application. It shows the **Classifications** for that Scan Resource.

<div class="grid cards" markdown>
- 	:material-page-previous: Previous topic: [Processing Order of Scan](../setup/defining-scans.md)
-   :material-page-next: Next topic: [Realtime Scan](realtime-scanning.md)
</div>