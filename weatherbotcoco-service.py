#-*- coding:utf-8 -*-
import tweepy
import pyowm

# twitter api setting
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')
api = tweepy.API(auth)

# pyowm api setting
owm = pyowm.OWM('')
observation = owm.weather_at_place('Seoul,KR')

# get weather data
weather = observation.get_weather()
prsTemp = weather.get_temperature('celsius')['temp']
maxTemp = weather.get_temperature('celsius')['temp_max']
minTemp = weather.get_temperature('celsius')['temp_min']
humidity = weather.get_humidity()
weatherStatus = weather.get_status()
  
firstLine = '[오늘의 날씨]'
secondLine = "현재: " + str(prsTemp) + "℃   "
secondLine += "최고: " + str(maxTemp) + "℃   "
secondLine += "최저: " + str(minTemp) + "℃"
thirdLine = "습도: " + str(humidity) + "%  "
thirdLine += "기상: " + weatherStatus

statusString = firstLine +'\n'+ secondLine +'\n'+ thirdLine

print(statusString)
print("-" * 30)

api.update_status(status = statusString)
