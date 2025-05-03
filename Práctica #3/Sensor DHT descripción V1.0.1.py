import Adafruit_DHT
📌 Importa la librería de Adafruit para usar sensores DHT11/DHT22. Esta librería ya tiene funciones listas para comunicarte con el sensor.

import time
📌 Importa el módulo time para poder usar sleep, que permite hacer pausas entre lecturas (por ejemplo, 2 segundos).

sensor = Adafruit_DHT.DHT22
📌 Indica el tipo de sensor que estás usando.
Si tienes un DHT11, cambia esta línea a:

sensor = Adafruit_DHT.DHT11
pin = 4
📌 Define el número del pin GPIO (en este caso, GPIO4) al que conectaste el cable de datos del sensor.
Este no es el número del pin físico, sino el número GPIO lógico de la Raspberry.

print("Iniciando lectura del sensor DHT...")
📌 Muestra un mensaje inicial para indicar que comienza el proceso.

while True:
📌 Inicia un bucle infinito: el código dentro de este bloque se repetirá una y otra vez.

    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
📌 Esta es la función más importante:

read_retry() intenta leer los datos del sensor hasta 15 veces automáticamente si falla al principio.

Devuelve dos valores:

humedad → porcentaje de humedad relativa (%)

temperatura → grados Celsius (°C)

    if humedad is not None and temperatura is not None:
📌 Verifica si la lectura fue exitosa. Si ambos valores no son None, significa que la lectura fue correcta.


        print(f"Temperatura: {temperatura:.1f} °C")
        print(f"Humedad: {humedad:.1f} %")
📌 Imprime los valores de temperatura y humedad.

:.1f significa que se muestra solo un decimal (ej: 23.4 °C).

    else:
        print("Fallo al leer datos del sensor. Intentando de nuevo...")
📌 Si la lectura falló (uno o ambos valores son None), se imprime un mensaje de error.

    time.sleep(2)
📌 Espera 2 segundos antes de hacer otra lectura, para no saturar el sensor.
