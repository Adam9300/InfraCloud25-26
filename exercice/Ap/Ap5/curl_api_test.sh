#!/bin/bash

echo "=== GET request ==="
curl https://jsonplaceholder.typicode.com/posts/1

echo ""
echo "=== POST request ==="
curl -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title":"Test","body":"Hello","userId":1}'

echo ""
echo "=== DELETE request ==="
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
