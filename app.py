# Jeff Dorwart
from datetime import datetime, timezone, timedelta
# import date       #Imports date
import time
import requests  # imports requests for web pages
# now = time.time # current time in seconds from Nov 1970.
# pto = -28800 # number of seconds offset for pacific standard time.
# pst_zonedelta = timedelta(seconds=pto)
# pst_zone =timezone(pst_zonedelta)
# now_datetime = datetime.fromtimestamp(now, pst_zone)
# dtnow = datetime.now()
# print (str('current datetime =' + dtnow))      # insertedd for troubleshooting
from flask import Flask, render_template
from jinja2 import Template
from flask_bootstrap import Bootstrap  # Installs bootstrap
import json

app = Flask(__name__)
Bootstrap(app)  # added 1105pm
# today = str(date.today())       #gets todays date as today
myLoc = 'New London, US'  # Temporarily set to static until form is developed


# myLoc= input("Enter your City, and Country i.e. New York, US : "
def getWeather(city, country):
    # Sends APPID, Key , Q and Desired location to openweather.org api.
    payload = {'APPID': 'db9e05cbff0486677c7460f541a309d1', 'q': city + ', ' + country, 'units': 'imperial'}
    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    # creates a response object (dictionary) from the requests JSON output
    response = r.json()
    # Create a dictionary from the response data 
    return {"temp": str(response['main']['temp']) + ' F',
            "feels_like": str(response['main']['feels_like']) + ' F',
            "Wind": str(response['wind']['speed']) + ' MPH',
            "condition": (response['weather'][0]['description']),
            "Sunrise": (response['sys']['sunrise']),
            "Sunset": (response['sys']['sunset'])
            }


# @app.route('/weather/<location>')
# def weatherBoot(location):
#        return render_template('weather.html', data = weatherDict,myLoc = location) 
@app.route('/weather/<city>:<country>')
def weather(city, country):
    weather_data = getWeather(city, country)
    return render_template('weather.html', **weather_data)


@app.route('/withboot/<city>:<country>')
def withBootStrap(city, country):
    weather_data = getWeather(city, country)
    return render_template('weatherboot.html', data=weather_data)
# print ("Current Time :" + now_datetime.strftime('%h:%m:%s'))
