#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.dates as dates
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

location = ""  # must be personal/hotspot locID, not region code
species = ""
portal = "atlasnc"
byr = "2020"  # required by some portals?
url = f"https://ebird.org/{portal}/mapServices/getLocInfo.do?fmt=json&byr={byr}&locID={location}&speciesCodes={species}"

response = requests.get(url).text
# print(response)
response = json.loads(response)['infoList']
data = []

# create new dataset with only the needed variables
for i in response:
    a = {}
    a["date"] = i["obsDt"]
    # try:
        # a["num"] = int(i["howMany"])
    # except ValueError:  # X given for abundance
        # a["num"] = 1
    try:
        a["bcode"] = codes[i["breedingCode"]]
    except KeyError:  # Observed but without breeding code
        a["bcode"] = 1
    data.append(a)

del response


# Plotting

x = [dates.datestr2num(i["date"]) for i in data]

y = [i["bcode"] for i in data]

plt.scatter(x, y)
plt.show()

