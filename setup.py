#!/bin/python

from evdev import *
from evdev import ecodes as e
import json
devices = [InputDevice(path) for path in list_devices()]
#print(devices[0].name)
def gen_JSON():
    j_devs = ["devices"]
    for device in devices:
        j_devs.append({"name": device.name, "path": device.path})

    with open("deffs.json", "w") as write_file:
        json.dump(j_devs, write_file)

def read_JSON():
    with open("deffs.json", "r") as file:
        dat = json.load(file)
        print('hi')
