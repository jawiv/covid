#! /usr/bin/python3

import requests

base_url = "https://covidtracking.com/"

for endpoint, file in [("api/states", "states_current.json"),
                       ("api/states/daily", "states_history.json"),
                       ("api/us", "us_current.json"),
                       ("api/us/daily", "us_history.json"),
                      ]:
    url = base_url + endpoint
    r = requests.get(url)
    #j = r.json
    with open(file, 'w') as outfile:
        outfile.write(r.text)
