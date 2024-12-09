#Jose Franco
#12/08/2024
#Application programming interfaces (APIs) to pull data from a website, specifically OpenNotify astronauts API

#Importing libraries
import requests
import json

#Testing the connection to the OpenNotify astronauts API
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

#Check status code
if response.status_code == 200:
    print("Connection successful!\n")
    # Display the raw JSON response in a vertical format
    raw_data = response.json()  # Parse JSON to ensure formatting works
    print("Raw Response:\n")
    print(json.dumps(raw_data, sort_keys = True, indent=4))
else:
    print(f"Failed to connect. Status code: {response.status_code}")
#Parsing and formatting the JSON data
data = response.json()
print("\nFormatted Output:")
print(f"There are {data['number']} astronauts currently in space:")
for person in data['people']:
    print(f"- {person['name']} on {person['craft']}")
