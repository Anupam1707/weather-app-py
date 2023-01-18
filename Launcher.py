import requests
url = 'https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/main.py'
page = requests.get(url)
exec(page.text)
