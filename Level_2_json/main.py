import json

# Python Dictionary
user = {"name": "Marsad", "age": 18, "favorite_club": "LFC"}

# This is for saving a dictionary to JSON file in your directory
with open("user.json", 'w') as file:
    # dump is used to dump the object into a file in Json format
    json.dump(user, file)




