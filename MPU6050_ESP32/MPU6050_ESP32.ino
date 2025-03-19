#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

// Variables to store gyroscope values and angles
int16_t gx, gy, gz;
float angleX = 0, angleY = 0, angleZ = 0;
unsigned long lastTime = 0; // Time tracking for calculating delta time

void setup() {
  Wire.begin();
  mpu.initialize();
  Serial.begin(9600);  // Initialize serial communication for printing gyro values and angles
}

void loop() {
  unsigned long currentTime = millis();
  float deltaTime = (currentTime - lastTime) / 1000.0;  // Calculate time difference in seconds
  lastTime = currentTime;

  // Get gyroscope data (angular velocity in degrees per second)
  mpu.getRotation(&gx, &gy, &gz);

  // Integrate the gyroscope readings to estimate angles
  angleX += gx * deltaTime;  // Integrate gx over time to get the angle for X
  angleY += gy * deltaTime;  // Integrate gy over time to get the angle for Y
  angleZ += gz * deltaTime;  // Integrate gz over time to get the angle for Z

  // Print the gyro readings and estimated angles for X, Y, Z axes
  Serial.print("Gyro X: ");
  Serial.print(gx);
  Serial.print(" | Angle X: ");
  Serial.print(angleX);
  Serial.print(" | Gyro Y: ");
  Serial.print(gy);
  Serial.print(" | Angle Y: ");
  Serial.print(angleY);
  Serial.print(" | Gyro Z: ");
  Serial.print(gz);
  Serial.print(" | Angle Z: ");
  Serial.println(angleZ);

  delay(100);  // Small delay for readability
}
