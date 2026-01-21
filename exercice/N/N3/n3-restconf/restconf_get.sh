#!/bin/bash

echo "=== RESTCONF GET interfaces ==="

curl -k -u cisco:cisco123! \
-H "Accept: application/yang-data+json" \
https://192.168.56.101/restconf/data/ietf-interfaces:interfaces