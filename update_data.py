#! /usr/bin/python3

import requests
import git

base_url = "https://covidtracking.com/"

for endpoint, file in [("api/v1/states/current.json", "states_current.json"),
                       ("api/v1/states/daily.json", "states_history.json"),
                       ("api/v1/us/current.json", "us_current.json"),
                       ("api/us/daily", "us_history.json"),
                      ]:
    url = base_url + endpoint
    r = requests.get(url)
    #j = r.json
    with open(file, 'w') as outfile:
        outfile.write(r.text)

        
g = git.cmd.Git("../covid-19-data")
g.pull()