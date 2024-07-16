
# Overview of Supported Data Sources


Privacera Discovery's key feature is scanning your data for sensitive information, providing tagged classifications for analysis and refinement.

Privacera Discovery crawls targeted data sources to identify and applies metadata labels called tags to potentially sensitive data, such as credit card numbers or email addresses.

Access Manager Tag Policies can then be created so that user access can be controlled and monitored.

## Connecting Data sources to Discovery

You can configure the applications supported by Privacera Discovery in
**Settings > Applications**.

## Data sources Connectors supported by Privacera Discovery

| **Category**        | **Data Source Connectors**                                                                                                                                                                                                                    |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Databases**       | [Vertica](../../../connectors/vertica/discovery/index.md), Amazon Redshift, Apache Hive, Apache HBase, Apache Kudu, Apache Phoenix, Azure SQL Database, Google BigQuery, Microsoft SQL Server, MySQL, Oracle, PostgreSQL, Snowflake, Teradata |
| **Cloud Storage**   | Amazon S3, Azure Data Lake Storage (ADLS), Google Cloud Storage (GCS)                                                                                                                                                                         |
| **File Systems**    | HDFS, Local Filesystem, NFS, SFTP                                                                                                                                                                                                             |

## Supported File Formats for Discovery Scans

| **Type**             | **Formats**                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------|
| **Structured Data**  | .avro, .avro (nested), .csv, .html, .json, .json (nested), .orc, .parquet, .parquet (nested), .sas, .tsv, .xls, .xlsx, .xml |
| **Compressed/Archive Data** | .gzip (single or multiple files), .gz (single or multiple files), .lzo/.lzop, .jar (single or multiple files), .tar.gz (single or multiple files), .snappy.parquet, .snappy.orc, .snappy.avro, .zip (single or multiple files), .zlib.orc, .zlib.parquet, .zlib.avro |
| **Unstructured Data**| .dat, .doc, .docx, .pdf, .txt                                                                 |
| **Media Data**       | *For metadata extraction only:* .jpeg, .mp4, .mpeg                                            |
| **Database Data**    | *For Database binary type columns is skipped and only non-binary columns data is scanned:*    |

	



<div class="grid cards" markdown>
-   :material-page-previous: Prev Topic: [Quick Start](../start/quick-start.md)
-   :material-page-next: Next Topic: [Starting Scan](../scanning/index.md)
</div>
