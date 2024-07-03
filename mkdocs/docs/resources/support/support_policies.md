---
title: Support Policies
---

# Privacera Support Policy



## PrivaceraCloud

Privacera will provide full support of Data Plane components installed in Customer's environment for at least 3 minor
releases of the product (8.1, 8.2, and 8.3). Customers are encouraged to continuously upgrade Data Plane components to
take advantage of new functionality and security vulnerability fixes available in the latest releases.

## PrivaceraCloud with All Components Hosted by Privacera

Privacera will upgrade all components of the system on a regular cadence. Notice will be given at least 7 days prior to
scheduled updates through status.privacera.com. Customers are encouraged to sign-up for notifications through the
Privacera status page.

## Privacera Self Managed (previously known as Privacera Platform)

**Version naming conventions and definitions:**

- **x - Major release**: Includes major new features and may contain backward incompatible functionality changes.
  Example: Privacera Self Managed 8
- **x.y - Minor release**: Includes some new features but maintains forward and backward compatibility within a given
  major release. Example: Privacera Self Managed 8.7
- **x.y.z - Maintenance release**: Includes improvements and bug fixes, maintaining forward and backward compatibility
  within a given minor release. Example: Privacera Self Managed 8.7.1

## General Release Guidelines

- Each major version is supported for 24 months following its first release. After that time, all minor and maintenance releases with the same major version number are not supported.
- For upgrades of Privacera Self Managed, Privacera will only support customers moving from:
    - One major release version to the immediately subsequent major release version. Example: From Release 5.3 to Release 6.0.0.1, but not from Release 4.3 to Release 6.0.0.1.
    - One minor release version to the two immediately subsequent minor release versions. Example: From Release 5.3 to Release 5.4 or Release 5.5, but not from Release 5.2 to Release 5.5.
    - One maintenance release version to another maintenance release version within the same minor release version. Example: From Release 5.3.1 to Release 5.3.5, but not from Release 5.3.1 to Release 5.4.1.
- Privacera strongly recommends that customers immediately upgrade to the latest release version for their given supported major version, as soon as it becomes available, to take advantage of these improvements.
- If Privacera cannot reproduce a customer-identified issue - including a security vulnerability - in the latest minor or maintenance release (whichever is more recent), the customer must update to this release as the remedy for their issue.

## Feature-Specific Guidelines

### Preview

- Privacera has implemented the necessary code but has not necessarily conducted quality assurance certification in any
  deployment configuration or against any third-party software.
- Privacera will process support requests related to this functionality but does not guarantee resolution within any
  specific timeline, unless otherwise contractually agreed.
- Privacera will not necessarily make this functionality available to all customers.
- Privacera can move this feature to Not Supported status at any time, without notice.

### Generally Available (GA)

- Privacera has implemented the necessary code and conducted quality assurance certification of the feature in question
  for at least one deployment configuration and the indicated version of third-party software (where applicable). All
  supported functionality is specified in the relevant documentation. The feature may have a list of specific, known
  limitations, which are noted in the documentation.
- Unless otherwise specified, Privacera will support the use of subsequent versions of third-party software (where
  applicable) to fix functionality and security bugs related to or caused by said software, including by making changes
  to Privacera code. As part of this provision, however, Privacera will only support the smallest possible increment
  update of third-party software. For example, if the bug is present in version 1.2.3.4 of the 3rd party software but is
  resolved in 1.2.3.5 as well as 2.0.0.0, Privacera will only support the use of version 1.2.3.5 automatically.
  Privacera will consider recommendations to support higher incremented later versions, and accompanying features, of
  third-party software (for example, 2.0.0.0) as new feature requests.
- Privacera will provide at least 12 months notice (via release notes) prior to moving this feature to Preview or Not
  Supported status, unless another timeline is specified in the release notes. This notice period does not apply with
  respect to specific versions of third-party software. For example, Privacera will not necessarily provide 12 months
  notice that it is discontinuing support for version x.y.z of a given database in order to support a more recent
  version of the same software. Rather, it will provide 12 months notice if it plans to discontinue support for that
  database entirely; that is, not support any version. Finally, this 12 month notice period does not apply to Privacera
  ending support for versions or offerings of third-party software that are no longer supported by their vendor or
  maker. In this case Privacera might end support more quickly than 12 months. Privacera reserves the right to implement
  backward incompatible changes in any release or series of releases in order to resolve identified security issues of
  sufficient severity.

## Kubernetes Variant Guidelines

- Privacera will support - at one time - versions of cloud provider-supplied variants of Kubernetes (`Kubernetes variants`) per the following table. Within 6 months of the release of the latest version of a Kubernetes variant, Privacera will begin supporting that version, while dropping support for the oldest supported version at that time. When the cloud provider drops support for a version of a Kubernetes variant, meaning that it is no longer possible to create a new cluster/instance with this version (per the relevant cloud provider’s release page), Privacera will immediately drop support for this version at the same time.
    - **Amazon Web Services (AWS)**
    - **Elastic Kubernetes Service (EKS)**
    - **Microsoft Azure Kubernetes Service (AKS)**
    - **Google Kubernetes Engine (GKE)**

- If, for any reason, Privacera’s product architecture is not technically capable of being simultaneously compatible with two or more versions of a provider’s Kubernetes variants, Privacera will support the latest compatible version(s), but not any incompatible earlier versions.

- Privacera will not support the use of open-source Kubernetes in Privacera Platform deployments.

## Datasource-Specific Guidelines

(Privacera Access Manager Only)

### Databricks
- Privacera will support two Long Term Support (LTS) versions of Databricks Runtime at a time. Within 6 months of its release by Databricks (per its release page), Privacera will support the newest version. At the same time, the third-latest version of Databricks will become Not Supported.
- Privacera will consider supporting releases in between LTS versions at customer request, but makes no forward-looking commitment to do so.

### Snowflake
- Privacera will only support use of the latest version of Snowflake.

### AWS Elastic Map Reduce (EMR)
- Within each major version of EMR, Privacera will support the four latest releases at a time (For example, for the 6.x.x major version, Privacera will support 6.5.0, 6.4.0, 6.3.1, 6.2.0). Within the second-latest major version of EMR, Privacera will only support the latest release (For example, for the 5.x.x version, Privacera will support 5.34.0). Within 6 months of its release by AWS (per its release page), Privacera will support these newest versions. At the same time, the fifth- and second-oldest release, respectively for each major version, will become Not Supported.

### Open Source Trino with Starburst Enterprise
- Privacera will support Long Term Support (LTS) releases of Open Source Trino with Starburst Enterprise for up to 12 months after their GA date. Privacera will consider support for interim Short Term Support (STS releases), but makes no forward-looking commitment to do so, and such support ends as soon as an STS release is superseded by an LTS. Customers using STS releases are advised to upgrade as soon as a newer LTS becomes available.

### Open Source Trino
- Privacera will support releases of Open Source Trino that align with supported releases of Starburst Enterprise; for example, if Starburst Enterprise 370-e is supported, then Trino 370 is also supported.
- Privacera does not necessarily support the feature in every conceivable deployment model. Contact your sales or support representative for details. Any functionality that is not explicitly in "Standard Support" is "Not Supported."
- Privacera recommends the feature for use in production when deployed in accordance with the aforementioned guidance.

---

*Version: 1.5*

*Privacera reserves the right to modify this policy at any time, without further proactive notification.*

*Effective Date: September 1st, 2023*
