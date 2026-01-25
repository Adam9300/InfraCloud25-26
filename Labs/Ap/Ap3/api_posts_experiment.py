import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_all_posts():
    """
    Haalt alle posts op via de REST API
    """
    response = requests.get(f"{BASE_URL}/posts")

    if response.status_code == 200:
        return response.json()
    else:
        print("Fout bij ophalen van posts.")
        return None


def get_post_by_id(post_id):
    """
    Haalt één specifieke post op via ID
    """
    response = requests.get(f"{BASE_URL}/posts/{post_id}")

    if response.status_code == 200:
        return response.json()
    else:
        print("Post niet gevonden.")
        return None


def main():
    posts = get_all_posts()

    if not posts:
        return

    print("\nOverzicht van posts:\n")

    for post in posts[:10]:  # enkel eerste 10 tonen
        print("Post ID :", post["id"])
        print("Titel  :", post["title"])
        print("-" * 40)

    while True:
        user_input = input("\nVoer een post-ID in (of 'q' om te stoppen): ")

        if user_input.lower() == "q":
            print("Programma afgesloten.")
            break

        if not user_input.isdigit():
            print("Geef een geldig nummer in.")
            continue

        post = get_post_by_id(int(user_input))

        if post:
            print("\nPost details:")
            print("Titel :", post["title"])
            print("Inhoud:")
            print(post["body"])


if __name__ == "__main__":
    main()
