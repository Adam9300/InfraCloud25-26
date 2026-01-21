#!/usr/bin/env bash
set -euo pipefail

BASE_URL="https://jsonplaceholder.typicode.com"

print_line() {
  echo "--------------------------------------------"
}

pause() {
  read -r -p "Druk op Enter om verder te gaan..."
}

require_tools() {
  command -v curl >/dev/null 2>&1 || { echo "Fout: curl is niet geïnstalleerd."; exit 1; }
}

show_menu() {
  clear
  echo "============================================"
  echo " REST API EXPERIMENT 3 - CURL (CLI MENU)"
  echo "============================================"
  echo "1) GET  - Alle users"
  echo "2) GET  - User op ID"
  echo "3) POST - Nieuwe post aanmaken"
  echo "4) DELETE - Post verwijderen op ID"
  echo "q) Stoppen"
  print_line
}

get_all_users() {
  echo "GET: $BASE_URL/users"
  print_line
  # -s: silent, -S: show errors, -i: include headers
  curl -sS -i "$BASE_URL/users"
  print_line
}

get_user_by_id() {
  read -r -p "Geef user ID (1-10): " id
  if [[ ! "$id" =~ ^[0-9]+$ ]]; then
    echo "Fout: ID moet een nummer zijn."
    return
  fi

  echo "GET: $BASE_URL/users/$id"
  print_line
  curl -sS -i "$BASE_URL/users/$id"
  print_line
}

create_post() {
  read -r -p "Titel: " title
  read -r -p "Body: " body
  read -r -p "UserId (nummer): " userId

  if [[ ! "$userId" =~ ^[0-9]+$ ]]; then
    echo "Fout: userId moet een nummer zijn."
    return
  fi

  # JSON payload maken (minimaal)
  payload=$(cat <<EOF
{
  "title": "$title",
  "body": "$body",
  "userId": $userId
}
EOF
)

  echo "POST: $BASE_URL/posts"
  echo "Payload:"
  echo "$payload"
  print_line

  # -X POST + header + data
  curl -sS -i -X POST "$BASE_URL/posts" \
    -H "Content-Type: application/json; charset=UTF-8" \
    -d "$payload"

  print_line
}

delete_post() {
  read -r -p "Geef post ID om te verwijderen (bv. 1): " id
  if [[ ! "$id" =~ ^[0-9]+$ ]]; then
    echo "Fout: ID moet een nummer zijn."
    return
  fi

  echo "DELETE: $BASE_URL/posts/$id"
  print_line
  curl -sS -i -X DELETE "$BASE_URL/posts/$id"
  print_line
}

main() {
  require_tools

  while true; do
    show_menu
    read -r -p "Kies een optie: " choice

    case "$choice" in
      1) get_all_users; pause ;;
      2) get_user_by_id; pause ;;
      3) create_post; pause ;;
      4) delete_post; pause ;;
      q|Q) echo "Programma afgesloten."; exit 0 ;;
      *) echo "Ongeldige keuze."; pause ;;
    esac
  done
}

main
