from __future__ import print_function

import json
from random import choice
from itertools import product

import requests

set_url = 'http://stark-oasis-75010.herokuapp.com/set'
get_url = 'http://stark-oasis-75010.herokuapp.com/get'

# [(0, 0, 0),
#  (0, 0, 127),
#  (0, 0, 255),
#  (0, 127, 0),
#  (0, 127, 127),
#  (0, 127, 255),
#  ...
#  (255, 255, 0),
#  (255, 255, 127),
#  (255, 255, 255)]
colours = list(product(*(((0, 127, 255),)*3)))

data = json.dumps(choice(colours))
print('POST', set_url, data)
requests.post(set_url, data)

print('GET', get_url, requests.get(get_url).text)
