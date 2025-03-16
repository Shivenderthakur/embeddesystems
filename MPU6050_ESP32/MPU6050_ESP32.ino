#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  while (!Serial)
    delay(10); // Wait for Serial Monitor to open

  // Initialize I2C communication
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  // Set accelerometer range to +/- 2G
  mpu.setAccelerometerRange(MPU6050_RANGE_2_G);
  // Set gyroscope range to +/- 250 degrees per second
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  // Set filter bandwidth to 5Hz
  mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);

  delay(100);
}

void loop() {
  // Get new sensor events
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Print accelerometer values
  Serial.print("Accel X: "); Serial.print(a.acceleration.x); Serial.print(" m/s^2, ");
  Serial.print("Y: "); Serial.print(a.acceleration.y); Serial.print(" m/s^2, ");
  Serial.print("Z: "); Serial.print(a.acceleration.z); Serial.println(" m/s^2");

  // Print gyroscope values
  Serial.print("Gyro X: "); Serial.print(g.gyro.x); Serial.print(" rad/s, ");
  Serial.print("Y: "); Serial.print(g.gyro.y); Serial.print(" rad/s, ");
  Serial.print("Z: "); Serial.print(g.gyro.z); Serial.println(" rad/s");

  // Print temperature
  Serial.print("Temperature: "); Serial.print(temp.temperature); Serial.println(" degC");

  Serial.println("");
  delay(500);
}
