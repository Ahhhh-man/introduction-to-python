# Postcode API
The official documentation about postcode API can be found [here](https://docs.python-requests.org/en/master/user/quickstart/#response-status-codes).

## Understanding how to use them
First we need to request the api, so we will need to `import requests`. Recall you will need to also do `pip install requests` if the request package is not globally installed on your device.

We call the api using `requests.get()` and check the status of the api using `.status_code`.
```python
import requests

check_response_postcode = requests.get("https://api.postcodes.io/postcodes/se120nb")

# First iteration
if check_response_postcode.status_code == 200:
    print('The status code is valid and returned code:', check_response_postcode.status_code)
else:
    print('Oops something went wrong. Please try again later.')
```
or equivalently,
```python
import requests

check_response_postcode = requests.get("https://api.postcodes.io/postcodes/se120nb")

# Second iteration
if check_response_postcode:
    print('Success!')
else:
    print('Unavailable.')
```

We can check the output of the call,
```python
import requests

check_response_postcode = requests.get("https://api.postcodes.io/postcodes/B152TT")
# print(type(check_response_postcode.headers))

# Let's see how we can parse from dict
# print(check_response_postcode.json())   # json() converts that data

# Let's store this data into a variable
response_dict = check_response_postcode.json()
# print(type(response_dict))
# print(response_dict)

result_dict = response_dict['result']
# print(result_dict)

for key in result_dict:
    print(f'The name of the key is {key} and the value is {result_dict[key]}.')
```

## Activity

### Checklist for API:
- prompt the user to enter the postcode
- validate the postcode
- present the location back to the user with appropriate message

## Solution
```python
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


postcode = PostcodeApi('se120nb')
print(postcode.message())

```