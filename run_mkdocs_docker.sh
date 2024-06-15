#!/bin/bash
set -e
set -x

MKDOCS_IMAGE=587946681758.dkr.ecr.us-east-1.amazonaws.com/paig/privacera-mkdocs-materials-custom:main-0.1.0-SNAPSHOT-latest

docker run --rm -v "$(pwd)/mkdocs:/docs" $MKDOCS_IMAGE $*
