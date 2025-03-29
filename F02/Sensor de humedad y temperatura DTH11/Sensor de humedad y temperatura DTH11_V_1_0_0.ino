#include <DHT.h>
#include <DHT_U.h>

// Definir el pin y tipo de sensor
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600); // Iniciar comunicación serial
    dht.begin(); // Iniciar el sensor
}

void loop() {
    float temperatura = dht.readTemperature(); // Leer temperatura en grados Celsius
    float humedad = dht.readHumidity(); // Leer humedad

    if (isnan(temperatura) || isnan(humedad)) {
        Serial.println("Error: No se pudo leer el sensor");
        return;
    }

    // Enviar los datos en formato fácil de procesar en Python
    Serial.print(temperatura);
    Serial.print(",");
    Serial.println(humedad);

    delay(2000); // Esperar 2 segundos antes de la siguiente lectura
}
