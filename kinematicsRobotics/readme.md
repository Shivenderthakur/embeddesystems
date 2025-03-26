# Robotic Arm Forward Kinematics Simulator

## Overview
This repository contains multiple Python scripts that implement forward kinematics for robotic arms. The implementations include GUI-based simulations using Tkinter and Matplotlib, as well as command-line tools for visualizing joint transformations.

## Features
- **GUI-based Simulations**: Interactive Tkinter applications for visualizing robotic arm movements.
- **Mathematical Computations**: Uses numpy and trigonometric functions to compute joint positions.
- **Matplotlib Visualization**: Plots the arm movements dynamically.
- **Animation Support**: Continuous joint rotations using Matplotlib animation.

## Installation
Ensure you have Python 3 installed. Then, install the required dependencies:

```sh
pip install numpy matplotlib tkinter
```

## Usage
Run any of the Python scripts to see the forward kinematics in action.

```sh
python forwardkinematicGUI.py
```

```sh
python forwardkinematicsUniversalGUI.py
```

## Files in the Repository

```yaml
- forwardkinematicGUI.py: GUI-based simulator for a two-link robotic arm.
- forwardkinematics.py: Command-line tool implementing forward kinematics for one and two-joint arms.
- forwardkinematicsUniversal.py: Generalized kinematics model with multiple joints and animation.
- forwardkinematicsUniversalGUI.py: GUI application to simulate an infinite robotic arm with adjustable joints.
- tmp.py: Script to extract and save Python file contents.
```

## Demo

### Video Demonstration
[![Demo Video](https://via.placeholder.com/800x450)](https://github.com/Shivenderthakur/embeddesystems/blob/learning/kinematicsRobotics/Demo.mkv)

### Screenshots
![Screenshot 1](https://github.com/Shivenderthakur/embeddesystems/blob/learning/kinematicsRobotics/Defaultpos.PNG)
![Screenshot 2](https://github.com/Shivenderthakur/embeddesystems/blob/learning/kinematicsRobotics/NewPos45.45.PNG)



