from machine import Pin
import time

# Configura el pin GP2 como entrada para el sensor
sensor = Pin(2, Pin.IN)

# Configura el pin GP25 (LED incorporado) como salida
led = Pin(25, Pin.OUT)

while True:
    # Lee el estado del sensor
    sensor_state = sensor.value()
    
    # Enciende o apaga el LED dependiendo del estado del sensor
    if sensor_state == 1:
        led.value(1)  # Encender LED
    else:
        led.value(0)  # Apagar LED

    # Espera 10 milisegundos
    time.sleep(0.01)
