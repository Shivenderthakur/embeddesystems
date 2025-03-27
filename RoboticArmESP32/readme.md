# Robotic Arm with ESP32

A simple project that uses an ESP32 to control a robotic arm using servos. Bluetooth commands are received to set the servo positions for base, shoulder, elbow, and gripper.

## Overview

This project demonstrates how to:
- Use the ESP32Servo library to control servo motors.
- Receive Bluetooth commands via the ESP32’s built-in Bluetooth serial.
- Gradually update servo positions to ensure smooth motion.

## Features

- **Bluetooth Control:** Communicate with the arm using a Bluetooth-enabled device.
- **Smooth Motion:** Servo positions are updated gradually for smoother movement.
- **Easy to Modify:** The code is simple and can be adapted for different robotic arm configurations.

## Hardware Requirements

- ESP32 development board
- 4 Servo motors (for base, shoulder, elbow, and gripper)
- Jumper wires and breadboard (or a custom PCB for a permanent setup)

## Software Requirements

- Arduino IDE or PlatformIO
- [ESP32Servo Library](https://github.com/jkb-git/ESP32Servo)  
- Bluetooth Serial (included with ESP32)

## Setup & Installation

1. **Hardware Setup:**  
   - Connect each servo to the designated ESP32 pins:
     - Base servo to pin **13**
     - Shoulder servo to pin **12**
     - Elbow servo to pin **14**
     - Gripper servo to pin **27**
   - Ensure your power supply meets the servo requirements.

2. **Software Setup:**  
   - Open the `RoboticArmESP32.ino` sketch in the Arduino IDE.
   - Install the required libraries (ESP32Servo) via the Library Manager.
   - Compile and upload the sketch to your ESP32.

3. **Bluetooth Pairing:**  
   - Power on the ESP32.
   - Pair your smartphone or computer with the Bluetooth device named **"ROBOARM"**.
   - Use a serial terminal app to send commands (formatted as `90,120,60,45\n`) to control the servos.

## How It Works

- **Bluetooth Communication:**  
  The ESP32 waits for data over Bluetooth. When a newline character (`\n`) is received, it parses the incoming string (expected format: `Base,Shoulder,Elbow,Gripper` angles).

- **Smooth Servo Updates:**  
  Instead of jumping immediately to the new position, the servos update gradually to create a smooth movement.



