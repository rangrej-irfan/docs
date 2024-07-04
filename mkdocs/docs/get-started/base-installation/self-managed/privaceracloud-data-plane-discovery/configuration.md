# PrivaceraCloud Data Plane Discovery Configuration

## AWS 

Run the following commands on the Privacera Manager host - 

```bash 
cd ~/privacera/privacera-manager
cp config/sample-vars/vars.discovery.aws.yml config/custom-vars/
vi config/custom-vars/vars.discovery.aws.yml 
```

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

```bash 
cd ~/privacera/privacera-manager
cp config/sample-vars/vars.kafka.yml config/custom-vars/
vi config/custom-vars/vars.kafka.yml
```
```bash
# Add or edit the following variables in the file
USE_KAFKA_SPECIFIC_STORAGE_CLASS: "true"
```

