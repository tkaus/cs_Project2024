import sys

#importinClasses
sys.path.append("..")
from fileManipulator import FileManipulator as files
from weatherDisplay import WeatherDisplay as display

n = len(sys.argv)

if (n == 1):
    print("Too few arguments")
    print("Type 'help' to see a list of commands.")
else: 
    if sys.argv[1] == "setup":
        files.setup()
        files.update()
        print("Success") 
    elif sys.argv[1] == "update":
        files.update() 
    elif sys.argv[1] == "current":
        if (n == 3):
            input = sys.argv[2]
            output = display.current2(input)
            print(output)
        else:
            output = display.current() 
            print(output, "F")
    elif sys.argv[1] == "save":
        print("This will save the current data file.")
        files.save()
    elif sys.argv[1] == "read":
        if (n == 3):
            print('Fetching Data')
            info = sys.argv[2]
            display.read(info)
        else:
            print("To use the read function, structure your command like the following.")
            print(">>> read YYYYMMDD")
    elif sys.argv[1] == "delete":
        if (n == 3):
            info = sys.argv[2]
            userin = input("y/n Are you sure you want to delete " + info + " >>> ")
            if(userin == "y"):
                print('Deleting Data')
                files.delete(info)
            else:
                print("okay")
        else:
            print("To use the delete function, structure your command like the following.")
            print(">>> read YYYYMMDD")
    elif sys.argv[1] == 'help':
        print("""
              Commands: 
                setup
                update
                current
                save""")
