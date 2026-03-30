import requests

def get_city_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city
    }
    try:
        r = requests.get(url,params=params)
        data=r.json()
        city_geography = data["results"][0]
        latitude = city_geography["latitude"]
        longitude = city_geography["longitude"]
        get_city_weather(latitude,longitude,city)
    except Exception as e:
        print(f'Something wrong : {e}')


def get_city_weather(lan,lon,city):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lan}&longitude={lon}&current_weather=true"
    try:
        current_weather = requests.get(weather_url).json()
        weather = current_weather["current_weather"]
        print(f'City : {city} Temperate : {weather["temperature"]} C WindSpeed : {weather["windspeed"]} Km/h')
    except Exception as e:
        print(f'Could not find current weather : {e}')

get_city_coordinates("Lahore")
get_city_coordinates("Islamabad")
get_city_coordinates("Karachi")