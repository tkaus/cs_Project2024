import requests 
import json
import os
import sys

directory = "/Users/tylerkaus/Desktop/WeatherData"
parentDirectory = "~/Desktop/"
filePath = os.path.expanduser(directory)

class FileManipulator():
    def update():
        temp = directory + "/setupAPI.txt"
        file = open(temp, "r")
        #file = open("setupAPI.txt", "r")
        setupAPI = file.read() 
        response = requests.get(setupAPI)
        data = response.json()
        temp = directory + "/data.json"
        with open(temp,"w+") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return

    def setup():
        if not os.path.exists(filePath):
            os.mkdir(filePath)
         
        latitude = input("Enter the latitude coordinates of a city: ")
        longitude = input("Enter the longitude coordinates of a city: ")
        apicall = "https://api.weather.gov/points/"+latitude+ ","+longitude
        apicall = apicall.replace(" ", "")
        response = requests.get(apicall)
        data = response.json()
        temp = filePath + "/apicall.json"
        #with open("apicall.json","w+") as f:
        with open(temp, "w+") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        with open(temp,"r") as file:
            read = json.load(file)
        temp = filePath + "/setupAPI.txt"
        setupAPI = open(temp, "w")
        setupAPI.write(read['properties']['forecast'])
        print(read['properties']['forecast'])
