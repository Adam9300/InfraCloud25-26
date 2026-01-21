#!/bin/bash

echo "=== FORM POST request ==="

curl -X POST https://httpbin.org/post \
-F "name=Student" \
-F "course=DevNet" \
-F "level=Beginner"
