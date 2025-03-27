#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <BluetoothSerial.h>

// PCA9685 Servo Driver
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40);

// Bluetooth Serial for ESP32
BluetoothSerial SerialBT;

// Servo Min/Max PWM values
#define SERVOMIN  125  // Minimum pulse length
#define SERVOMAX  575  // Maximum pulse length

// Servo channel mappings (PCA9685 channels 1-4)
#define SERVO_BASE       0
#define SERVO_SHOULDER   1
#define SERVO_ELBOW      2
#define SERVO_GRIPPER    3

unsigned char Data_String[25], Data_Index = 0, New_Data_Rec_Flag = 0;
unsigned int Received_Servo_Value[4];

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ROBOTIC ARM");  // Bluetooth name

  // Initialize PCA9685 Servo Driver
  pwm.begin();
  pwm.setPWMFreq(60);  // Set frequency to 60Hz (typical for servos)

  Serial.println("ESP32 Bluetooth Robot Arm with PCA9685 Ready");
}

// Convert angle (0-180°) to PWM pulse (SERVOMIN-SERVOMAX)
int angleToPulse(int ang) {
   return map(ang, 0, 180, SERVOMIN, SERVOMAX);
}

void moveServo(int channel, int angle) {
  int pulse = angleToPulse(angle);
  pwm.setPWM(channel, 0, pulse);
  Serial.printf("Servo %d set to angle %d (pulse: %d)\n", channel, angle, pulse);
}

void loop() {
  if (SerialBT.available()) {
    char incomingChar = SerialBT.read();
    if (incomingChar == '\n') {  // End of data marker
      New_Data_Rec_Flag = 1;
      Data_String[Data_Index] = '\0';
      Data_Index = 0;
    } else {
      Data_String[Data_Index++] = incomingChar;
    }
  }

  if (New_Data_Rec_Flag) {
    New_Data_Rec_Flag = 0;

    // Parse received data (format: "90,120,60,45#")
    sscanf((char *)Data_String, "%d,%d,%d,%d", &Received_Servo_Value[0], 
           &Received_Servo_Value[1], &Received_Servo_Value[2], &Received_Servo_Value[3]);

    // Print received servo values
    Serial.print("Received Data: ");
    Serial.print("Base: ");
    Serial.print(Received_Servo_Value[0]);
    Serial.print(", Shoulder: ");
    Serial.print(Received_Servo_Value[1]);
    Serial.print(", Elbow: ");
    Serial.print(Received_Servo_Value[2]);
    Serial.print(", Gripper: ");
    Serial.println(Received_Servo_Value[3]);

    // Move servos
    moveServo(SERVO_BASE, Received_Servo_Value[0]);
    moveServo(SERVO_SHOULDER, Received_Servo_Value[1]);
    moveServo(SERVO_ELBOW, Received_Servo_Value[2]);
    moveServo(SERVO_GRIPPER, Received_Servo_Value[3]);
  }
}
