from flask import Flask, request, Response
import json
from validator import Validator
from DataLayer import WeatherDataLayer

app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def get_weather():
    return "yeh lo weather"


@app.route('/weather', methods=['POST'])
def add_weather():
    request_data = request.data
    # got the json data in string in the above line
    weather_dict = json.loads(request_data)
    # validation done here
    error_fields = Validator.validate_request(weather_dict)
    if (len(error_fields) > 0):
        error_status = "\"message\":\"{} value is required\"".format(error_fields)
        response = Response(error_status, status=400, content_type="application/json")
        return response
    # valid data, now process it

    WeatherDataLayer.save_to_db(weather_dict)

    return "{\"message\":\"weather added successfully\"}"


@app.route('/weather', methods=['PUT'])
def put_weather():
    return "weather updated"


@app.route('/weather', methods=['DELETE'])
def delete_weather():
    return "weather deleted"


if __name__ == '__main__':
    app.run()
