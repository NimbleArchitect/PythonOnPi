#!/usr/bin/python3

import requests
import RPi.GPIO as GPIO

input_pin = 27
url = 'http://example.com/api/frontdoor'

GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def button_press(channel):
    state = GPIO.input(channel)
    if state == 1:
        req = requests.post(url, data = "on", headers = {"Content-type": "text/plain", "Accept-Encoding":""})
    return

GPIO.add_event_detect(input_pin, GPIO.BOTH, callback = button_press, bouncetime = 1)

try:
    while True:
        pass
finally:
    GPIO.cleanup()
