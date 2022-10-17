#!/bin/bash
url="http://levan.home:5000/v2/horizons-api/manifests"
regex="Etag: \"([^\"]*)"
response=$(curl --silent --head -H "Accept: application/vnd.docker.distribution.manifest.v2+json" "$url"/"$1")
if [[ $response =~ $regex ]]; then
  curl --silent -X "DELETE" "$url"/"${BASH_REMATCH[1]}"
  echo "Image horizons-api:${BASH_REMATCH[1]} has been deleted"
else
  echo "No match found for horizons-api:$1"
fi
