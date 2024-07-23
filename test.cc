#include <Arduino.h>

#define TRIG_PIN 9
#define ECHO_PIN 10

float calculateHeight(float distanceCm) {
  // Linear interpolation between the given points
  if (distanceCm >= 20 && distanceCm <= 50) {
    return 170 + (distanceCm - 20) * (199 - 170) / (50 - 20);
  } else {
    return -1; // Return -1 if the distance is out of the expected range
  }
}

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  long duration;
  float distanceCm, heightCm, heightFeet, heightInches;

  // Clear the trigPin
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  // Set the trigPin on HIGH state for 10 microseconds
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Read the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(ECHO_PIN, HIGH);

  // Calculate the distance in centimeters
  distanceCm = (duration * 0.034) / 2;

  // Calculate the height based on the distance
  heightCm = calculateHeight(distanceCm);

  // Convert height to feet and inches
  heightFeet = heightCm / 30.48;
  heightInches = heightCm / 2.54;

  // Print the distance and height
  Serial.print("Distance: ");
  Serial.print(distanceCm);
  Serial.print(" cm, Height: ");
  if (heightCm != -1) {
    Serial.print(heightCm);
    Serial.print(" cm, ");
    Serial.print(heightFeet, 2); // Print feet with 2 decimal places
    Serial.print(" ft, ");
    Serial.print(heightInches, 2); // Print inches with 2 decimal places
    Serial.println(" in");
  } else {
    Serial.println("Out of range");
  }

  delay(1000); // Wait for a second before the next measurement
}