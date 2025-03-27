# Robotic Arm Servo Driver

A project that uses an ESP32 and a PCA9685 servo driver to control a robotic arm via Bluetooth commands. This repository demonstrates how to interface with the PCA9685 for controlling multiple servos simultaneously.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is designed to control a robotic arm using an ESP32 microcontroller paired with a PCA9685 servo driver board. By receiving Bluetooth commands, the system adjusts servo angles to move the robotic arm precisely.

## Features

- **Bluetooth Communication:** Receive commands wirelessly.
- **Multiple Servo Control:** Use the PCA9685 to control up to 16 servos.
- **Real-Time Feedback:** Monitor servo movements via serial output.
- **Easy Integration:** Straightforward code structure for customization.

## Hardware Requirements

- ESP32 development board
- PCA9685 16-channel PWM/Servo Driver
- 4 Servo motors (for base, shoulder, elbow, and gripper)
- Jumper wires and a breadboard

## Software Requirements

- Arduino IDE or PlatformIO
- [Adafruit_PWMServoDriver Library](https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library)
- Bluetooth Serial (built into the ESP32)

## Setup & Installation

1. **Hardware Assembly:**
   - Connect the PCA9685 to the ESP32 via I²C (commonly SDA to GPIO 21 and SCL to GPIO 22).
   - Attach the servos to the PCA9685 channels:
     - **Channel 0:** Base Servo
     - **Channel 1:** Shoulder Servo
     - **Channel 2:** Elbow Servo
     - **Channel 3:** Gripper Servo

2. **Software Setup:**
   - Open the `RoboticArmServoDriver.ino` sketch in the Arduino IDE.
   - Install the [Adafruit_PWMServoDriver Library](https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library) via the Library Manager.
   - Compile and upload the sketch to your ESP32.

## Usage

1. **Power Up:** Ensure your ESP32, PCA9685, and servos are properly powered.
2. **Bluetooth Pairing:**  
   - Pair your smartphone or computer with the Bluetooth device named **"ROBOTIC ARM"**.
3. **Send Commands:**  
   - Use a Bluetooth terminal app to send a command string in the following format:
     
     ```
     base,shoulder,elbow,gripper
     ```
     
   - The command must be terminated with a newline character (`\n`).

## Code Overview

- **Bluetooth Handling:**  
  The code continuously listens for incoming Bluetooth data and uses a newline as the end-of-command marker.
  
- **Data Parsing:**  
  Received data is parsed to extract individual servo angles.

- **Servo Control:**  
  Each angle is converted to a corresponding PWM pulse using a mapping function. The PCA9685 then sets the servo positions accordingly.

- **Feedback:**  
  Servo angles and their mapped PWM pulses are output to the Serial Monitor for debugging.

## Example

Sending the following command:
will set:
- **Base Servo:** 90°
- **Shoulder Servo:** 120°
- **Elbow Servo:** 60°
- **Gripper Servo:** 45°


## License

This project is licensed under the MIT License.

