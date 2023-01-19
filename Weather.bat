@echo off & python -x "%~f0" %* & goto :eof 

import os

try :
    import requests
except ImportError:
    print("Installing Packages")
    os.system("pip install requests")
import requests

url = 'https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/run.py'
page = requests.get(url)
exec(page.text)
