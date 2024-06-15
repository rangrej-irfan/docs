# Documentation for Privacera

This folder and subfolders contain the documentation for Privacera. The documentation is written in Markdown
and is built using [MkDocs](https://www.mkdocs.org/).

## How to run the documentation locally

We have customized the materials-mkdocs with additional plugins and features. To run the documentation locally, make
sure to pull the image from our ECR.

> Note: For now we are using the same image used by the PAIG product. The steps to get the credentials are the same.
> Please connect with the PAIG team to get the credentials.

You will need to run the following command to run the docker and it will start the documentation on port 8002.

```bash
./run_local_docs_docker.sh
```

You can access the documentation at http://localhost:8005
