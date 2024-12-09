#Jose Franco
#12/08/2024
#Application programming interfaces (APIs) to pull data from a website.
#Testing ofice and fire API

#Importing libraries
import requests
import json

#Testing the connection to the Ofice and fire API
url = "https://anapioficeandfire.com/api/characters/583"
response = requests.get(url)

#Check status code
if response.status_code == 200:
    print("\nConnection successful!\n")
    # Display the raw JSON response in a vertical format
    raw_data = response.json()  # Parse JSON to ensure formatting works
    print("Raw Response:\n")
    print(json.dumps(raw_data, sort_keys = True, indent=4))
else:
    print(f"Failed to connect. Status code: {response.status_code}")
#Parsing and formatting the JSON data
data = response.json()
#Display formatted data
print("\nFormatted Output:\n")
print(f"Name: {data['name']}")
print(f"Gender: {data['gender']}")
print(f"Culture: {data['culture']}")
print(f"Born: {data['born']}")
print(f"Died: {data['died'] if data['died'] else 'Alive'}")
print(f"Titles: {', '.join(data['titles']) if data['titles'] else 'None'}")
print(f"Aliases: {', '.join(data['aliases']) if data['aliases'] else 'None'}")
print(f"Father: {data['father'] if data['father'] else 'Unknown'}")
print(f"Mother: {data['mother'] if data['mother'] else 'Unknown'}")
print(f"Spouse: {data['spouse'] if data['spouse'] else 'None'}")
print(f"Played By: {', '.join(data['playedBy']) if data['playedBy'] else 'None'}")

