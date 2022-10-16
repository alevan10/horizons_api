#!/usr/bin/env bash
url="http://levan.home:5000/v2/horizons-api/manifests"
regex="Etag: \"([^\"]*)"
response=$(curl --slient --head -H "Accept: application/vnd.docker.distribution.manifest.v2+json" "$url"/"$1")
if [[ $response =~ $regex ]]; then
  echo "${BASH_REMATCH[1]}"
  curl --slient -X "DELETE" "$url"/"${BASH_REMATCH[1]}"
  echo "Image horizons-api:${BASH_REMATCH[1]} has been deleted"
else
  echo "No match found"
fi
