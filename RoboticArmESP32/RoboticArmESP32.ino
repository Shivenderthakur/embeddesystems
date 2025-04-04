
#include <ESP32Servo.h>
#include <BluetoothSerial.h>

#define SERVO_BASE            25
#define SERVO_SHOULDER        26
#define SERVO_ELBOW           27
#define SERVO_GRIPPER         33

BluetoothSerial SerialBT; // Create BluetoothSerial object

Servo myservo_1;  // Servo for base movement
Servo myservo_2;  // Servo for shoulder movement
Servo myservo_3;  // Servo for elbow movement
Servo myservo_4;  // Servo for gripper control

unsigned char Data_String[25], Data_Index = 0, New_Data_Rec_Flag = 0;
unsigned int Received_Servo_Value[4], Final_Servo_Val[4];
unsigned char Index_i = 0, Index_j = 0, Counter_to_Refresh = 0;

void setup() {
  Serial.begin(9600);  // Initialize Serial Monitor communication
  SerialBT.begin("ROBOARM"); // Set the Bluetooth device name

  myservo_1.attach(SERVO_BASE);       
  myservo_2.attach(SERVO_SHOULDER);   
  myservo_3.attach(SERVO_ELBOW);      
  myservo_4.attach(SERVO_GRIPPER);    
  myservo_1.write(90);
  delay(200);
  myservo_2.write(90);
  delay(200);
  myservo_3.write(90);
  delay(200);
  myservo_4.write(90);
  delay(200);

  Received_Servo_Value[0] = 90;     // Default values
  Received_Servo_Value[1] = 90;
  Received_Servo_Value[2] = 90;
  Received_Servo_Value[3] = 45;
  
  Final_Servo_Val[0] = 90;          // Default values
  Final_Servo_Val[1] = 90;
  Final_Servo_Val[2] = 90;
  Final_Servo_Val[3] = 45;
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

    // Print received values to Serial Monitor
    Serial.print("Received Data: ");
    Serial.print("Base: ");
    Serial.print(Received_Servo_Value[0]);
    Serial.print(", Shoulder: ");
    Serial.print(Received_Servo_Value[1]);
    Serial.print(", Elbow: ");
    Serial.print(Received_Servo_Value[2]);
    Serial.print(", Gripper: ");
    Serial.println(Received_Servo_Value[3]);


}

  Counter_to_Refresh++;
  delay(1);
  if (Counter_to_Refresh >= 10) {    // delay of 10 msec = 1 msec * 10, this will allow smooth movement of servos
    Counter_to_Refresh = 0;
    // Update base servo position
    if (Received_Servo_Value[0] != Final_Servo_Val[0]) {
      if (Received_Servo_Value[0] > Final_Servo_Val[0]) {
        Final_Servo_Val[0]++;
      }

      if (Received_Servo_Value[0] < Final_Servo_Val[0]) {
        Final_Servo_Val[0]--;
      }
      myservo_1.write(180 - Final_Servo_Val[0]);      // adjusted as per app
    }
   // Update shoulder servo position
    if (Received_Servo_Value[1] != Final_Servo_Val[1]) {
      if (Received_Servo_Value[1] > Final_Servo_Val[1]) {
        Final_Servo_Val[1]++;
      }

      if (Received_Servo_Value[1] < Final_Servo_Val[1]) {
        Final_Servo_Val[1]--;
      }
      myservo_2.write(Final_Servo_Val[1]);
    }
    // Update elbow servo position
    if (Received_Servo_Value[2] != Final_Servo_Val[2]) {
      if (Received_Servo_Value[2] > Final_Servo_Val[2]) {
        Final_Servo_Val[2]++;
      }

      if (Received_Servo_Value[2] < Final_Servo_Val[2]) {
        Final_Servo_Val[2]--;
      }
      myservo_3.write(Final_Servo_Val[2]);
    }
    // Update gripper servo position
    if (Received_Servo_Value[3] != Final_Servo_Val[3]) {
      if (Received_Servo_Value[3] > Final_Servo_Val[3]) {
        Final_Servo_Val[3]++;
      }

      if (Received_Servo_Value[3] < Final_Servo_Val[3]) {
        Final_Servo_Val[3]--;
      }
      myservo_4.write(180 - (2 * Final_Servo_Val[3]));  // adjusted as per app
    }
  }
}
