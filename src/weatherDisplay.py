import json
import os 
import sys

directory = "/Users/tylerkaus/Desktop/WeatherData"
parentDirectory = "~/Desktop/"
filePath = os.path.expanduser(directory)

class WeatherDisplay():
    #displaysTemparature 
    def current():
        temp = filePath + "/data.json"
        with open(temp, 'r') as file:
            weatherData = json.load(file)
        output = weatherData['properties']['periods'][0]['temperature']
        return output

    #displaysCustomData 
    def current2(input):
        temp = filePath + "/data.json"
        with open(temp, 'r') as file:
            weatherData = json.load(file)
        output = "Please Try Again"
        try: 
            output = weatherData['properties']['periods'][0][input]
        except KeyError:
            print("""Command Failed! Try these other metrics instead.
            startTime::starting point of the reading 
            endTime::end point of the reading 
            temperature::current temparature 
            temperatureTrend::current trend of temparature
            windSpeed::current wind speed 
            windDirection::current wind direction 
            shortForecast::shortened version of the current forecast 
            detailedForecast::detailed version of current forecast""") 
        return output
    
    #displaysDataFromSavedFile
    def read(info):
        
        temp = filePath + "/" + info + ".json"
        if os.path.exists(temp):
            with open(temp,"r") as file:
                readData = json.load(file)
            #printingTheData 
            print("==========================")
            print("Date: " + str(readData["properties"]["updated"]))
            print("Temperature: "+ str(readData["properties"]["periods"][0]["temperature"]))
            print("Wind Speed: "+str(readData["properties"]["periods"][0]["windSpeed"]))
            print("Wind Direction: "+str(readData["properties"]["periods"][0]["windDirection"]))
            print("Detailed Forecast: "+str(readData["properties"]["periods"][0]["detailedForecast"]))
            print("==========================")
            print("Success")
        else:
            print("File does not exist or incorrect command.")
