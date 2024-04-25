# Command Line Weather Application 
This program will allow the user to view the weather forcast and other metrics in  
in the command line. It will also save data from the day to help track weather  
forcast over time.
# Instructions to Build Project 
In terminal, run the following command>
 python3 weatherapp.py (*command*)
# List of current commands 
## update 
fetches recent data from API 
## setup 
tells program which area to fetch data from 
## current 
fetches the current temperature from weather data   
also can be used with the name of a metric   
for example > python3 weatherapp.py windSpeed
## save 
saves a collection of data from the current weather  
data file to a new file identifiable with a date  
## read 
reads data from a saved file  
use command by typing into the terminal python3 weatherapp.py read YYYYMMDD  
REMEMBER TO EXCLUDE "-" OR "/"
## delete 
deletes a saved file  
use command by typing into the terminal python3 weatherapp.py delete YYYYMMDD  
REMEMBER TO EXCLUDE "-" OR "/" 
