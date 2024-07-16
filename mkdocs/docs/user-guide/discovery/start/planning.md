---
title: Planning Your Privacera Discovery Setup
---

# Planning Your Privacera Discovery Setup

This guide provides a general approach to setting up Privacera Discovery to help you effectively manage and protect your sensitive data.

1. **Inventory Data Assets**
	- Take an inventory of the data assets you want to monitor, including databases, tables, and applications such as Snowflake or Databricks. Identify the data owners of these assets.

2. **Connect Data Sources**
	- Enable and connect your data sources for scanning in Privacera Discovery. Refer to the [Connecting Data Sources](../sources/index.md) guide for detailed instructions.

3. **Define Data Zones (Optional)**
	- Optionally, create data zones for your data sources to delegate administration to your organizational groups. See the [Data Zones Overview](../zones/overview.md) for more information.

4. **Define Scans**
	- Set up scans to classify your data sources, including resource scoring, scanning schedules, and specifying which data sources to include or exclude. Detailed setup instructions can be found in the [Scan Setup](../scanning/setup/defining-scans.md) guide.
	- Classification techniques:
		- [Dictionaries](../scanning/classification/dictionaries.md)
		- [Heuristics Models](../scanning/classification/models.md)
		- [Rules](../scanning/classification/rules.md)

5. **Refine Scans**
	- Based on the system's classifying tags, refine the scans using the following techniques:
		- [Dictionaries](../review/refining/dictionaries.md)
		- [Models](../review/refining/models.md)
		- [Rules](../review/refining/rules.md)
		- [Accepting or Rejecting Classifications from Scans](../review/reviewing.md)

6. **Implement Compliance Workflow**
	- Establish organizational mechanisms to implement a compliance workflow, including:
		- [Monitoring Alerts](../policies/compliance/alerts.md)
		- [Checking for Movement of Data Across Data Zones](../zones/movement.md)

7. **Enhance Security**
	- Enhance security by masking or encrypting database tables, columns, rows, or other fields. For more information, see the [Get Started with Encryption](**TODO**) guide.

Following these steps will help you set up and optimize Privacera Discovery to effectively manage your sensitive data. For more detailed instructions and additional support, refer to the linked guides.

<div class="grid cards" markdown>
- 	:material-page-previous: Previous topic: [Getting Started](index.md)
-   :material-page-next: Next topic: [Quick Start](quick-start.md)
</div>