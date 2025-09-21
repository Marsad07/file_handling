import json
from datetime import date

today = date.today()

with open("log.txt", 'a') as file:
    file.write(str(today) + "\n")

print("Date has been added to log:", today)
