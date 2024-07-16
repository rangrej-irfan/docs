## Realtime Scan

By default, Privacera Discovery scans resources that are added to an
application (realtime scanning). When a parent resource entry is added to the
**Include Resource** tab of the **Data Source** page, any changes to that
resource is monitored such as a file being added to a folder or table being
added within a database. On detection of those events, a real time scan is
initiated on newly added resource.

To scan the resource in realtime, the application should be enabled and
resource should be added to the **Include Resource** tab in the application.

Realtime scan is supported on the following datasources:

Table 76. Supported Datasources for Realtime Scan

<table>  
<tr>  
<th>

Application

</th>  
<th>

Cloud

</th></tr>  
<tr>  
<td>

S3

</td>  
<td>

AWS

</td></tr>  
<tr>  
<td>

ADLS

</td>  
<td>

Azure

</td></tr>  
<tr>  
<td>

Google Cloud Storage and Google BigQuery

</td>  
<td>

GCP

</td></tr></table>



###### Prerequisites

Make sure following prerequisites are met for supporting realtime scan:

1. Application is configured, and a successful test connection has been established.

2. Ensure that the **Enable Real-Time toggle** is enabled under **APPLICATION PROPERTIES** at the time of application configuration.

3. Make sure Realtime configuration is done on respective (AWS, AZURE or GCP) console depending on the cloud environment.

    1. For AWS S3, perform the steps given in [Configure S3 for real-time scanning on Privacera Platform](configure-s3-for-real-time-scanning-on-privacera-platform.html "Configure S3 for real-time scanning on Privacera Platform").

    2. For AZURE ADLS, perform the steps given in [Enable Pkafka for real-time audits in Discovery on Privacera Platform](enable-pkafka-for-real-time-audits-in-discovery-on-privacera-platform.html "Enable Pkafka for real-time audits in Discovery on Privacera Platform").

    3. For GCP GCS and GBQ, perform the steps given in [Google Sink to Pub/Sub](google-sink-to-pub-sub.html "Google Sink to Pub/Sub").

###### Procedure for Enabling Realtime Scan

1. Go to **Discovery** > **Data Sources**.

2. From the **Applications** list, select the application.

3. Click **ADD**.

4. For GBQ application, add values for **Dataset Name** and **Table Name** fields.

### Note

Add ***** in Table Name field for real scan of any tables added or modified in
the given Dataset.

For file system, add folder as a **Resource**.

### Important

Ensure the value for the **Scan Type** field is set as `Scan`.

5. Click **SAVE**.

6. Go to Cloud console and upload a file in folder which added as a resource in preceding step.

7. Under **Diagnostics** > **Health Check** > **Kafka/Kinesis** or **Pub/Sub topics** , check for audit consumption in the following kafka topics:

    1. For S3: `privacera_scan_worker_aws_s3_{DEPLOYMENT_ENV_NAME}`

    2. For ADLS: `event_hub_{DEPLOYMENT_ENV_NAME}`

    3. For GCS: `privacera_audits_{DEPLOYMENT_ENV_NAME} belongs to privacera_googlecloud_audits_group_{DEPLOYMENT_ENV_NAME}`

    4. For GBQ: `privacera_audits_{DEPLOYMENT_ENV_NAME} belongs to privacera_googlebigquery_audits_group_{DEPLOYMENT_ENV_NAME}`

8. Check scan entry of uploaded file in resource under Scan Summary Report with **Realtime scan** as a reason.

9. Check for the **Classifications** for that Scanned Resource.

## View classification results

You can view scan results on the **Classification** page. For more
information, see [Classifications overview](classifications.html
"Classifications overview").
