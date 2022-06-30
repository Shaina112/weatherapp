from flask import Flask, request, Response
import json
from validator import validate_request
from DataLayer import save_to_db, get_all_from_db

app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def get_weather():

    rows= get_all_from_db()
    rows_json = json.dumps(rows)
    response = Response(rows_json,content_type="application/json" )
    return response

@app.route('/weather', methods=['POST'])
def add_weather():
    request_data = request.data
    # got the json data in string in the above line
    weather_dict = json.loads(request_data)
    # validation done here
    error_fields = validate_request(weather_dict)
    if (len(error_fields) > 0):
        error_status = "\"message\":\"{} value is required\"".format(error_fields)
        response = Response(error_status, status=400, content_type="application/json")
        return response
    # valid data, now process it

    save_to_db(weather_dict)
    return "{\"message\":\"weather added successfully\"}"


@app.route('/weather', methods=['PUT'])
def put_weather():
    #Code to be implemented
    return "weather updated"


@app.route('/weather', methods=['DELETE'])
def delete_weather():
    #code to be implemented
    return "weather deleted"


if __name__ == '__main__':
    app.run()
