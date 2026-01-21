import requests

base_url = "https://jsonplaceholder.typicode.com"

def get_all_users():
    """
    Haalt alle gebruikers op via de REST API
    """
    url = f"{base_url}/users"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Fout bij ophalen van gebruikers.")
        print("Statuscode:", response.status_code)
        return None


def get_user_by_id(user_id):
    """
    Haalt één specifieke gebruiker op via ID
    """
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Gebruiker niet gevonden.")
        return None


def main():
    # 1. Alle gebruikers ophalen
    users = get_all_users()

    if users is None:
        return

    print("Lijst van gebruikers:\n")

    for user in users:
        print("ID   :", user["id"])
        print("Naam :", user["name"])
        print("Email:", user["email"])
        print("-" * 30)

    # 2. Specifieke gebruiker opvragen
    while True:
        user_input = input("\nVoer een gebruikers-ID in (of 'q' om te stoppen): ")

        if user_input.lower() == "q":
            print("\nProgramma afgesloten.")
            break

        if not user_input.isdigit():
            print("Voer een geldig nummer in.")
            continue

        user_id = int(user_input)
        user = get_user_by_id(user_id)

        if user:
            print("\nGevonden gebruiker:")
            print("Naam :", user["name"])
            print("Email:", user["email"])
            print("Stad :", user["address"]["city"])


if __name__ == "__main__":
    main()