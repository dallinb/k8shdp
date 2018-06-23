#!/bin/env python
"""kibana_import_indexes.py.

A script to extract a list of indeces from Elasticseach and add to
Kibana.
"""
import json
import re
import requests
import urllib
import socket


def get_ip():
    """Get the IP address of the local node."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

url = "http://localhost:9200/_aliases"
response = urllib.urlopen(url)
data = json.loads(response.read())

for index in data.keys():
    if index == '.kibana':
        continue
    index = re.sub('[0-9][0-9][0-9][0-9].[0-9][0-9].[0-9][0-9]$', '*', index)
    data = {'title': index}
    url = 'http://%s:5601/es_admin/.kibana/index-pattern/%s/_create'
    url = url % (get_ip(), index)
    headers = {'content-type': 'application/json'}
    headers['kbn-xsrf'] = "anything"
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print response
