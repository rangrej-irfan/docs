# AWS Lake Formation

AWS Lake Formation is a fully managed service that makes it easy to build,
secure, and manage data lakes. AWS Lake Formation provides its own permissions
model that augments the IAM permissions model. This centrally defined
permissions model enables fine-grained access to data stored in data lakes
through a simple grant or revoke mechanism, much like a relational database
management system (RDBMS). AWS Lake Formation permissions are enforced using
granular controls at the column, row, and cell-levels across AWS services,
including Amazon Athena, Amazon EMR, and Amazon Redshift.


## Connector configuration modes

Following two modes are available for configuring the AWS Lake Formation
connector with Privacera.


### Push mode

In this mode, Privacera is the source of truth for access control policies.
The access control policies are defined in the Privacera and then these
policies will be pushed to AWS Lake Formation. From there, these policies will
be enforced for the AWS Lake Formation-supported services, such as Amazon
Redshift Spectrum, Amazon EMR, and Amazon Athena. 

![Push Mode Configuration for AWS Lake Formation Connector](../../images/1666724921b399.png)

As shown in the above image, with the Push mode, all the policies are
stored and managed by Privacera. For the databases that are in Amazon S3 and
managed by AWS Glue Catalog, Privacera will push the policies to AWS Lake
Formation using Lake Formation APIs. AWS Lake Formation will enforce these
policies natively. Privacera uses its connector architecture to enforce the
remaining data sources.

Since the same databases and tables defined in AWS Glue could be used by other third party tools–such as Databricks and
Trino–it the same policies can be optionally enforced by these tools also. Please note, in this case the capabilities
will be limited to the capabilities Privacera supports in Lake Formation.

### Pull mode

In this mode, the AWS Lake Formation is the source of truth for access
control. The access control policies are pulled from the Lake Formation at
specific time intervals. From Privacera, and then these policies get enforced
on various data sources defined by the configuration provided. 

![Pull Mode Configuration for AWS Lake Formation Connector](../../images/1666724923f1ee.png)


As shown in the above image, with the Pull mode, AWS Lake Formation is the
primary store for the dataset in S3 that is managed by Glue Catalog. Since AWS
Lake Formation is the primary store, administrators will manage these policies
directly in the AWS Lake Formation console or through its APIs. Since the same
databases and tables defined in AWS Glue could be used by other third party
tools–such as Databricks and Trino–it is paramount that the same policies are
consistently enforced by these tools also.

Privacera has native integrations with most of the other tools that use AWS
Glue and it can assist in enforcing these policies. This is implemented by
pulling the policies and tags from AWS Lake Formation and pushing them to
Privacera. Once the policies and tags are in Privacera, then Privacera will
enforce them in Databricks and/or Trino by applying the same original policies
defined in AWS Lake Formation.

## Comparison of Pull and Push Mode

To help you choose the correct mode for using the Privacera connector for Lake Formation, the table below outlines the
key differences between the Pull and Push modes:

| Feature                    | Pull Mode                                                                      | Push Mode                                                                                            |
|----------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Data Flow Direction**    | Pulls data from Lake Formation into Privacera                                  | Pushes data from Privacera to Lake Formation                                                         |
| **Data Access Management** | Privacera periodically fetches access control lists (ACLs) from Lake Formation | Privacera directly updates ACLs in Lake Formation                                                    |
| **Real-time Updates**      | Not real-time; depends on the polling interval                                 | Real-time updates as changes are pushed instantly                                                    |
| **Latency**                | Higher latency due to periodic polling                                         | Lower latency with immediate policy enforcement                                                      |
| **Use Case Suitability** | Use this if you are already using Lake Formation and want to replicate the policies to other data sources that use the same Glue catalogs, like Databricks and Trino | Use this if you want to manage the policies for all data sources from one central point in Privacera |

## Recommendation

We recommend using the Push mode for the Privacera connector for Lake Formation. Here are the key reasons for this
recommendation:

1. **Real-Time Policy Enforcement:** Push mode enables immediate updates to access control lists (ACLs) in Lake
   Formation, ensuring that any changes to data governance policies are applied instantly across all integrated data
   sources. This reduces the risk of unauthorized access and enhances data security.

2. **Centralized Management:** With Push mode, you can manage policies for all data sources from a single, central
   point. This simplifies the administration of data governance policies and ensures consistency across your entire data
   ecosystem.

4. **Better Control Over Policies:** Push mode allows for more granular control and immediate enforcement of policies in
   Lake Formation. This ensures that data governance rules are consistently applied without delays, enhancing overall
   compliance and security.


While Pull mode can be useful for specific scenarios, such as when replicating policies to other data sources using the
same Glue catalogs, Push mode offers significant advantages in terms of real-time updates, centralized management, and
overall control and security. Therefore, for most use cases, Push mode is the preferred choice to ensure robust and
efficient data governance with the Privacera connector for Lake Formation.

## Transitioning from Pull Mode to Push Mode

For those who want to start with Pull mode and later transition to Push mode, the process is straightforward and can be
managed effectively with the following steps:

1. **Initial Setup in Pull Mode:**
    - Begin by setting up the Privacera connector in Pull mode to integrate with Lake Formation.
    - Configure the connector to periodically fetch access control lists (ACLs) from Lake Formation.
    - Define and implement your data governance policies, ensuring they are replicated to other data sources that use
      the same Glue catalogs, like Databricks and Trino.

2. **Monitor and Evaluate:**
    - Regularly monitor the performance and effectiveness of the Pull mode setup.
    - Gather feedback from stakeholders on the current setup's effectiveness and areas for improvement.

3. **Prepare for Transition to Push Mode:**
    - Plan the transition by outlining the necessary changes and ensuring all stakeholders are informed.
    - Review the prerequisites for Push mode
    - Update your data governance policies to ensure they are ready for real-time enforcement.

4. **Transition to Push Mode:**
    - Reconfigure the Privacera connector to operate in Push mode. This involves setting up direct updates of ACLs from
      Privacera to Lake Formation.
    - Ensure that the connector is correctly pushing policy changes in real-time and that all configurations align with
      your initial setup.
    - Test the new configuration to verify that policy updates are being applied instantly and consistently across all
      integrated data sources.

5. **Post-Transition Monitoring:**
    - Continuously monitor the performance of the Push mode setup.
    - Address any issues or challenges that arise during the transition to ensure a smooth operation.

Once you're ready to leverage the benefits of real-time updates and centralized management, transitioning
to Push mode will enhance your data governance capabilities and ensure more robust security and compliance across your
data ecosystem.

<div class="grid cards" markdown>
-   :material-page-next: [Push Mode](aws-lake-formation-push-mode/index.md)
</div>
<div class="grid cards" markdown>
-   :material-page-next: [Pul Mode](aws-lake-formation-pull-mode/index.md)
</div>
