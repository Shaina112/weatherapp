class Validator:

    def validate_request(weather_dict):
        fields=["city", "state", "country", "latitude", "longitude", "temperature", "timestamp"]
        error_fields=""
        for field in fields:
            if field not in weather_dict or len(str(weather_dict[field]).strip()) == 0:
                error_fields += field + " "

        return error_fields