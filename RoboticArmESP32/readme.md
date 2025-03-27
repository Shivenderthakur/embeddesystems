# Robotic Arm with ESP32

This project demonstrates how to control a robotic arm using an ESP32. Two approaches are provided:
1. **Direct Servo Control** using the [ESP32Servo Library](https://github.com/jkb-git/ESP32Servo) to drive four servos.
2. **Servo Driver Control** using a PCA9685 board with the [Adafruit_PWMServoDriver Library](https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library) for higher channel count and resolution.

Both versions use Bluetooth to receive commands and set the servo positions for the base, shoulder, elbow, and gripper.

---

## Overview

This project demonstrates how to:
- Use an ESP32 to control servos either directly or via a PCA9685 driver.
- Receive Bluetooth commands over the ESP32’s built-in Bluetooth Serial.
- Gradually update servo positions for smooth movement.
- Convert received angle commands into servo actions.

---

## Features

- **Bluetooth Control:** Communicate with the arm using any Bluetooth-enabled device.
- **Smooth Motion:** Servo positions update gradually to avoid abrupt movements.
- **Flexible Implementation:** Choose between direct servo control (ESP32Servo) or using a PCA9685 driver for multi-channel support.

---

## Hardware Requirements

- **For Both Versions:**
  - ESP32 development board
  - 4 Servo motors (for base, shoulder, elbow, and gripper)
  - Jumper wires and a breadboard (or a custom PCB for permanent wiring)

- **For Direct Servo Control:**
  - No additional hardware is required as the servos are directly controlled via the ESP32.

- **For Servo Driver Control:**
  - PCA9685 servo driver module (e.g., Adafruit 16-channel PWM/Servo Driver)
  - I²C connections (typically SDA to GPIO 21 and SCL to GPIO 22 on the ESP32, but verify for your board)

---

## Software Requirements

- Arduino IDE or PlatformIO
- **Libraries:**
  - For Direct Servo Control: [ESP32Servo Library](https://github.com/jkb-git/ESP32Servo)
  - For Servo Driver Control: [Adafruit_PWMServoDriver Library](https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library)
- Bluetooth Serial (built into the ESP32)

---

## Setup & Installation

### 1. Hardware Setup

#### Direct Servo Control (ESP32Servo)
- Connect each servo to the designated ESP32 pins:
  - **Base servo:** Pin **13**
  - **Shoulder servo:** Pin **12**
  - **Elbow servo:** Pin **14**
  - **Gripper servo:** Pin **27**
- Ensure that your power supply is sufficient for the servos.

#### Servo Driver Control (PCA9685)
- Connect the PCA9685 to the ESP32 via I²C:
  - Typically, **SDA** to GPIO 21 and **SCL** to GPIO 22.
- Attach the servos to the PCA9685 channels:
  - **Base servo:** Channel **0**
  - **Shoulder servo:** Channel **1**
  - **Elbow servo:** Channel **2**
  - **Gripper servo:** Channel **3**

### 2. Software Setup

- Open the appropriate sketch in the Arduino IDE:
  - **For Direct Servo Control:** `RoboticArmESP32.ino`
  - **For Servo Driver Control:** `RoboticArmServoDriver.ino`
- Install the required libraries via the Arduino Library Manager.
- Compile and upload the sketch to your ESP32.

### 3. Bluetooth Pairing & Usage

- Power on your ESP32.
- Pair your smartphone or computer with the Bluetooth device:
  - **Direct Control:** The device name is **"ROBOARM"**
  - **Servo Driver Control:** The device name is **"ROBOTIC ARM"**
- Use a serial terminal or Bluetooth app to send commands.

---

## How It Works

### Bluetooth Communication
- The ESP32 listens for Bluetooth data.
- When a newline character (`\n`) is received, the incoming string is parsed.
- The expected data format is a comma-separated list of angles (for base, shoulder, elbow, gripper).

### Servo Control
- **Direct Control:**  
  The ESP32Servo library directly moves the servos. Positions are updated gradually to ensure smooth transitions.
  
- **Servo Driver Control:**  
  Angle values are mapped to PWM pulse lengths for the PCA9685. The driver then sets the servo positions accordingly, with real-time feedback printed to the Serial Monitor.

---

## Data Format

Send data as a comma-separated list of angles, terminated with a newline. For example:


- **90:** Base servo angle
- **120:** Shoulder servo angle
- **60:** Elbow servo angle
- **45:** Gripper servo angle

*Example:* When you send `90,120,60,45\n` via Bluetooth, the robotic arm updates each servo to the corresponding angle.

---


## License

This project is licensed under the MIT License.
