# Configuring and Running Discovery Scans

Privacera Discovery scans are used to identify sensitive data in connected data sources.

## Discovery scan targets

After an application data source has been connected, subsets of that data can be
configured as scan targets.

To define a Privacera Discovery scan target:

1. To add specific databases and tables to be scan targets, go to **Discovery > Data Source**.

2. Click the desired application in the **Applications** section.

3. Click **ADD** to define a subset of that Datasource for scanning.
	
	* Enter the database name (_database_ or for Snowflake _database_._schema_) or wildcard asterisk for all databases.
	
	* Enter one or more comma-separated table names or wildcard asterisk for all tables. Wildcard asterisks can also be used in table names as prefix, suffix, or inside the name.

### Start a scan

After a scan target is established, it can be scanned. Each database/table set
is listed by row, under **Scanning Details**. The columns are: **Database** ,
**Tables** , and **Actions**.

To start a scan, click **SCAN RESOURCE**.

The following message is displayed:

> Scan request is in the queue, please check after 2 minutes.

### View a scan

Completion status and various statistics for all scan **Discovery > Scan
Status**.

<div class="grid cards" markdown>
- 	:material-page-previous: Previous topic: [Connecting Data Sources](../sources/index.md)
-   :material-page-next: Next topic: [Processing Order of Scan](setup/defining-scans.md)
</div>