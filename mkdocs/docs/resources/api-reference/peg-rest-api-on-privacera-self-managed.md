---
title: PEG REST API on Privacera Self-Managed deployment
---

# PEG REST API on Privacera Self-Managed Deployment

For the Privacera Self-Managed deployment, by default, the PEG API endpoint is:


==https://<privacera_hostname>:6869/api/peg/public==

Please check with your installation team for the value of `<privacera_hostname>` and confirm if the default port has 
not been changed.

The PEG REST API consists of the following endpoints:

| Endpoint | Description |
| --- | --- |
| `/authenticate` | Generates a token to be used with subsequent `/protect` and `/unprotect` endpoints. |
| `/getSchemes` | Returns the names of Privacera-supplied and user-defined encryption schemes. |
| `/protect` | Encrypts the data. |
| `/unprotect` | Decrypts the data. |


## API Authentication Methods on Privacera Platform

There are two different ways to authenticate to the PEG REST API:

* Basic authentication with a username and password.
* Using Privacera authentication token.

### Basic Authentication

A Portal user needs to have the `ROLE_ENCRYPTION_ALL` or `ROLE_ENCRYPTION_READ` role to authenticate to the PEG REST API
via basic authentication. [TODO: Add link to the role management page]

For basic authentication, pass your username and password credentials in the `<username>:<password>` argument directly
on the `/protect` or `/unprotect` endpoint.

### PEG REST API Authentication Token

The PEG REST API authentication token can be created in two ways:

* In the Privacera Portal.
* Using the `/authenticate` REST API endpoint.

The token must be included in the HTTP header for subsequent endpoint calls.

#### Generate PEG REST API Authentication Token in the Privacera Portal

To generate a token in the Privacera Portal:

1. Log in to the Privacera Portal.
2. From the left navigation menu, select **Launch Pad** and click **Privacera Token**.
3. Click **+Generate Token** and generate a new token by entering the expiration details, etc.
4. An Access Key and a Secret Key, the components of the token, are generated as shown below:
5. Store the Access Key and Secret Key credentials safely.

The token is a combination of `<AccessKey>` and `<SecretKey>` delimited by a colon (:). `<AccessKey>:<SecretKey>`

This token is required in the header of the `/protect` or `/unprotect` endpoints in the following form:

`X-API-KEY:<AccessKey>:<SecretKey>`

#### Generate PEG REST API Authentication Token Using the /authenticate Endpoint

To generate the token using the `/authenticate` endpoint:

1. Use the `/authenticate` endpoint with basic authentication user credentials to authenticate the end-user. PEG is
   integrated with the Privacera Portal.

    ```sh
    curl -u <service_user>:<password> \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --data-raw '{"user":"<application_user>"}' \
        https://<privacera_hostname>:6869/api/peg/public/authenticate
    ```

2. If the authentication is successful, PEG returns the colon-delimited token `<AccessKey>:<SecretKey>`.
3. Subsequent calls to the `/protect` and `/unprotect` endpoints must include the `X-API-KEY` header with the token:
    `X-API-KEY:<token_from_authenticate>`



## Self Signed Certificate

If you are testing with a self-signed certificate, to bypass the certificate
validation check, add the `curl -k` option.

## User Impersonation

If you have been granted privileged user status by the account administrator, you can make REST API calls on behalf of other users. This process is known as "user impersonation."

In this scenario, you use your own username and password on the `/protect` or `/unprotect` endpoint and include the username of the other user as the value of the `user:` field. The password of the other user is not required.

In the following example, the privileged user `<privileged_user>` includes their own password and specifies `user:<username_being_impersonated>` to `/protect` on behalf of that user:

```sh
curl -k -u <privileged_user>:<privileged_user_password> -H "Accept: application/json" \
-d '{"schemelist":["TEST_EMAIL_NEW_30_6"], \
"datalist":[["sally@gmail.com"]], \
"user":"<username_being_impersonated>"}' \ 
-H 'Content-Type: application/json' <peg_server_URL_or_API_endpoint>/api/peg/public/protect
```

Data services, such as Databricks or Trino, can also utilize the privileged user as the service user, allowing the data
service to run `/protect` and `/unprotect` on behalf of other users of the data service.

## /protect API Endpoint on Privacera Platform

This example of the `/protect` endpoint illustrates some common fields of the PEG REST API on the Privacera Platform.

Instead of basic authentication, this example uses token authentication with an `X-API-KEY:<token_from_authenticate>`. If you prefer basic authentication, remove the token line and replace it with `-u <service_user>:<password>`.

```sh
curl \
--request 'POST' 'https://<privacera_hostname>:6869/api/peg/public/protect' \
--header "X-API-KEY:<token_from_authenticate>" \
--header "Accept: application/json" \
--header 'Content-Type: application/json' \
--data-raw '{
    "schemelist":["<encryption_scheme>,..."], 
    "datalist":[["<data_to_encrypt>",...]], 
    "maskSchemelist": ["<masking_scheme>",...], 
    "maskDatalist": [[data_to_mask,...]], 
    "user":"<application_user>"
}'
```

| Line | Description |
| --- | --- |
| `schemelist` | List of `<encryption_schemes>`. |
| `datalist` | List of data elements, one for each scheme in the `schemelist` parameter. |
| `<data>` | A data element to be encrypted with `/protect` or decrypted with `/unprotect`. |
| `maskSchemeList` | List of `<masking_schemes>`. |
| `<masking_scheme>` | One or more `<masking_schemes>` to mask the data in `maskDataList`. |
| `maskDataList` | List of data elements for masking, with at least one for each masking scheme in the `maskSchemeList` parameter or more data elements to be masked. |

## Example PEG API Endpoints

Most of the examples do not show the full `curl` command and the required authentication. They only show the JSON bodies
of the requests and responses.

