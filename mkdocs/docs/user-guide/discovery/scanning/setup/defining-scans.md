# Processing order of scan techniques

Privacera Discovery applies [tags](../classification/tags.md "Tags") to dataset attributes
using defined [rules](../classification/rules.md "Rules") . This is done by comparing data
against [dictionaries](../classification/dictionaries.md "Dictionaries") and
[models](../classification/models.md "Models"). The application of tags depends on the order
of relevant rules. After a rule is triggered, the rest of the relevant rules
are not processed.

After creating rules, you can reorder them into the necessary sequence to
ensure that your data is tagged appropriately. See [Reorder Structured
Rules](create-a-structured-rule.html#reorder-structured-rules "Reorder
structured rules") for more information.

# Start a scan

There are several ways to start scans in Privacera Discovery:

* From the **Data Sources** page, which is described here.

* For offline (re-scan) or realtime (continuous) scans. See [Offline and Realtime Scans](../ways/index.md "Offline and Realtime Scans").

* If you have set up datazones, starting a scan, called **reevaluation** , is discussed in [Data zones overview](../../zones/overview.md "Data zones overview").

To start a scan from the **Data Source** page, follow these steps:

1. From the **Applications** section, select the application that contains the resource you want to scan.

2. In the **Scanning Details** section, locate the resource you want to scan.

3. Click **SCAN RESOURCE**.

A message appears indicating that a scan has been initiated.

<div class="grid cards" markdown>
- 	:material-page-previous: Previous topic: [Starting Scan](../index.md)
-   :material-page-next: Next topic: [Offline and Realtime scans](../ways/index.md)
</div>