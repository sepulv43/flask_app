import forecastio
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key = os.environ['FORECASTIO_API_TOKEN']

def get_weather(address,):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	if location == None: 
		return "location not found"
	else:
		forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
		return "{} and {} in {}".format(forecast.summary, forecast.temperature, location.address)
