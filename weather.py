import requests

API_KEY = "{your own API key}"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def geolocation(city_name):
  GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"
  geo_request_url = f"{GEO_URL}?q={city_name}&appid={API_KEY}"
  geo_response = requests.get(geo_request_url)
  data = geo_response.json()
  lat = data[0]["lat"]
  lon = data[0]["lon"]
  
  return [lat, lon]

city = input("Enter a city name: ")
geo_data = geolocation(city)

request_url = f"{BASE_URL}?lat={geo_data[0]}&lon={geo_data[1]}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
  data = response.json()
  weather = data["weather"][0]["description"]
  temperature = round(data["main"]["temp"] - 273.15, 2)
  
  print("Weather:", weather)
  print("Temperature:", temperature, "celsius")
else:
  print("An error occurred")

