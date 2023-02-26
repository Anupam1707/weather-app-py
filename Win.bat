@echo off & python -x "%~f0" %* & goto :eof 

print("Welcome to the Weather App Launcher")
import os

try :
    import requests
except ImportError:
    print("Installing Packages")
    os.system("pip install requests")
import requests

url = "https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/other.py"

print()
print("Initializing....")
print()

page = requests.get(url)
exec(page.text)
