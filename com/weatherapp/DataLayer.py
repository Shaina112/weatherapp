import sqlite3

class WeatherDataLayer:


    def save_to_db(weather_dict):
        create_table_query = "create table if not exists weather (city TEXT, state TEXT, country TEXT, " \
                             "longitude TEXT, latitude TEXT, temperature TEXT, timestamp TEXT)"
        city = str(weather_dict['city'])
        state = str(weather_dict['state'])

        country = str(weather_dict['country'])
        latitude = str(weather_dict['latitude'])
        longitude = str(weather_dict['longitude'])
        temperature = str(weather_dict['temperature'])
        timestamp = str(weather_dict['timestamp'])
        # logic to manipulate data and save it to database.
        connection = sqlite3.connect("weather.db")
        # creating connection object
        cursor = connection.cursor()
        # creating table
        connection.execute(create_table_query)
        connection.execute(
            """Insert into weather (city, state, country, latitude, longitude, temperature, timestamp) values(?,?,?,?,?,?,?);""",
            (city, state, country, latitude, longitude, temperature, timestamp))
        # writing create table query
        connection.commit()
        connection.close()

