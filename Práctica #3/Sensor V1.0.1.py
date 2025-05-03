from machine import Pin, time_pulse_us
from time import sleep_us, sleep

# Pines asignados (ajústalos si usas otros en tu placa)
pingPin = Pin(7, Pin.OUT)  # Trigger pin (también se usa como echo)
red = Pin(11, Pin.OUT)
blue = Pin(10, Pin.OUT)
green = Pin(9, Pin.OUT)

def get_distance_cm():
    # Enviar pulso de activación
    pingPin.init(Pin.OUT)
    pingPin.value(0)
    sleep_us(2)
    pingPin.value(1)
    sleep_us(5)
    pingPin.value(0)

    # Leer tiempo del pulso de respuesta
    pingPin.init(Pin.IN)
    try:
        duration = time_pulse_us(pingPin, 1, 30000)  # Espera hasta 30 ms
    except OSError:
        return -1  # Error de lectura

    cm = (duration / 2) / 29
    return cm

while True:
    distance_cm = get_distance_cm()
    inches = distance_cm / 2.54

    print("{:.2f}in, {:.2f}cm".format(inches, distance_cm))

    # Control de LEDs según la distancia
    if inches < 10:
        red.value(1)
        green.value(0)
        blue.value(0)
    elif 10 < inches < 50:
        red.value(0)
        green.value(0)
        blue.value(1)
    else:
        red.value(0)
        green.value(1)
        blue.value(0)

    sleep(0.5)
