import json 
import os
from datetime import datetime

directory = "/Users/tylerkaus/Desktop/WeatherData"
parentDirectory = "~/Desktop/"
filePath = os.path.expanduser(directory)

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
currentTemp = readData['properties']['periods'][0]['temperature']
windSpeed = readData['properties']['periods'][0]['windSpeed']
windDirection = readData['properties']['periods'][0]['windDirection']
forecast = readData['properties']['periods'][0]['detailedForecast']
#savingDataToNewFile
writtenData = {
    identifier : {
    "Date" : todaysDate,
    "temparature" : currentTemp,
    "windSpeed" : windSpeed,
    "windDirection" : windDirection,
    "detailedForecast" : forecast,
    }
}
with open(temp, "r+") as file:
    existingData = json.load(file)
    tempVar = existingData[writtenData]
    tempVar.append(writtenData)
    json.dump(existingData, file)

# with open(temp, "w+") as newFile:

    # newFile.write(json.dumps(writtenData))
    # newFile.write(json.dumps(existingData))
    # json.dump(existingData, newFile)
print("Success")
