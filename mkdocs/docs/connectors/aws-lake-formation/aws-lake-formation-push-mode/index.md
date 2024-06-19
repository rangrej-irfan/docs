# AWS Lake Formation - Push Mode

!!! info "Connector configuration modes"
    This document describes the configuration modes for the AWS Lake Formation connector with Privacera using the 
    Push mode. For more information on the Pull mode, refer to 
    [AWS Lake Formation - Pull mode](../index.md#pull-mode). For differences between the Push and 
    Pull modes, [refer to](../index.md).


## Introduction

In this mode, Privacera is the source of truth for access control policies. For more information on the Push mode, refer 
to [Push mode](../index.md#push-mode).

## Access Management Features

### Supported Access Management Features

{{ read_csv('snippets/access_overview.csv') }}

{{ read_csv('snippets/supported_access_features.csv') }}

### User Identity Mapping

Lake Formation supported services like AWS Athena and AWS Redshift Spectrum use AWS IAM and SAML users for access 
control. The Roles in Privacera are mapped to the IAM roles in AWS. Any permissions granted to the roles in Privacera 
are pushed to Lake Formation for corresponding IAM roles. For SAML users and groups, the permissions for Users and
Groups in Privacera are pushed to Lake Formation with the SAML ARN prefix (TODO: Give examples here)

### Limitations for Access Management Features

1. Lake Formation doesn't support external UDF, so column masking and encryption from Privacera are not available.
2. Privacera doesn't support Cell Level Filtering for Lake Formation.

## Discovery Features

Discover features are not supported in Lake Formation connectors


## Data Encryption Features

Data encryption features are not supported in Lake Formation connectors

