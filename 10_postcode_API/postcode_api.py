# import requests
#
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# # First iteration
# if check_response_postcode.status_code == 200:
#     print('The status code is valid and returned code:', check_response_postcode.status_code)
# else:
#     print('Oops something went wrong. Please try again later.')


# ====================================================================================

# import requests
#
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# # Second iteration
# if check_response_postcode:
#     print('Success!')
# else:
#     print('Unavailable.')


# ====================================================================================

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

#
# checklist for api:

# prompt the user to enter the postcode
# validate the postcode
# present the location back to the user with appropriate message
#
