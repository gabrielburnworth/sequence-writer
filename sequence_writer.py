#!/usr/bin/env python

"""Python Celery Script sequence writer."""

from __future__ import print_function
import sequence_commands


class Sequence:
    def __init__(self, name='New Sequence', color='gray', post=print):
        self.sequence = {
            'name': name,
            'color': color,
            'body': []
            }
        self.add = self.sequence['body'].append
        self.post = post

    def __enter__(self):
        return self

    def move_absolute(self, **kwargs):
        self.add(sequence_commands.move_absolute(**kwargs))

    def move_relative(self, **kwargs):
        self.add(sequence_commands.move_relative(**kwargs))

    def send_message(self, **kwargs):
        self.add(sequence_commands.send_message(**kwargs))

    def find_home(self, **kwargs):
        self.add(sequence_commands.find_home(**kwargs))

    def if_statement(self, **kwargs):
        self.add(sequence_commands.if_statement(**kwargs))

    def write_pin(self, **kwargs):
        self.add(sequence_commands.write_pin(**kwargs))

    def read_pin(self, **kwargs):
        self.add(sequence_commands.read_pin(**kwargs))

    def execute_sequence(self, **kwargs):
        self.add(sequence_commands.execute_sequence(**kwargs))

    def execute_script(self, **kwargs):
        self.add(sequence_commands.execute_script(**kwargs))

    def wait(self, **kwargs):
        self.add(sequence_commands.wait(**kwargs))

    def take_photo(self, **kwargs):
        self.add(sequence_commands.take_photo(**kwargs))

    def __exit__(self, *args):
        self.post(self.sequence)


if __name__ == '__main__':
    # Print unformatted sequence
    with Sequence("my sequence", "green") as s:
        s.move_relative(distance=(100, 100, 0))
        s.wait(milliseconds=1000)
        s.take_photo()

    # Print formatted sequence
    import json

    def print_json(sequence):
        print(json.dumps(sequence, indent=2, sort_keys=False))

    with Sequence("my sequence", "green", print_json) as s:
        s.move_relative(distance=(100, 100, 0))
        s.wait(milliseconds=1000)
        s.take_photo()

    # Save sequence to file
    def save_as_file(sequence):
        with open('my_sequence.json', 'w') as sequence_file:
            json.dump(sequence, sequence_file)

    with Sequence("my sequence", "green", save_as_file) as s:
        s.move_relative(distance=(100, 100, 0))
        s.wait(milliseconds=1000)
        s.take_photo()

    # Upload sequence
    import requests

    def upload(sequence):
        r = requests.post("http://httpbin.org/post", data=json.dumps(sequence))
        print(r, r.json())

    with Sequence("my sequence", "green", upload) as s:
        s.move_relative(distance=(100, 100, 0))
        s.wait(milliseconds=1000)
        s.take_photo()
