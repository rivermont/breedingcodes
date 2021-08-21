#!/usr/bin/env python3

import requests
import json

location = ""
species = ""
url = f"https://ebird.org/mapServices/getLocInfo.do?fmt=json&locID={location}&speciesCodes={species}"

response = requests.get(url).text
# print(response)
data = json.loads(response)['infoList']

print(data)

