#!/bin/python

from evdev import *
from evdev import ecodes as e
import selectors
import setup as st
import json
#Store the Identity of the devices used, and grabs then (only recipient)
controls = [InputDevice('/dev/input/event8'), InputDevice('/dev/input/event9')]
selector = selectors.DefaultSelector()

for i in range(0,len(controls)):
    controls[i].grab()
    selector.register(controls[i], selectors.EVENT_READ)




#Specifying virtual device options
keys = {
    e.EV_KEY : [288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299],
    e.EV_ABS : [
        (e.ABS_X, AbsInfo(value=0, min=0, max=1023, fuzz=0, flat=0, resolution=0)),
        (e.ABS_Y, AbsInfo(0, 0, 1023, 0, 0, 0)),
        (e.ABS_RZ, AbsInfo(0, 0, 255, 0, 0, 0)),
        (e.ABS_THROTTLE, AbsInfo(0, 0, 255, 0, 0, 0))
    ]
}
#Create virtual device
ui = UInput(keys, name="VirtualPad", version=0x3)
#parsed = json.loads('"{0}"'.format(ui.capabilities()))
#print(json.dumps(ui.capabilities(), indent=8, separators=(',', ':')))
def map(val, in_min, in_max, out_min, out_max):
    return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    for key, mask in selector.select():
        device = key.fileobj
        for event in device.read():
            print(event)
            if device.name == controls[0].name and event.type == e.EV_ABS and not event.code == e.ABS_THROTTLE:
                ui.write(event.type, event.code, event.value)
                ui.syn()
            if device.name == controls[1].name and event.type == e.EV_ABS and (event.code == 1 or event.code == 2):
                if event.code == 1:
                    val = map(event.value, 0, 255, 255, 127)
                elif event.code == 2:
                    val = map(event.value, 0, 255, 0, 127)
                ui.write(event.type, e.ABS_THROTTLE, val)
                ui.syn()
            if device.name == controls[0].name and event.type == e.EV_KEY:
                ui.write(event.type, event.code, event.value)
                ui.syn()
