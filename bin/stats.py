#!/usr/bin/env python
"""
Half finished script for grabbing info from the jenkins api
Copyright 2019 Tyler Cipriani <tyler@tylercipriani.com>; GPLv3
"""

import os
import re
import sys

import requests

JENKINS = 'https://integration.wikimedia.org/ci'

r = requests.get(os.path.join(JENKINS, 'api/json?tree=jobs[name]'))
r.raise_for_status()
jobs = r.json()
for job in jobs['jobs']:
    job_api = os.path.join(
        JENKINS,
        'job',
        job['name'],
        'api/json?tree=allBuilds[id,timestamp,result,duration,actions[parameters[name,value]],builtOn]')
    r = requests.get(job_api)
    r.raise_for_status()

    for build in r.json()['allBuilds']:
        if not build.get('result'):
            continue
        try:
            print([y.get('value') for y in [x for x in build['actions'] if x.get('parameters')][0]['parameters']])
        except:
            print(build)
            raise
