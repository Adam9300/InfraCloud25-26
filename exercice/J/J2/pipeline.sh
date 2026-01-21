#!/bin/bash

echo "=== J2 PIPELINE START ==="

echo "[1] Python script uitvoeren"
python3 scripts/app.py > output/result.txt

echo "[2] Resultaat tonen"
cat output/result.txt

echo "=== J2 PIPELINE EINDE ==="
