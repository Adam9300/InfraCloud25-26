#!/usr/bin/env bash

APIKEY="cisco|mp881n8AN-e7b_MpXssCvapVW8ct2s4fPi4W3HGFvXk"

for BOOK in {0..999}
do
  echo $BOOK
  DELETE_URL="http://library.demo.local/api/v1/books/$BOOK"
  echo $DELETE_URL
  curl -X DELETE $DELETE_URL \
    -H "accept: application/json" \
    -H "X-API-Key: $APIKEY" \
    -H "Content-Type: application/json"
done
