# Eigen image-experiment 2 (sql)

## Beschrijving
Webservice om afbeeldingen te uploaden, een simpele image-bewerking uit te voeren
(bv. grayscale), en metadata + resultaten op te slaan in een SQLite database.

Gebaseerd op de lab-aanpak: Flask webapp + templates/static + Docker build/run via bash script,
poort 8080 en host 0.0.0.0. 

## Features
- Upload image (jpg/png/webp)
- Image processing experiment (bv. grayscale)
- SQLite opslag:
  - upload info (timestamp, client IP)
  - experiment type
  - paden naar origineel en resultaat
- Gallery pagina met geschiedenis van uploads/experimenten

## Database schema (SQLite)
De app maakt de DB automatisch aan bij de eerste run.

Tabel `images`:
- id (INTEGER, PK)
- original_name (TEXT)
- stored_name (TEXT)
- result_name (TEXT)
- experiment (TEXT)
- client_ip (TEXT)
- created_at (TEXT)

