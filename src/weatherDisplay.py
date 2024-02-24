import json
import os 
import sys

directory = "/Users/tylerkaus/Desktop/WeatherData"
parentDirectory = "~/Desktop/"
filePath = os.path.expanduser(directory)

class WeatherDisplay():
    def current():
        temp = filePath + "/data.json"
        with open(temp, 'r') as file:
            weatherData = json.load(file)
        output = weatherData['properties']['periods'][0]['temperature']
        return output
    
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
            shortForecast::shortended version of the current forecast 
            detailedForecast::detailed version of current forecast""") 
        return output
    
