# Eigen microservice-experiment
## Beschrijving
Kleine Flask microservice voor signup/login met salted password hashing + een Jenkins pipeline die Docker build/run/test automatiseert.

## Doel
- Via curl een nieuwe user aanmaken + inloggen met deze user
- Docker container aanmaken en testen
- Users in db terugvinden met gehashte wachtwoord

## Features
- `POST /signup` : maakt user aan, bewaart salt + SHA-256(salt+password) in SQLite
- `POST /login`  : controleert credentials
- `GET /health`  : simpele healthcheck voor CI


