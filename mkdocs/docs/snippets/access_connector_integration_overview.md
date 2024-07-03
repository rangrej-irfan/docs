Privacera uses the most efficient integration mechanisms to enforce permissions in various data sources. The three
common mechanisms are:

1. **Privacera PolicySync**: Policies are defined in Privacera and then pushed down to the data source, where they are
   enforced by the native system. This mechanism is commonly used for managing policies in most RDBMSs.

2. **Apache Ranger Plugin**: These lightweight Java libraries are embedded within the compute environment of the data
   source. The plugins enforce policies in real-time and send audit logs to the central audit service.

3. **Privacera DataServer**: For integrations such as AWS S3, Azure ADLS, and GCP GCS, the DataServer can generate
   signed URLs, which are then provided to the compute environment for data retrieval or updates. This approach is
   commonly used in integrations like Apache Spark or other Java libraries.