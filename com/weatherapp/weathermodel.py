#Weather class with attributes

import temperature
import flask
from flask import request, render_template
from flask_restful import Api
import requests
import geocoder
import temperature
# Not in use right now, will use it later
class Weather:

    def __init__(self, latitude, longitude, timestamp, temperatureINF, millisec, city, state, country,):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.millisec = millisec
        self.temperatureInF = temperatureINF
        self.city = city
        self.state = state
        self.country = country





