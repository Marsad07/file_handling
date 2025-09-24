import json
import os.path

all_users = []

# this will read the list of the users that already exist
if os.path.exists("data.json"):
    with open("data.json", 'r') as file:
        all_users = json.load(file)


# Here we collect the input and store it in a dictionary
user_name = (input("Enter your name: "))
user_age = (input("Enter your age: "))
user_fav = (input("Enter your favourite food: "))

user = {"name": user_name, "age": user_age, "favorite_food": user_fav}
all_users.append(user)

with open("data.json", 'w') as file:
    json.dump(all_users, file, indent=4)
    print(all_users)



