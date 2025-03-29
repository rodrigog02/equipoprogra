# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 23:10:28 2025

@author: AxelR9
"""

import RPi.GPIO as GPIO
import time

sensor_pin = 2
led_pin = GPIO.BCM_LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        sensor_state = GPIO.input(sensor_pin)
        
        if sensor_state == GPIO.HIGH:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)
            
        time.sleep(0.01)

except KeyboardInterrupt:
    pass
    
finally:
    GPIO.cleanup()