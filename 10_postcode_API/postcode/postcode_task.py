import requests


class PostcodeApi:
    def __init__(self, user_postcode):
        self.user_postcode = user_postcode
        self.check_response_postcode = requests.get("https://api.postcodes.io/postcodes/" + self.user_postcode)
        self.response_dict = self.check_response_postcode.json()
        if self.check_response_postcode:
            self.result_dict = self.response_dict['result']
        else:
            self.error_dict = self.response_dict['error']

    def check_valid(self):
        return True if self.check_response_postcode else False

    def location(self):
        return self.result_dict['admin_district'] if self.check_valid() else None

    def longitude(self):
        return self.result_dict['longitude'] if self.check_valid() else None

    def latitude(self):
        return self.result_dict['latitude'] if self.check_valid() else None

    def message(self):
        return f'The postcode you have given is {self.user_postcode}. Your location is {self.location()}; the longitude is {self.longitude()} and latitude is {self.latitude()}.' if self.check_valid() else self.error_dict

