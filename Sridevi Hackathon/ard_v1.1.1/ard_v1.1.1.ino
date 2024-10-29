#include <Arduino.h>

const int sensorPin = A0;  // Analog pin connected to LM35
const int buzzerPin = 2;   // Digital pin connected to the buzzer

void setup() {
  Serial.begin(9600);  // Initialize serial communication with ESP
  pinMode(buzzerPin, OUTPUT);

  // Buzzer startup sound
  for (int i = 0; i < 2; i++) {
    tone(buzzerPin, 1000); // Start a 1 kHz tone
    delay(100);            // Sound duration
    noTone(buzzerPin);     // Stop the tone
    delay(100);            // Pause between beeps
  }
}

void loop() {
  int sensorValue = analogRead(sensorPin);           // Read analog value from LM35
  float voltage = sensorValue * (5.0 / 1023.0);      // Convert ADC reading to voltage
  float temperature = voltage * 100.0;               // Convert voltage to temperature (LM35 outputs 10mV per °C)

  // Send temperature data with a prefix
  Serial.print("TEMP:");
  Serial.println(temperature);

  delay(2000);  // Delay between readings (adjust as needed)
}
