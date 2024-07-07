# PrivaceraCloud Data Plane Discovery Configuration

## Enable Discovery features 

Run the following commands on the Privacera Manager host to enable Discovery features
in Self Managed and PrivaceraCloud Data Plane deployments.

=== "AWS"

    Copy the `vars.discovery.aws.yml` from `config/sample-vars` to `config/custom-vars` and edit the file.
    ```bash 
    cd ~/privacera/privacera-manager
    cp config/sample-vars/vars.discovery.aws.yml config/custom-vars/
    vi config/custom-vars/vars.discovery.aws.yml 
    ```
    
    Add or edit the following variables:
    ```bash 
    # Add or edit the following variables in the file
    DISCOVERY_BUCKET_NAME: “<Your_Discovery_Configuration_Bucket_Name>”
    
    DISCOVERY_USE_POD_IAM_ROLE: "true"
    DISCOVERY_IAM_ROLE_ARN: "<PLEASE_CHANGE>"
    
    DISCOVERY_CONSUMER_ENABLE: "true"
    DISCOVERY_CONSUMER_USE_POD_IAM_ROLE: "true"
    DISCOVERY_CONSUMER_IAM_ROLE_ARN: "<PLEASE_CHANGE>"
    
    PORTAL_USE_POD_IAM_ROLE: "true"
    PORTAL_IAM_ROLE_ARN: "<PLEASE_CHANGE>"
    
    DISCOVERY_K8S_SPARK_DYNAMIC_ALLOCATION_ENABLED: "true"
    ```

=== "Azure"

    Copy the `vars.discovery.azure.yml` from from `config/sample-vars` to `config/custom-vars`.
    ```bash 
    cd ~/privacera/privacera-manager  
    cp config/sample-vars/vars.discovery.azure.yml config/custom-vars
    vi config/custom-vars/vars.discovery.azure.yml
    ``` 

    Add or edit the following variables:
    ```bash 
    DISCOVERY_FS_PREFIX: "<PLEASE_CHANGE>"
    DISCOVERY_AZURE_STORAGE_ACCOUNT_NAME: <PLEASE_CHANGE>"
    DISCOVERY_AZURE_STORAGE_ACCOUNT_KEY: "<PLEASE_CHANGE>"

    DISCOVERY_AZURE_LOCATION: "<PLEASE_CHANGE>"

    CREATE_AZURE_RESOURCES: "false"

    DISCOVERY_AZURE_RESOURCE_GROUP: "<PLEASE_CHANGE>"

    DISCOVERY_AZURE_COSMOS_DB_ACCOUNT: "<PLEASE_CHANGE>"
    DISCOVERY_COSMOSDB_URL: <PLEASE_CHANGE>"
    DISCOVERY_COSMOSDB_KEY: "<PLEASE_CHANGE>"

    DISCOVERY_CONSUMER_ENABLE: "true"
    ```


=== "GCP"

    Copy the `vars.discovery.gcp.yml` from from `config/sample-vars` to `config/custom-vars` and edit the file.
    ```bash 
    cd ~/privacera/privacera-manager
    cp config/sample-vars/vars.discovery.gcp.yml config/custom-vars/
    vi config/custom-vars/vars.discovery.gcp.yml
    ```
    
    Add or edit the following variables:
    ```bash
    BIGTABLE_INSTANCE_ID: "<PLEASE_CHANGE>"
    DISCOVERY_BUCKET_NAME: "<PLEASE_CHANGE>"
    ```

## Enable Kafka for Discovery

Copy the `vars.kafka.yml` from from `config/sample-vars` to `config/custom-vars` and edit the file.

```bash 
cd ~/privacera/privacera-manager
cp config/sample-vars/vars.kafka.yml config/custom-vars/
vi config/custom-vars/vars.kafka.yml
```

Add or edit the following variables:
```bash
# Add or edit the following variables in the file
USE_KAFKA_SPECIFIC_STORAGE_CLASS: "true"
```

## Enable real-time discovery features

Run the following commands on the Privacera Manager host to enable real-time discovery features
for Self Managed and PrivaceraCloud Data Plane deployments.

=== "AWS"

    Copy the `vars.pkafka.aws.yml` from `config/sample-vars` to `config/custom-vars` and edit the file.
    ```bash
    cd ~/privacera/privacera-manager
    cp config/sample-vars/vars.pkafka.aws.yml config/custom-vars/
    vi config/custom-vars/vars.pkafka.aws.yml
    ```

    Add or edit the following variables:
    ```bash
    PKAFKA_SQS_ENDPOINT: "<PLEASE_CHANGE>"

    PKAFKA_USE_POD_IAM_ROLE: "true"
    PKAFKA_IAM_ROLE_ARN: "<PLEASE_CHANGE>"
    ```

    Set the value of PKAFKA_SQS_ENDPOINT to the value of SQS Queue name URL, as
    per the following format. To know more, see [Amazon SQS queue name
    URL](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-
    queue-message-identifiers.html#queue-name-url).

    `https://sqs.<AWS_REGION>.amazonaws.com/<ACCOUNT_ID>/privacera_bucket_sqs_<DEPLOYMENT_ENV_NAME>`


=== "Azure"

    Copy the `vars.pkafka.azure.yml` from `config/sample-vars` to `config/custom-vars` and edit the file.
    ```bash
    cd ~/privacera/privacera-manager
    cp config/sample-vars/vars.pkafka.azure.yml config/custom-vars/
    vi config/custom-vars/vars.pkafka.azure.yml
    ```

    Add or edit the following variables:
    ```bash
    PKAFKA_EVENT_HUB: "<PLEASE_CHANGE>"
    PKAFKA_EVENT_HUB_NAMESPACE: "<PLEASE_CHANGE>"
    PKAFKA_EVENT_HUB_CONSUMER_GROUP: "<PLEASE_CHANGE>"
    PKAFKA_EVENT_HUB_CONNECTION_STRING: "<PLEASE_CHANGE>"
    ```

=== "GCP"

    Copy the `vars.pkafka.gcp.yml` from `config/sample-vars` to `config/custom-vars` and edit the file.
    ```bash
    cd ~/privacera/privacera-manager
    cp config/sample-vars/vars.pkafka.gcp.yml config/custom-vars/
    vi config/custom-vars/vars.pkafka.gcp.yml
    ```

    Add or edit the following variables:
    ```bash
    PKAFKA_GCP_SINK_DESTINATION_PUBSUB_SUBSCRIPTION_NAME: "<PLEASE_CHANGE>"
    ```

## Enable Discovery Classification push to Ranger Tags

Run the following commands on the Privacera Manager host to enable Discovery tags push to Ranger
    
```bash
cd ~/privacera/privacera-manager
vi config/custom-vars/vars.discovery.agent.yml
```
    
```bash
DISCOVERY_RANGER_TAGSYNC_USERNAME: "<PLEASE_CHANGE>"
RANGER_TAGSYNC_PASSWORD: "<PLEASE_CHANGE>"
DISCOVERY_RANGER_REST_ENABLED: "true"
```
