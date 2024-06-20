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