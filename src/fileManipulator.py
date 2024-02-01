#import argparse
import requests 
import json


class FileManipulator():
    def update():
        response = requests.get("https://api.weather.gov/gridpoints/FSD/149,22/forecast")
        data = response.json()
        with open("data.json","w+") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return

    def current():
        with open('data.json', 'r') as file:
            weatherData = json.load(file)
        output = weatherData['properties']['periods'][0]['temperature']
        return output

