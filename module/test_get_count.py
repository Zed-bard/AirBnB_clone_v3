#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from module import storage
from module.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
