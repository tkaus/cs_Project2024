import argparse
import requests 
import json
import sys

n = len(sys.argv)

if (n == 1):
    print("Too few arguments")
else: 
    if argv[1] == "setup":
        print('Program is working')
        