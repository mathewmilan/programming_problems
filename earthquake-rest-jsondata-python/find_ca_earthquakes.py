#!/usr/bin/env python3

import json
import requests
import datetime as DT
from operator import itemgetter
import pprint

#USGS JSON feed for all domestic earthquakes from past week
URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

#Load earthquake data for the past week from the USGS url
#Returns a list of earthquake incidents (key-value pairs)
def get_data_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    parsed_data = json.loads(response.text)
    pprint.pprint(parsed_data)
    return parsed_data['features']

#Filter earthquakes in California
#Returns a list of earthquakes in CA
def get_earthquakes_in_cali(quake_list):
    ca_quakes = []
    for quake in quake_list:
        if (quake['properties']['place'].find('California') > 0):
            ca_quakes.append(quake['properties'])
        elif (quake['properties']['place'].find('CA') > 0):
            ca_quakes.append(quake['properties'])
#    pprint.pprint(ca_quakes)
    return ca_quakes

#Sort the Earthquakes in California by time
#Display Time, Place and Magnitude from the Sorted List
def sort_print_earthquakes(quake_list):
    quake_sorted = sorted(quake_list, key=itemgetter('time'))
    for quake in quake_sorted:
        time_stamp = DT.datetime.utcfromtimestamp(quake['time']//1000).isoformat()
        print("%s | %s | Magnitude: %s" % (time_stamp, quake['place'], quake['mag']))
    return 


quake_features = get_data_from_url(URL)
#ca_quakes = get_earthquakes_in_cali(quake_features)
#sort_print_earthquakes (ca_quakes)