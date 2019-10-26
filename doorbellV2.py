#!/usr/bin/python3

import requests
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
countdown = 0
INPUT_PIN = 17
url = 'http://example.com/api/doorbell'

GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button_press(channel):
  global countdown
  state = -1
  if countdown == 0:
    print("countdown is 0")
    state = GPIO.input(channel)
    print("reading pin state: %s"%(state))
    if state == 1:
      print('url: %s'%(url))
      req = requests.post(url, data = "on", headers={"Content-type": "text/plain", "Accept-Encoding":""})
      if req.status_code != requests.codes.ok:
        req.raise_for_status()
        countdown = 5
      return

GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH, callback=button_press, bouncetime=1)

try:
  while True:
    if countdown > 0:
      countdown = countdown - 1;
      sleep(1);

finally:
  GPIO.cleanup()
