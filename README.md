# Documentation for Privacera

This folder and subfolders contain the documentation for Privacera. The documentation is written in Markdown
and is built using [MkDocs](https://www.mkdocs.org/).

## How to run the documentation locally

We have customized the materials-mkdocs with additional plugins and features. To run the documentation locally, make
sure to pull the image from our ECR.

> Note: For now we are using the same image used by the PAIG product. The steps to get the credentials are the same.
> Please connect with the PAIG team to get the credentials or follow this

1. Go to the [ECR Token Generation Jobs](https://gitlab.com/privacera/paig/ci/-/jobs)
2. Pick the latest job for **get_ecr_token** and click on the link.
3. Search for the string `$ echo "echo \"$password\" | docker login --username AWS --password-stdin 587946681758.dkr.ecr.us-east-1.amazonaws.com"`
4. Copy the line after that which start something like this `echo "eyJwY... | docker login --username AWS --password-stdin 587946681758.dkr.ecr.us-east-1.amazonaws.com`
5. Run the command in your terminal. This will login you to the ECR.
6. Then run this to pull the image `ocker pull 587946681758.dkr.ecr.us-east-1.amazonaws.com/paig/privacera-mkdocs-materials-custom:main-0.1.0-SNAPSHOT-latest`

> Note: The token is valid for limited time. If it expires, you will need to repeat the steps.

> Note: If the mkdocs docker image has been updated, then you need to pull the latest image from the ECR. Follow the same step
as above to get the credentials and do the docker pull

You will need to run the following command to run the docker and it will start the documentation on port 8002.

```bash
./run_local_docs_docker.sh
```
Then go to [http://localhost:8005](http://localhost:8005) to see the documentation.

There are few caveats to this setup:
1. The documentation will auto refresh when you make changes to the markdown files. However, you will need to stop the and start the docker container to see the changes.
   - When mkdocs.yml is updated 
   - When any files in the snippets folders are updated
   - When titles or meta data is updated in the markdown files


## User Guide for documentation


### Title for each documentation page
At the top of each documentation page, you need to add the title of the page. The title should be in the following format:
```markdown
---
title: Put your title here. E.g. Base Installation for PrivaceraCloud
---
```

Here are some optional parameters that you can add to the top of the documentation page:
```markdown
icon: material/home
hide:
- navigation
- toc
```

### How do I use collapsible sections?
```markdown
/// details | Log Message `Here goes the title`
    type: warning 

The valid types are ['note', 'attention', 'caution', 'danger', 'error', 'tip', 'hint', 'warning']

!!! warning
    The **type** should be exactly below the **details** tag. The **type** should be one of the valid types mentioned above.

///
```

### Footnotes
Refer to this document for how to use footnotes: [Footnotes](https://squidfunk.github.io/mkdocs-material/reference/footnotes/)
!!! note
    The footnotes are shown at the bottom of the page.

### 

### Supported and Not Supported icons
```markdown
:green_circle: - For Yes
:yellow_circle: - For Partial
:no_entry_sign: - For No
:material-circle-outline: - For Not Applicable
```


### How to exclude a page from search
```markdown
<!--
---
search:
exclude: true
---
-->
```