#! / usr/bin/python3
import requests
import sys

if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

url = "http://0.0.0.0:5000/search_user"
data = {'q': letter}
response = requests.post(url, data=data)

try:
    response_data = response.json()
    if response_data:
        user_id = response_data.get('id')
        user_name = response_data.get('name')
        if user_id is not None and user_name is not None:
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
