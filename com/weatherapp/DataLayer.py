import psycopg2


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="weatherapp",
        user="postgres",
        password="password")

    return conn


def save_to_db(weather_dict):
    city = str(weather_dict['city'])
    state = str(weather_dict['state'])

    country = str(weather_dict['country'])
    latitude = str(weather_dict['latitude'])
    longitude = str(weather_dict['longitude'])
    temperature = str(weather_dict['temperature'])
    timestamp = str(weather_dict['timestamp'])
    # logic to manipulate data and save it to database.
    # creating connection object
    try:
        conn = get_connection();
        cursor = conn.cursor()
        cursor.execute(
            '''Insert into weather (city, state, country, latitude, longitude, temperature, timestamp) values(%s,%s,%s,%s,%s,%s,%s);''',
            (city, state, country, latitude, longitude, temperature, timestamp))
        # writing create table query
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_all_from_db():
    connection=get_connection()
    cursor = connection.cursor()
    cursor.execute(
       'select * from weather');
    rows= cursor.fetchall()
    return rows

