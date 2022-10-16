#!/usr/bin/env bash
url="http://levan.home:5000/v2/horizons-api/manifests"
regex="Etag: \"([^\"]*)"
response=$(curl --head -H "Accept: application/vnd.docker.distribution.manifest.v2+json" "$url"/"$1")
if [[ $response =~ $regex ]]; then
  echo "${BASH_REMATCH[1]}"
  curl -X "DELETE" "$url"/"${BASH_REMATCH[1]}"
else
  echo "No match found"
fi
