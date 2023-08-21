#! / usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script_name.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

url = "https://api.github.com/user"
headers = {
    "Authorization": f"Bearer {personal_access_token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    user_id = data.get("id")
    if user_id is not None:
        print("Your GitHub ID:", user_id)
    else:
        print("Unable to fetch GitHub ID")
else:
    print("Error:", response.status_code)
