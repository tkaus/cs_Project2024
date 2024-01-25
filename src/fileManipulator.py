import argparse
import requests 
import json
response = requests.get("https://api.weather.gov/gridpoints/FSD/149,22/forecast")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

data = response.json()

with open("text.json", "w+") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

