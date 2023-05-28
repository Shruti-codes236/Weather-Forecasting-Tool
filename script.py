#Author: Shruti Avhad
#Python program to check weather details using openweathermap API and request module and json module

# importing the requests library
import requests
import json

# api-endpoint
URL = "http://api.openweathermap.org/data/2.5/weather?"

# location given here
location = input("Enter the city name: ")

# defining a params dict for the parameters to be sent to the API
PARAMS = {'q': location, 'appid': '247a3cedba5706345e51babc0b56a264'}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

y = data['cod']

if y != 200:
    print("City not found")
    exit()

# extracting temperature, pressure, humidity, wind speed, wind direction, cloudiness, sunrise and sunset
temp = data['main']['temp']
pressure = data['main']['pressure']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
wind_direction = data['wind']['deg']
cloudiness = data['clouds']['all']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']

# converting temperature from kelvin to celsius
#temp = temp - 273.15

# converting wind direction from degrees to direction
if wind_direction >= 0 and wind_direction <= 90:
    wind_direction = "North East"
elif wind_direction > 90 and wind_direction <= 180:
    wind_direction = "South East"


# printing the output
print("Temperature: " + str(temp) + " degree Kelvin")
print("Pressure: " + str(pressure) + " hPa")
print("Humidity: " + str(humidity) + " %")
print("Wind Speed: " + str(wind_speed) + " m/s")
print("Wind Direction: " + str(wind_direction))
print("Cloudiness: " + str(cloudiness) + " %")
print("Sunrise: " + str(sunrise) + " UTC")
print("Sunset: " + str(sunset) + " UTC")
