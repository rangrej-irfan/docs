---
title: PEG REST API on PrivaceraCloud
---

# PEG REST API on PrivaceraCloud

The PEG API endpoint can be obtained using the **Copy Url** link in **Settings > Api Key**.

In the examples here, this endpoint is referred to as `<cloud_peg_api_endpoint>`.

The PEG REST API includes the following endpoints:

* `/protect`: Encrypts the data.
* `/unprotect`: Decrypts the data.

## REST API Prerequisites

| Prerequisite   | Description |
|----------------| --- |
| API Key        | For the `/protect` and `/unprotect` REST API requests, you need an API key. |
| Scheme Policy  | For the `/protect` and `/unprotect` REST API endpoints, you must create a scheme policy that grants these permissions to the user. |

## PEG API Endpoint on PrivaceraCloud

This example of the `/protect` endpoint illustrates some common fields of the PEG REST API on PrivaceraCloud. The example is split across separate lines for clarity but in actual use is a single line.

```sh
curl -il \
--request POST https://<cloud_peg_api_endpoint>/api/<api-key>/api/peg/public/protect \
-u <service_user>:<password> \
--header "Accept: application/json" \
--header "Content-Type: application/json" \
--data-raw '{
    "schemelist": ["<encryption_scheme>",...], 
    "datalist": [["<data_to_encrypt>",...]], 
    "maskSchemelist": ["<masking_scheme>",...], 
    "maskDatalist": [[<data_to_mask>,...]], 
    "user": "<application_user>"
}'
```

| Line | Description |
| --- | --- |
| `<cloud_peg_api_endpoint>` | Your API endpoint as described in PEG REST API on PrivaceraCloud |
| `<api_key>` | Your API key, as described in API Key on PrivaceraCloud |
| `schemelist` | List of `<encryption_schemes>`. |
| `datalist` | List of data elements, one for each scheme in the `schemelist` parameter. |
| `<data>` | A data element to be encrypted with `/protect` or decrypted with `/unprotect`. |
| `maskSchemeList` | List of data elements for masking, with at least one for each masking scheme in the `maskSchemeList` parameter or more data elements to be masked. |
| `<masking_scheme>` | One or more `<masking_schemes>` to mask the data in `maskDataList`. |
| `maskDataList` | List of data elements for masking, with at least one for each masking scheme in `maskSchemeList` parameter or more data elements to be masked. |
| `<application_user>` | The application user or end-user that connects to a service, such as Snowflake, UDF, or ODBC application. Scheme policies verify the permission to use Privacera Encryption for this user. |
| `presentationSchemeList` | Not shown here, the `/unprotect` request can include a field to specify an optional presentation scheme. On `/unprotect`, the server uses the `presentation_scheme` to obfuscate the data even more for display to authorized users. `presentationSchemeList` on `/protect` is ignored. |


## Example PEG REST API Endpoints for PrivaceraCloud

These examples do not show the full `curl` command, authentication, or the PrivaceraCloud PEG API endpoint. Only the JSON bodies for the requests (with the curl `--data-raw` option) and responses are shown.

If you are testing with a self-signed certificate, to bypass the certificate validation check, add the `curl -k` option.

### /protect with Encryption Scheme

The two elements in the input `datalist` array are encrypted with the encryption schemes `PERSON_NAME` and `EMAIL`.

```bash
--data-raw '{
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

This example uses the authentication token retrieved with `/authenticate`.

```sh
--data-raw '{
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
    "maskDatalist": [
        ["", null, "**-**-****", "**/**/*******:**:**"]
    ]
}
```

### /protect with Both Encryption and Masking

The element in the input `datalist` array is encrypted with the encryption scheme `SYSTEM_EMAIL` and at the same time
the data in the input `maskDataList` is masked with the masking scheme `MASKING_SCHEME`.

```bash
--data-raw '{
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
        ["mNM-^@RUWqb.qRK"]
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

```bash
--data-raw '{
    "schemelist": ["PERSON_NAME", "EMAIL"], 
    "datalist": [
        ["WjM5", "5vpJF9zT", "1EbplEYVBjy"],
        ["i0bD@WKbMYpr.CvE", "?9aqS8zV@YUym.hkd", "d501shhJEO&@Y

pvfOc.VYH"]
    ], 
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

The input in the `datalist` array is decrypted with the encryption scheme `EMAIL2` and then obfuscated with the
presentation scheme `EMAIL2_P`.

This example uses the authentication token retrieved with `/authenticate`.

```sh
--data-raw '{
    "datalist": [["8283a@QhbpH.yOs", "5fGP@RyZBO.UZE"]],
    "schemelist": ["EMAIL2"], 
    "presentationSchemelist": ["EMAIL2_P"],
    "user": "jimmybob@BigCo.com"
}'
```

### /unprotect with Masking Scheme

Masking schemes must not be used with `/unprotect`, which returns an error because the masked data cannot be unmasked.

## Audit Details for PEG REST API Accesses

PrivaceraCloud records access to the PEG REST API encryption keys and schemes.
