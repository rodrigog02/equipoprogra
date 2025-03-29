#version 1.0.0
import serial
import time

# Configuración del puerto serie
PUERTO_SERIE = 'COM3'  # Cambia esto según el puerto en Windows 
VELOCIDAD = 9600

try:
    ser = serial.Serial(PUERTO_SERIE, VELOCIDAD, timeout=1)
    time.sleep(2)  # Esperar a que la conexión esté lista
    print(f"Conectado a {PUERTO_SERIE}")
except Exception as e:
    print(f"Error al conectar con el puerto {PUERTO_SERIE}: {e}")
    exit()

while True:
    try:
        # Leer línea del puerto serie
        linea = ser.readline().decode('utf-8').strip()

        # Verificar que no esté vacía y procesar datos
        if linea and "Error" not in linea:
            temperatura, humedad = map(float, linea.split(","))
            print(f" Temperatura: {temperatura} °C  | Humedad: {humedad} %")
        else:
            print("Error en la lectura del sensor.")

        time.sleep(2)  # Esperar 2 segundos para la próxima lectura

    except Exception as e:
        print(f"Error al leer datos: {e}")
        break

# Cerrar el puerto serie al terminar
ser.close()
print("Puerto serial cerrado.")
