#import argparse
import requests 
import json


class FileManipulator():
    def update():
        file = open("setupAPI.txt", "r")
        setupAPI = file.read() 
        # response = requests.get("https://api.weather.gov/gridpoints/FSD/149,22/forecast")
        response = requests.get(setupAPI)
        data = response.json()
        with open("data.json","w+") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return

    def current():
        with open('data.json', 'r') as file:
            weatherData = json.load(file)
        output = weatherData['properties']['periods'][0]['temperature']
        return output

    def setup():
        latitude = input("Enter the x coordinates of a city: ")
        longitude = input("Enter the y coordinates of a city: ")
        apicall = "https://api.weather.gov/points/"+latitude+ ","+longitude
        apicall = apicall.replace(" ", "")
        print(apicall)
        response = requests.get(apicall)
        data = response.json()
        with open("apicall.json","w+") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        with open("apicall.json","r") as file:
            read = json.load(file)
        setupAPI = open("setupAPI.txt", "w")
        setupAPI.write(read['properties']['forecast'])
        print(read['properties']['forecast'])
        