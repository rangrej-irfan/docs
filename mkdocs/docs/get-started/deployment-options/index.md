---
title: Deployment Options for Privacera
---

## Deployment Options

Privacera offers two deployment options to suit different organizational needs and preferences: PrivaceraCloud and
Self-Managed.

### 1. PrivaceraCloud

PrivaceraCloud is the Software-as-a-Service (SaaS) deployment option, providing a fully managed solution hosted by
Privacera. This option simplifies deployment and management by offloading infrastructure and operational
responsibilities to Privacera.

**Key Features:**

- **Managed Service:** Privacera handles all infrastructure, maintenance, and updates, ensuring high availability and
  reliability.
- **Flexible Integration:** Organizations can choose to deploy connectors and the Discovery module within their own
  Virtual Private Cloud (VPC), allowing sensitive data to remain within their control while leveraging Privacera’s
  managed services.
- **Compliance and Security:** Benefit from Privacera's robust security practices and compliance certifications,
  ensuring your data governance needs are met with the highest standards.

### 2. Self-Managed

The Self-Managed deployment option allows organizations to run the entire Privacera platform within their own Virtual
Private Cloud (VPC). This approach provides complete control over the deployment, configuration, and management of
Privacera, offering maximum flexibility and customization.

**Key Features:**

- **Full Control:** Organizations maintain full control over their infrastructure, data, and governance policies,
  allowing for customized configurations and optimizations.
- **Cloud:** Deploy Privacera within any cloud provider's VPC, aligning with your existing infrastructure and IT strategies.
- **Data Security:** All components, including control plane, connectors and the Discovery module, operate within the organization's
  VPC, ensuring sensitive data never leaves their controlled environment.
- **Customization:** Tailor the deployment to meet specific security, compliance, and operational requirements unique to
  your organization.

By offering both PrivaceraCloud and Self-Managed deployment options, Privacera provides the flexibility to choose the
best approach for your organization's data governance and security needs, whether you prefer a fully managed service or
complete control over your deployment.

## Deployment Options Comparison

To help you choose the correct deployment option for your organization, the table below outlines the key differences between PrivaceraCloud and Self-Managed deployments:

| Feature | PrivaceraCloud (SaaS) | Self-Managed |
| --- | --- | --- |
| **Deployment Location** | Hosted by Privacera | Customer's VPC |
| **Management Responsibility** | Managed by Privacera | Managed by Customer |
| **Scalability** | Easily scalable; managed by Privacera | Customer-managed scaling |
| **Infrastructure Maintenance** | Handled by Privacera | Customer responsibility |
| **Connector Deployment** | Option to deploy in customer's VPC | Deployed in customer's VPC |
| **Discovery Module Deployment** | Deployed in customer's VPC | Deployed in customer's VPC |
| **Control Over Environment** | Limited to configuration and policies | Full control over infrastructure and environment |
| **Compliance and Security** | Managed compliance and security standards by Privacera | Customer-managed compliance and security |
| **Updates and Patches** | Automatically managed by Privacera | Customer responsible for updates and patches |
| **Operational Overhead** | Minimal for the customer | Higher, as managed by the customer |
| **Data Residency** | Data can remain in customer's VPC with connectors and Discovery module | All data and components reside in customer's VPC |

By considering these differences, you can select the deployment option that best aligns with your organization's operational preferences, control requirements, and resource capabilities.