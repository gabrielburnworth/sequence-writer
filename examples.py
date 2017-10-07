#!/usr/bin/env python

"""Sequence Writer usage examples."""

from sequence_writer import Sequence


# Print unformatted sequence
with Sequence("my sequence", "green") as s:
    s.move_relative(distance=(100, 100, 0))
    s.wait(milliseconds=1000)
    s.take_photo()

"""
# Result:

{'color': 'green', 'body': [{'kind': 'move_relative', 'args': {'y': 100,
'x': 100, 'z': 0, 'speed': 100}}, {'kind': 'wait', 'args': {'milliseconds':
1000}}, {'kind': 'take_photo', 'args': {}}], 'name': 'my sequence'}

"""


# Print formatted sequence
import json

def print_json(sequence):
    print(json.dumps(sequence, indent=2, sort_keys=False))

with Sequence("my sequence", "green", print_json) as s:
    s.move_relative(distance=(100, 100, 0))
    s.wait(milliseconds=1000)
    s.take_photo()

# Result
"""
{
  "name": "my sequence",
  "color": "green",
  "body": [
    {
      "kind": "move_relative",
      "args": {
        "y": 100,
        "x": 100,
        "z": 0,
        "speed": 100
      }
    },
    {
      "kind": "wait",
      "args": {
        "milliseconds": 1000
      }
    },
    {
      "kind": "take_photo",
      "args": {}
    }
  ]
}
"""


# Save sequence to file
def save_as_file(sequence):
    with open('my_sequence.json', 'w') as sequence_file:
        json.dump(sequence, sequence_file)

with Sequence("my sequence", "green", save_as_file) as s:
    s.move_relative(distance=(100, 100, 0))
    s.wait(milliseconds=1000)
    s.take_photo()

# Result: my_sequence.json file saved


# Upload sequence
import requests

def upload(sequence):
    r = requests.post("http://httpbin.org/post", data=json.dumps(sequence))
    print(r, r.json())

with Sequence("my sequence", "green", upload) as s:
    s.move_relative(distance=(100, 100, 0))
    s.wait(milliseconds=1000)
    s.take_photo()

# Result:
# <Response [200]> {<POST data>}
