# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import time
import random
import RPi.GPIO as GPIO

# Configuración de pines
ping_pin = 7
red = 11
blue = 10
green = 9

# Inicialización GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def microseconds_to_inches(microseconds):
    return microseconds / 74 / 2

def microseconds_to_centimeters(microseconds):
    return microseconds / 29 / 2

def get_distance():
    GPIO.setup(ping_pin, GPIO.OUT)
    GPIO.output(ping_pin, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(ping_pin, GPIO.HIGH)
    time.sleep(0.000005)
    GPIO.output(ping_pin, GPIO.LOW)
    
    GPIO.setup(ping_pin, GPIO.IN)
    
    # Simulación de lectura (reemplazar con implementación real)
    start_time = time.time()
    while GPIO.input(ping_pin) == GPIO.LOW:
        if time.time() - start_time > 0.1:
            return 0
    
    start_time = time.time()
    while GPIO.input(ping_pin) == GPIO.HIGH:
        pulse_duration = (time.time() - start_time) * 1000000
        if pulse_duration > 10000:
            return 0
    
    return pulse_duration

def main():
    try:
        while True:
            duration = get_distance()
            
            inches = microseconds_to_inches(duration)
            cm = microseconds_to_centimeters(duration)
            
            print(f"{inches:.2f}in, {cm:.2f}cm")
            
            if inches < 10:
                GPIO.output(red, GPIO.HIGH)
                GPIO.output(green, GPIO.LOW)
                GPIO.output(blue, GPIO.LOW)
            elif 10 <= inches < 50:
                GPIO.output(red, GPIO.LOW)
                GPIO.output(green, GPIO.LOW)
                GPIO.output(blue, GPIO.HIGH)
            else:
                GPIO.output(red, GPIO.LOW)
                GPIO.output(green, GPIO.HIGH)
                GPIO.output(blue, GPIO.LOW)
                
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Programa detenido")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()

