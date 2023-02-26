@echo off & python -x "%~f0" %* & goto :eof 

print("Welcome to the Weather App Launcher")
import os

try :
    import requests
except ImportError:
    print("Installing Packages")
    os.system("pip install requests")
import requests

print("Select from the below option :- ")
print("For Fullscreen (1280x720) : Press f or F")
print("For Windowed   : Press w or W")

st = str(input())

if st == "f" or st == "F":
    url = "https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/main.py"
elif st == "w" or st == "W":
    url = "https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/other.py"

print()
print("Initializing....")
print()

page = requests.get(url)
exec(page.text)
