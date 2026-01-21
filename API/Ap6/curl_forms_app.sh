#!/usr/bin/env bash
set -euo pipefail

# API: https://httpbin.org

BASE_URL="https://httpbin.org"

require_tools() {
  command -v curl >/dev/null 2>&1 || { echo "Fout: curl is niet geïnstalleerd."; exit 1; }
}

line() { echo "--------------------------------------------"; }
pause() { read -r -p "Druk op Enter om verder te gaan..."; }
clear_screen() { printf "\033c"; }

extract_status() {
  sed -n '1{s/.* \([0-9][0-9][0-9]\).*/\1/p; q;}'
}

menu() {
  clear_screen
  echo "============================================"
  echo " REST API EXPERIMENT - CURL FORMS"
  echo "============================================"
  echo "1) POST "
  echo "2) GET /get (API test)"
  echo "q) Stoppen"
  line
}

get_ping() {
  echo "GET: $BASE_URL/get"
  line
  resp="$(curl -sS -i "$BASE_URL/get")"
  status="$(printf "%s" "$resp" | extract_status)"
  printf "%s\n" "$resp"
  line
  echo "HTTP status: $status"
}

post_form() {
  read -r -p "Naam: " name
  read -r -p "Email: " email
  read -r -p "Bericht: " message

  echo "POST multipart/form-data naar: $BASE_URL/post"
  line

  resp="$(curl -sS -i -X POST "$BASE_URL/post" \
    -F "name=$name" \
    -F "email=$email" \
    -F "message=$message")"

  status="$(printf "%s" "$resp" | extract_status)"
  printf "%s\n" "$resp"
  line
  echo "HTTP status: $status"
  echo "Controle: je formvelden staan in de JSON response onder \"form\"."
}

main() {
  require_tools

  while true; do
    menu
    read -r -p "Kies een optie: " choice
    case "$choice" in
      1) post_form; pause ;;
      2) get_ping; pause ;;
      q|Q) echo "Programma afgesloten."; exit 0 ;;
      *) echo "Ongeldige keuze."; pause ;;
    esac
  done
}

main
