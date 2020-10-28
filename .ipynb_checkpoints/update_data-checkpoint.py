#! /usr/bin/python3

import requests
import git

base_url = "https://api.covidtracking.com/"

for endpoint, file in [("v1/states/current.json", "states_current.json"),
                       ("v1/states/daily.json", "states_history.json"),
                       ("v1/us/current.json", "us_current.json"),
                       ("v1/us/daily.json", "us_history.json"),
                      ]:
    url = base_url + endpoint
    r = requests.get(url)
    #j = r.json
    with open(file, 'w') as outfile:
        outfile.write(r.text)

        
g = git.cmd.Git("../covid-19-data")
g.pull()