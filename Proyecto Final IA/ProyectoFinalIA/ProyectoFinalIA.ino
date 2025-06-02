#include <DHT.h>

#define DHTPIN 2          // Pin donde está conectado el DHT11
#define DHTTYPE DHT11     // Tipo de sensor DHT
#define MQ135PIN A0       // Pin analógico donde está conectado MQ-135

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // Leer temperatura y humedad
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  // Leer MQ-135 (lectura cruda)
  int mqRaw = analogRead(MQ135PIN);

  // Suponiendo que tus lecturas reales están entre 900 y 950, las escalamos a 300-600
  int mqScaled = map(mqRaw, 900, 950, 300, 600);

  // Limitar valores escalados al rango 300-600 para evitar valores fuera de rango
  if (mqScaled < 300) mqScaled = 300;
  if (mqScaled > 600) mqScaled = 600;

  // Verificar que temp y hum son válidos (dht puede dar NAN)
  if (isnan(temp) || isnan(hum)) {
    Serial.println("Error leyendo DHT11");
  } else {
    // Enviar datos por serial separados por comas
    Serial.print(temp, 2);
    Serial.print(",");
    Serial.print(hum, 2);
    Serial.print(",");
    Serial.println(mqScaled);
  }

  delay(10000);  // Esperar 10 segundos
}

