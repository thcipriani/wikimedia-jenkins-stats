#!/usr/bin/env python3

from datetime import datetime

import requests

URL = 'https://integration.wikimedia.org/ci/computer/api/json?tree=computer[displayName,loadStatistics[busyExecutors[hour[latest]]]]'

r = requests.get(URL)
r.raise_for_status()


for computer in r.json()['computer']:
    if not computer['displayName'].startswith('integration-slave-docker-'):
        continue
    print('{}\t{}\t{}'.format(
        datetime.utcnow(),
        computer['displayName'],
        computer['loadStatistics']['busyExecutors']['hour']['latest']
    ))
