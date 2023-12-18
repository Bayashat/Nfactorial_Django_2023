import requests

def weather_api(city):
    api_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': 'd96324cbb9c32b869936b0e36a2e2728',
        'units': 'metric' # Celsius
    }

    res = requests.get(api_url, params=params)

    data = res.json()
    return data['main']['temp']
    # print(data['main']['feels_like'])
