#!/bin/sh

if [ ! -d docker/build/ ]; then
    mkdir docker/build/
fi

docker/zip_source.sh
docker build -t pharmacy-api docker/
