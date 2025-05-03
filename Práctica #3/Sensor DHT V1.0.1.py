import Adafruit_DHT
import time

# Elegir el tipo de sensor: DHT11 o DHT22
sensor = Adafruit_DHT.DHT22  # Usa DHT11 si es ese tu modelo

# Pin GPIO donde está conectado el sensor
pin = 4  # GPIO4 (pin físico 7 en la Raspberry Pi)

print("Iniciando lectura del sensor DHT...")

while True:
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

    if humedad is not None and temperatura is not None:
        print(f"Temperatura: {temperatura:.1f} °C")
        print(f"Humedad: {humedad:.1f} %")
    else:
        print("Fallo al leer datos del sensor. Intentando de nuevo...")

    time.sleep(2)
