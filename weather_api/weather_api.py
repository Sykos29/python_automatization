import requests

API_KEY = '##########PERSONAL_API_KEY##########'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Enter a city name: ")

request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
print(request_url)

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()

    cityname = data['name']

    weather = data['weather'][0]['description']

    temperature = round((data['main']['temp']-273.15),2)

    print(f'The weather in {cityname} is currently {weather} at {temperature} °C');

else:
    print(response.status_code)

