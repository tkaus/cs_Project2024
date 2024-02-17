import sys

#importinClasses
sys.path.append("..")
from fileManipulator import FileManipulator

n = len(sys.argv)

if (n == 1):
    print("Too few arguments")
    print("Type 'help' to see a list of commands.")
else: 
    if sys.argv[1] == "setup":
        FileManipulator.setup()
        FileManipulator.update()
        print("Success") 
    elif sys.argv[1] == "update":
        FileManipulator.update() 
    elif sys.argv[1] == "current":
        output = FileManipulator.current()
        print(output, "F")
    elif sys.argv[1] == 'help':
        print("""
              Commands: 
                setup
                update
                current""")
