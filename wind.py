#!/bin/python

import PySimpleGUI as sg
from evdev import *
from evdev import ecodes as e

keys = []

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Select Keys:')],
            [sg.Checkbox('Trigger', default=True), sg.Checkbox('Thumb'), sg.Checkbox('Thumb2')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Define Virtual GamePad', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    if values[0] == True:
        keys.append("BTN_TRIGGER")
    if values[1] == True:
        keys.append("BTN_THUMB")
    if values[2] == True:
        keys.append("BTN_THUMB2")
    print(keys)
    break
window.close()

layout = [  [sg.Text('Selected Keys')],
            [sg.Text(keys)],
            #[sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Define Virtual GamePad', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
window.close()
