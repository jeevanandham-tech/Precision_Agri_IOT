#include <DHT.h>
#define DHTPIN 2     // DHT sensor pin
#define DHTTYPE DHT22   // DHT 22

DHT dht(DHTPIN, DHTTYPE);

const int moisturePin = A0; // Soil moisture sensor pin
const int ldrPin = A1;       // Light sensor pin
const int relayPin = 3;      // Relay module pin

void setup() {
    Serial.begin(9600);
    dht.begin();
    pinMode(relayPin, OUTPUT);
    digitalWrite(relayPin, LOW); // Turn off the relay initially
}

void loop() {
    // Read sensors
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();
    int moistureLevel = analogRead(moisturePin);
    int lightLevel = analogRead(ldrPin);

    // Print sensor values
    Serial.print("Humidity: "); Serial.print(humidity);
    Serial.print(" %\tTemperature: "); Serial.print(temperature);
    Serial.print(" *C\tMoisture Level: "); Serial.print(moistureLevel);
    Serial.print("\tLight Level: "); Serial.println(lightLevel);

    // Control irrigation based on moisture level
    if (moistureLevel < 300) { // Threshold value for soil moisture
        digitalWrite(relayPin, HIGH); // Turn on the water pump
    } else {
        digitalWrite(relayPin, LOW); // Turn off the water pump
    }

    delay(2000); // Wait for 2 seconds before the next loop
}
