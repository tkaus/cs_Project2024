import json 
import os

directory = "/Users/tylerkaus/Desktop/WeatherData"
parentDirectory = "~/Desktop/"
filePath = os.path.expanduser(directory)

readFile = filePath + "/data.json"

with open(readFile, "r") as file:
    readData = json.load(file)
print("the program is working")
print(readData["geometry"]["coordinates"][0])
