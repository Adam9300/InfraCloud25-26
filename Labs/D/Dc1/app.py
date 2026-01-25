import os
import argparse
from datetime import datetime

MESSAGE = os.getenv("APP_MESSAGE", "Hello from container!")
LOG_PATH = os.getenv("APP_LOG_PATH", "/var/log/myapp/app.log")

def log_line(line: str):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()}Z {line}\n")

def main():
    parser = argparse.ArgumentParser(description="My Docker CLI app")
    parser.add_argument("command", choices=["start", "status", "health"])
    args = parser.parse_args()

    if args.command == "start":
        log_line("start command")
        print(MESSAGE)

    elif args.command == "status":
        print("running")

    elif args.command == "health":
        print("OK")

if __name__ == "__main__":
    main()
