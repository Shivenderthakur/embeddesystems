#include <Servo.h>

int pins[] = {3, 5, 6, 9, 10, 11};
int len = 6;
Servo myservo[6];
String inputString = "";

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < len; i++)
    myservo[i].attach(pins[i]);
  Serial.println("Pins initialized up to 6.");
}

void loop() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    
    if (inChar == ';') {
      // End of command

      parseCommand(inputString);
      inputString = "";
    } else {
      inputString += inChar;
    }
  }
}

void parseCommand(String command) {
  int commaIndex = command.indexOf(',');
  if (commaIndex == -1) {
    Serial.println("Invalid format. Use index,angle;");
    return;
  }
  int index = command.substring(0, commaIndex).toInt();
  int angle = command.substring(commaIndex + 1).toInt();

  if (index >= 1 && index <= 6) {
    myservo[index - 1].write(angle);
    Serial.print("Servo ");
    Serial.print(index);
    Serial.print(" set to ");
    Serial.println(angle);
  } else {
    Serial.println("Invalid index. Please send a number between 1 and 6.");
  }
}