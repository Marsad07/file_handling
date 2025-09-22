import json

# Create dictionaries
users = ({"name": "Marsad", "age": 18, "favorite_color": "blue"},
          {"name": "Ali", "age": 20, "favorite_color": "green"})

with open("users.json", 'w') as file:
    json.dump(users, file)
    print(users)

