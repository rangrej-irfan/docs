---
title: Setup for Access Management for Databricks all-purpose compute clusters with Fine-Grained Access Control (FGAC)
---

# Setup for Access Management for Databricks all-purpose compute clusters with Fine-Grained Access Control (FGAC)

# Configure 

=== "Self Managed and Data Plane"

    --8<-- "docs/connectors/databricks-clusters-fgac/access/snippets/setup-self-managed.md"

=== "PrivaceraCloud"

    --8<-- "docs/connectors/databricks-clusters-fgac/access/snippets/setup-pcloud.md"



# Create Databricks cluster policy 
+We recommend to use [Databricks cluster policy](https://docs.databricks.com/en/admin/clusters/policies.html){:target="_blank"} to control cluster configuration. Here are the steps to create cluster policy: 

  - Log in to **Databricks Web UI** 
  - Click on the **Compute** icon on the sidebar
  - Click on the **Policies** tab
  - Click on the **Create policy** button 
  - Provide a name to the policy i.e **privacera-fgac-cluster-policy**
  - Add below policy definition, and replace <instance-profile-arn> with your actual instance-profile-arn 
```shell
{
  "spark_conf.spark.databricks.isv.product": {
    "type": "fixed",
    "value": "privacera"
  },
  "spark_conf.spark.driver.extraJavaOptions": {
    "type": "fixed",
    "value": "-javaagent:/databricks/jars/privacera-agent.jar"
  },
  "spark_conf.spark.databricks.repl.allowedLanguages": {
    "type": "fixed",
    "value": "sql,python,r"
  },
  "spark_conf.spark.databricks.delta.formatCheck.enabled": {
    "type": "fixed",
    "value": "false"
  },
  "aws_attributes.instance_profile_arn": {
    "type": "fixed",
    "value": "<instance-profile-arn>"
  }
}

```


# Create Databricks cluster  
+Here are the steps to create databricks cluster with Privacera plugin (FGAC): 

  1. Log in to **Databricks Web UI** 
  2. Click on the **Compute** icon on the sidebar
  3. Click the **Create Compute** button.
  4. Fill in the cluster configuration details.
  5. Under the Cluster Policies dropdown which we created in previous step (i.e **privacera-fgac-cluster-policy**)
  6. Under the **Advanced option** :
    - Select the source as **Workspace** for init scripts.
    - Specify the Workspace file path:
        - Self Managed and Data Plane
            - /privacera/{DEPLOYMENT_ENV_NAME}/ranger_enable.sh
        - PrivaceraCloud 
            - /privacera/{DEPLOYMENT_ENV_NAME}/privacera_databricks.sh  
  7. Click on the **Add** button.
  8. Click **Create Compute** to create the cluster.

<div class="grid cards" markdown>
-   :material-page-previous: Prev topic: [Prerequistes](prerequisites.md)
-   :material-page-next: Next topic: [Advanced Configuration](advanced-configuration.md)
</div>
