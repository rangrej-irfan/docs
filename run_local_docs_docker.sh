#!/bin/bash
set -e
set -x
PORT_MAPPING="-p 8005:8005"
DOCKER_ENV=
if [ "$1" == "build" ]; then
  DOCKER_ENV="$DOCKER_ENV -e CI=true"
  PORT_MAPPING=""
elif [ "$1" == "" ]; then
  #https://www.mkdocs.org/user-guide/cli/#mkdocs-serve
  params="serve --dev-addr=0.0.0.0:8005 --dirty"
fi

docs_folder="$(pwd)/mkdocs"
MKDOCS_IMAGE=587946681758.dkr.ecr.us-east-1.amazonaws.com/paig/privacera-mkdocs-materials-custom:main-0.1.0-SNAPSHOT-latest
#MKDOCS_IMAGE=privacera-mkdocs-materials-custom

docker run --rm -v "${docs_folder}:/docs" $DOCKER_ENV $PORT_MAPPING $MKDOCS_IMAGE $params $*
