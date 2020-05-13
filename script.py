import requests

url_template = 'http://wttr.in/{}'
payload = {'m':'', 'n':'', 'T':'', 'lang':'ru'}
cities = ['belarus', 'svo', 'minsk']
for city in cities:
    url = url_template.format(city)
    response = requests.get(url, params=payload)
    print(response.text)