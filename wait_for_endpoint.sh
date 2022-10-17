#!/bin/bash
url=${HORIZONS_API_URL:="http://levan.home/api/v0"}
count=0
response=$(curl --silent $url/health)
while [ "$response" != "\"pong\"" ]
do
  if [ $count -gt 20 ]; then
    echo "Endpoint unavailable"
    exit 2
  fi
  response=$(curl --silent $url/health)
  ((count+=1))
  echo "Attempt $count. Retrying..."
  sleep 5
done
echo "Endpoint is ready"
