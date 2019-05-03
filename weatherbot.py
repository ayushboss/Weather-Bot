import urllib
import json

def getIp():
	url = 'https://api.ipify.org?format=json'
	ipRaw = urllib.urlopen(url).read()
	ip = json.loads(ipRaw)['ip']
	return ip;

def getWeatherForecast(ip):
	base_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?'
	query='key=6aa7a3414caa408d818152633190305&q='+ip+'&num_of_days=0&format=json'
	url = base_url+query
	data = urllib.urlopen(url).read()
	parsed = json.loads(data)
	current_weather = parsed['data']['current_condition'][0]
	return current_weather

def displayWeather(data):
	print """
		Weather: '{0}'
		Temperature: '{1}'
		Wind: '{2}'
		Precipitation: '{3}' MM
	""".format(data['weatherDesc'][0]['value'], data['temp_F'], data['windspeedKmph'], data['precipMM'])

ip = getIp()
weatherData = getWeatherForecast(ip)
displayWeather(weatherData)
