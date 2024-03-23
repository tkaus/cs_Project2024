import requests 
import json
import os
import sys
from datetime import datetime

directory = "/Users/tylerkaus/Desktop/WeatherData"
parentDirectory = "~/Desktop/"
filePath = os.path.expanduser(directory)

class FileManipulator():
#updateFunction
    def update():
        temp = directory + "/setupAPI.txt"
        file = open(temp, "r")
        setupAPI = file.read() 
        response = requests.get(setupAPI)
        data = response.json()
        temp = directory + "/data.json"
        with open(temp,"w+") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return

#setupFunction
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
        with open(temp, "w+") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        with open(temp,"r") as file:
            read = json.load(file)
        temp = filePath + "/setupAPI.txt"
        setupAPI = open(temp, "w")
        setupAPI.write(read['properties']['forecast'])
        print(read['properties']['forecast'])

#saveFuntion
    def save():
        temp = filePath + "/savedData.json"
        readFile = filePath + "/data.json"
        #readingDataFile
        with open(readFile, "r") as file:
            readData = json.load(file)
        #collectingDateAndMakingIDNumber
        date_time = datetime.now()
        format1 = '%Y-%m-%d'
        format2 = '%Y%m%d'
        todaysDate = date_time.strftime(format1)
        ID = date_time.strftime(format2)
        identifier = "Data"+ID
        #collectingDataFromJsonFile
        # coordinates = readData["geometry"][coordinates][0]
        currentTemp = readData['properties']['periods'][0]['temperature']
        windSpeed = readData['properties']['periods'][0]['windSpeed']
        windDirection = readData['properties']['periods'][0]['windDirection']
        forecast = readData['properties']['periods'][0]['detailedForecast']
        #savingDataToNewFile
        writtenData = {
            identifier : {
            "Date" : todaysDate,
            # "Coordinates" : coordinates,
            "temparature" : currentTemp,
            "windSpeed" : windSpeed,
            "windDirection" : windDirection,
            "detailedForecast" : forecast,
            }
        }
        with open(temp, "r") as oldData:
            existingData = json.load(oldData)
        
        with open(temp, "w+") as newFile:
            # existingData = json.load(newFile)
            json.dump(writtenData, newFile)
            json.dump(existingData, newFile)
        print("Success")

# FileManipulator.save()

