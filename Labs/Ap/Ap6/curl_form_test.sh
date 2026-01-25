#!/bin/bash

# 1. GET request – API bereikbaar?
# Dit commando stuurt een eenvoudige GET-request naar de API.
# Het wordt gebruikt om te controleren of de REST-API bereikbaar is.
echo "=== 1. GET request ==="
curl https://httpbin.org/get

echo ""

# 2. GET request met verbose output
# De optie -v (verbose) toont extra informatie zoals:
# - HTTP request headers
# - HTTP response headers
# - statusinformatie
# Dit is handig om de communicatie met de API te debuggen.
echo "=== 2. GET request met verbose output ==="
curl -v https://httpbin.org/get

echo ""

# 3. POST request met form-data (HTML-form simulatie)
# -X POST geeft aan dat er data wordt verstuurd.
# -F stuurt data als form-data (multipart/form-data),
# wat hetzelfde formaat is als een HTML-formulier.
# Hiermee simuleren we het verzenden van een webformulier via curl.
echo "=== 3. POST request met form-data ==="
curl -X POST https://httpbin.org/post \
-F "name=Student" \
-F "course=DevNet" \
-F "level=Beginner"

echo ""

# 4. POST request met JSON-data
# -H zet de Content-Type header op application/json.
# -d bevat de JSON-data die naar de API wordt gestuurd.
# Dit is de standaardmanier om data te versturen naar een REST-API.
echo "=== 4. POST request met JSON-data ==="
curl -X POST https://httpbin.org/post \
-H "Content-Type: application/json" \
-d '{"name":"Student","course":"DevNet","level":"Beginner"}'

echo ""

# 5. HTTP statuscode controleren
# -s zorgt voor stille modus (geen extra output).
# -o /dev/null negeert de response body.
# -w toont enkel de HTTP-statuscode.
# Dit wordt gebruikt om snel te controleren of de request succesvol was.
echo "=== 5. HTTP statuscode controleren ==="
curl -s -o /dev/null -w "Status code: %{http_code}\n" https://httpbin.org/get