### /authenticate

This example uses basic authentication to retrieve a token required for other examples.

```sh
curl \
-u <service_user>:<password> \
--header "Accept: application/json" \
--header "Content-Type: application/json" \
--data-raw '{"user":"<application_user>"}' \
https://your_peg_host:6869/api/peg/public/authenticate 
```

**Response**

```json
{
    "token": "bWtpc2VyOjE6MTYxNzIyMTk4Njg2Mjo4NjM5OTEzOA==:U3AcayrrQW3eecXjocH8ArJNqDr1GmJAM92Fa/f8T/YxJitKuCqw/CIB7Lm9Szqk",
    "tokenid": 1,
    "tokenExpiry": "2021-04-01T12:19:30Z",
    "tokenName": "service_user",
    "tokenStatus": "ENABLED",
    "userName": "application_user"
}
```

### /getSchemes

Returns the names of Privacera-supplied and user-defined encryption schemes.

```sh
curl -i https://your_peg_host:6869/api/peg/public/getschemes \
--header "X-API-KEY: <token>" \
--header "Accept: application/json" \
--header "Content-Type: application/json" \
-d '{"user": "<username>"}'
```

**Response**

```json
{
    "schemes": [
        "SYSTEM_PERSON_NAME", 
        "SYSTEM_SSN", 
        "SYSTEM_EMAIL", 
        "SYSTEM_ADDRESS", 
        "SYSTEM_CREDITCARD", 
        "SYSTEM_US_PHONE_FORMATTED", 
        "SYSTEM_ACCOUNT"
    ]
}
```

### /protect with Encryption Scheme

The two elements in the input `datalist` array are encrypted with the encryption schemes `PERSON_NAME` and `EMAIL`.

```sh
curl --data-raw '{
    "schemelist": ["PERSON_NAME", "EMAIL"],
    "datalist": [
        ["Mark", "Jonathan", "Christopher"],
        ["mark@example.com", "jonathan@test.com", "christopher@google.com"]
    ],
    "user": "jimmybob@BigCo.com"
}'
```

**Response**

```json
{
    "datalist": [
        ["WjM5", "5vpJF9zT", "1EbplEYVBjy"],
        ["i0bD@WKbMYpr.CvE", "?9aqS8zV@YUym.hkd", "d501shhJEO&@YpvfOc.VYH"]
    ],
    "data": "",
    "responseStatus": "SUCCESS"
}
```

### /protect with Masking Scheme

The element in the input `maskDataList` array is masked by the masking scheme `MASKING_SCHEME`.

```sh
curl --data-raw '{
    "maskSchemelist": ["MASKING_SCHEME"],
    "maskDatalist": [
        ["", null, "12-12-2012", "12/12/2025T09:01:02"]
    ],
    "user": "<application_user>"
}'
```

**Response**

```json
{
    "datalist": [],
    "data": "",
    "maskDatalist": [
        ["**-**-****", "**/**/*******:**:**"],
        ["*****@*****.***", "", null]
    ],
    "responseStatus": "SUCCESS"
}
```

### /protect with Both Encryption and Masking

The element in the input `datalist` array is encrypted with the encryption scheme `SYSTEM_EMAIL` and at the same time the data in the input `maskDataList` is masked with the masking scheme `MASKING_SCHEME`.

```sh
curl --data-raw '{
    "schemelist": ["SYSTEM_EMAIL"],
    "datalist": [["sally@gmail.com"]],
    "maskSchemelist": ["DATE_MASKING_SCHEME"],
    "maskDatalist": [
        ["", null, "12-12-2012", "12/12/2025T09:01:02"]
    ],
    "user": "padmin"
}'
```

**Response**

```json
{
    "datalist": [
        ["*btaV@CyilS.Jvk"]
    ],
    "data": "",
    "maskDatalist": [
        ["", null, "**-**-****", "**/**/*******:**:**"]
    ],
    "responseStatus": "SUCCESS"
}
```

### /unprotect without Presentation Scheme

The two elements in the input `datalist` array are decrypted with the encryption schemes `PERSON_NAME` and `EMAIL`.

```sh
curl --data-raw '{
    "schemelist": ["PERSON_NAME", "EMAIL"],
    "datalist": [["WjM5", "5vpJF9zT", "1EbplEYVBjy"], ["i0bD@WKbMYpr.CvE", "?9aqS8zV@YUym.hkd", "d501shhJEO&@YpvfOc.VYH"]],
    "user": "<application_user>"
}'
```

**Response**

```json
{
    "datalist": [
        ["Mark", "Jonathan", "Christopher"],
        ["mark@example.com", "jonathan@test.com", "christopher@google.com"]
    ],
    "data": "",
    "responseStatus": "SUCCESS"
}
```

### /unprotect with Presentation Scheme

The input in the `datalist` array is decrypted with the encryption scheme `EMAIL2` and then obfuscated with the presentation scheme `EMAIL2_P`.

```sh
curl --data-raw '{
    "datalist": [["8283a@QhbpH.yOs", "5fGP@RyZBO.UZE"]],
    "schemelist": ["EMAIL2"],
    "presentationSchemelist": ["EMAIL2_P"],
    "user": "jimmybob@BigCo.com"
}'
```

## /unprotect with Masking Scheme

Masking schemes must not be used with `/unprotect`, which returns an error because the masked data cannot be unmasked.

## REST API Response Partial Success on Bulk Operations

For bulk operations, where multiple data elements are included in the `datalist` JSON array of the `/protect` or `/unprotect` request, if an error is encountered in processing one of those elements, the endpoint returns the response as "Partial Success" but does not fail the entire batch.

## Audit Details for PEG REST API Accesses

Privacera records access to the PEG REST API encryption keys and schemes.
