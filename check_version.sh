#!/usr/bin/env bash
tag_list=$(curl levan.home:5000/v2/horizons-api/tags/list)
if [[ ${tag_list} == *"$(poetry version -s)"* ]]; then
    echo "Bumping Horizons API version"
    poetry version patch
    exit 1
else
    echo "Horizons API version ok"
fi
