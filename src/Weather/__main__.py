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
    elif sys.argv[1] == 'help':
        print("""
              Commands: 
                setup
                update
                current""")
