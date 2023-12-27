import requests 
import geopy
geolocator = geopy.Nominatim(user_agent="Weather")
api_key = '45db40e61c13b4a4c6609debf481e505'
user_input = input("Enter the city: ")
location = geolocator.geocode(user_input)
weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}')
print(weather.json())