import requests


payload = {'m':'','T':'','q':'','u':'','lang':'ru'}
cities = ['Лондон', 'svo', 'Череповец']
for city in cities:
    url = f'http://wttr.in/{city}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
