from datetime import datetime
import json
import os
import random
import sys

data_file = "dice_results.json"
log_file = "dice_logs.txt"

def login_user():
    return input("Input your username: ")

def log(str):
    with open(log_file, "a+") as f:
        f.write(f"{datetime.now()} --- {str} \n")

def load_data():
    with open(data_file, "r+") as f:
        # If the file is empty, return an empty list
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)

def roll_dice(sides, rolls):
    return [int(random.random() * (sides + 1)) for i in range(rolls)]

if __name__ == "__main__":
    data = load_data()
    args = sys.argv[1:]
    if "--user" in args:
        username = args[args.index("--user") + 1]
    else:
        username = os.environ.get('USER') or login_user()

    if "--sides" in args:
        sides = int(args[args.index("--sides") + 1])
    else:
        sides = 6

    if "--count" in args:
        count = int(args[args.index("--count") + 1])
    else:
        count = 1

    log(f"Starting game for user: {username}, sides: {sides}, dices: {count}")
    print(f"Welcome, {username}!")
    print("--------------------------------\n")

    while True:
        print("1. Roll dice")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            values = roll_dice(sides, count)
            print(f"You rolled: {values}")
            log(f"User {username} rolled: {values}")

            for value in values:
                data.append({"name": username, "value": value, "timestamp": str(datetime.now())})
            log(f"User {username} saved results: {data}")

            save_data(data)
        elif choice == "2":
            log(f"User {username} chose to exit")
            break
        else:
            print("Invalid choice")
            log(f"User {username} chose invalid choice: {choice}")
        print("\n--------------------------------\n")