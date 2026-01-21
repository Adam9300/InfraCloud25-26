import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL", "https://api.github.com")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))

def main():
    r = requests.get(URL, timeout=TIMEOUT)
    print("Status:", r.status_code)
    print("Server:", r.headers.get("Server"))
    data = r.json()
    # GitHub root endpoint bevat vaak 'current_user_url' etc.
    print("Keys:", list(data.keys())[:8])

if __name__ == "__main__":
    main()
