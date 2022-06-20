from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def get_weather():
    return "yeh lo weather"


@app.route('/weather', methods=['POST'])
def add_weather():
    request_data = request.data
    # got the json data in string in the above line
    error_field = ""
    weather_dict = json.loads(request_data)
    if 'city' in weather_dict and len(str(weather_dict['city']).strip())>0:
        city = str(weather_dict['city'])
    else:
        error_field += "city "

    if 'state' in weather_dict and len(str(weather_dict['state']).strip())>0:
        state = str(weather_dict['state'])
    else:
        error_field += "state "

    if 'country' in weather_dict and len(str(weather_dict["country"]).strip())>0:
        country = str(weather_dict['country'])
    else:
        error_field += "country "


    if 'latitude' in weather_dict and len(str(weather_dict['latitude']).strip())>0:
        latitude = str(weather_dict['latitude'])
    else:
        error_field += "latitude "

    if 'longitude' in weather_dict and len(str(weather_dict['longitude']).strip())>0:
        longitude = str(weather_dict['longitude'])
    else:
        error_field += "longitude "

    if 'temperature' in weather_dict and len(str(weather_dict['temperature']).strip())>0:
        temperature = str(weather_dict['temperature'])
    else:
        error_field += "temperature "

    if 'timestamp' in weather_dict and len(str(weather_dict['timestamp']).strip())>0:
        timestamp = str(weather_dict['timestamp'])
    else:
        error_field += "timestamp "



    # logic to manipulate data and save it to database.




    error_status="\"message\":\"{} value is required\"".format(error_field)
    if(len(error_field) > 0):
        response = Response(error_status, status=400, content_type="application/json")
        return response
    return city



@app.route('/weather', methods=['PUT'])
def put_weather():
    return "weather updated"


@app.route('/weather', methods=['DELETE'])
def delete_weather():
    return "weather deleted"


if __name__ == '__main__':
    app.run()
