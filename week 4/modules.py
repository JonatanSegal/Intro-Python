import requests

res = requests.get('http://kea.dk')

print(res.text)
