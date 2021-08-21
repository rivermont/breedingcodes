#!/usr/bin/env python3

import requests
import json

codes = {"": 0,
         "F": 1,
         "H": 2,
         "S": 3,
         "S7": 4,
         "M": 5,
         "P": 6,
         "C": 7,
         "T": 8,
         "N": 9,
         "A": 10,
         "B": 10.5,
         "PE": 11,
         "CN": 12,
         "NB": 13,
         "DD": 14,
         "UN": 15,
         "ON": 16,
         "FL": 17,
         "CF": 18,
         "FY": 19,
         "FS": 20,
         "NE": 20,
         "NY": 20
         }

location = ""
species = ""
url = f"https://ebird.org/mapServices/getLocInfo.do?fmt=json&locID={location}&speciesCodes={species}"

response = requests.get(url).text
# print(response)
data1 = json.loads(response)['infoList']
data2 = []

for i in data1:
    a = {}
    a["date"] = i["obsDt"]
    try:
        a["num"] = int(i["howMany"])
    except ValueError:  # X given for abundance
        a["num"] = 1
    try:
        a["bcode"] = codes[i["evidence"]]
    except KeyError:
        a["bcode"] = 1
    data2.append(a)

print(data2)

