import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RoboticArmSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Robotic Arm Simulator")
        self.geometry("900x700")
        
        # Initialize default values for joint angles, link lengths, and base coordinates
        self.joint_angles = [90, 90]  # Initial angles in degrees
        self.link_lengths = [10, 10]  # Lengths of the two links
        self.base_coordinates = [0, 0]  # Base origin coordinates (x0, y0)
        
        self.create_widgets()
        self.create_plot()
        self.update_plot()

    def create_widgets(self):
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.LEFT, padx=20, pady=20)

        # Angle Inputs
        ttk.Label(control_frame, text="Base Link Angle (θ₁):").grid(row=0, column=0, padx=5, pady=5)
        self.theta1_entry = ttk.Entry(control_frame)
        self.theta1_entry.grid(row=0, column=1, padx=5, pady=5)
        self.theta1_entry.insert(0, str(self.joint_angles[0]))

        ttk.Label(control_frame, text="Upper Joint Angle (θ₂):").grid(row=1, column=0, padx=5, pady=5)
        self.theta2_entry = ttk.Entry(control_frame)
        self.theta2_entry.grid(row=1, column=1, padx=5, pady=5)
        self.theta2_entry.insert(0, str(self.joint_angles[1]))

        # Link Length Inputs
        ttk.Label(control_frame, text="Link 1 Length (L₁):").grid(row=2, column=0, padx=5, pady=5)
        self.link1_entry = ttk.Entry(control_frame)
        self.link1_entry.grid(row=2, column=1, padx=5, pady=5)
        self.link1_entry.insert(0, str(self.link_lengths[0]))

        ttk.Label(control_frame, text="Link 2 Length (L₂):").grid(row=3, column=0, padx=5, pady=5)
        self.link2_entry = ttk.Entry(control_frame)
        self.link2_entry.grid(row=3, column=1, padx=5, pady=5)
        self.link2_entry.insert(0, str(self.link_lengths[1]))

        # Base Coordinates Inputs
        ttk.Label(control_frame, text="Base X Coordinate (X₀):").grid(row=4, column=0, padx=5, pady=5)
        self.base_x_entry = ttk.Entry(control_frame)
        self.base_x_entry.grid(row=4, column=1, padx=5, pady=5)
        self.base_x_entry.insert(0, str(self.base_coordinates[0]))

        ttk.Label(control_frame, text="Base Y Coordinate (Y₀):").grid(row=5, column=0, padx=5, pady=5)
        self.base_y_entry = ttk.Entry(control_frame)
        self.base_y_entry.grid(row=5, column=1, padx=5, pady=5)
        self.base_y_entry.insert(0, str(self.base_coordinates[1]))

        # Control Buttons
        update_button = ttk.Button(control_frame, text="Update Plot", command=self.update_parameters)
        update_button.grid(row=6, column=0, columnspan=2, pady=10)

        reset_button = ttk.Button(control_frame, text="Reset to Default", command=self.reset_parameters)
        reset_button.grid(row=7, column=0, columnspan=2, pady=10)

    def create_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.set_xlim(-25, 25)
        self.ax.set_ylim(-25, 25)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, padx=20, pady=20)

    def update_parameters(self):
        try:
            # Get angles
            theta1 = float(self.theta1_entry.get())
            theta2 = float(self.theta2_entry.get())
            if not (-360 <= theta1 <= 360) or not (-360 <= theta2 <= 360):
                raise ValueError("Angles must be between -360 and 360 degrees.")
            
            # Get link lengths
            link1_length = float(self.link1_entry.get())
            link2_length = float(self.link2_entry.get())
            if link1_length <= 0 or link2_length <= 0:
                raise ValueError("Link lengths must be positive values.")
            
            # Get base coordinates
            base_x = float(self.base_x_entry.get())
            base_y = float(self.base_y_entry.get())

            # Update the parameters
            self.joint_angles = [theta1, theta2]
            self.link_lengths = [link1_length, link2_length]
            self.base_coordinates = [base_x, base_y]

            self.update_plot()
        except ValueError as e:
            print(f"Invalid input: {e}")

    def reset_parameters(self):
        # Reset to default values
        self.joint_angles = [90, 90]
        self.link_lengths = [10, 10]
        self.base_coordinates = [0, 0]

        # Reset UI entries
        self.theta1_entry.delete(0, tk.END)
        self.theta1_entry.insert(0, str(self.joint_angles[0]))

        self.theta2_entry.delete(0, tk.END)
        self.theta2_entry.insert(0, str(self.joint_angles[1]))

        self.link1_entry.delete(0, tk.END)
        self.link1_entry.insert(0, str(self.link_lengths[0]))

        self.link2_entry.delete(0, tk.END)
        self.link2_entry.insert(0, str(self.link_lengths[1]))

        self.base_x_entry.delete(0, tk.END)
        self.base_x_entry.insert(0, str(self.base_coordinates[0]))

        self.base_y_entry.delete(0, tk.END)
        self.base_y_entry.insert(0, str(self.base_coordinates[1]))

        self.update_plot()

    def update_plot(self):
        self.ax.clear()
        self.ax.set_xlim(-25, 25)
        self.ax.set_ylim(-25, 25)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True)

        # Convert angles from degrees to radians
        theta1_rad = np.radians(self.joint_angles[0])
        theta2_rad = np.radians(self.joint_angles[1])

        # Extract the base coordinates and link lengths
        x0, y0 = self.base_coordinates
        l1, l2 = self.link_lengths

        # Calculate positions of joints and end effector
        x1 = x0 + l1 * np.cos(theta1_rad)
        y1 = y0 + l1 * np.sin(theta1_rad)

        x2 = x1 + l2 * np.cos(theta1_rad + theta2_rad)
        y2 = y1 + l2 * np.sin(theta1_rad + theta2_rad)

        # Plot the arm
        self.ax.plot([x0, x1], [y0, y1], label="Base to First Joint", color="red", linewidth=2)
        self.ax.plot([x1, x2], [y1, y2], label="First Joint to End Effector", color="blue", linewidth=2)
        self.ax.scatter([x0, x1, x2], [y0, y1, y2], color="black", zorder=5)
        self.ax.legend()

        self.canvas.draw()

if __name__ == "__main__":
    app = RoboticArmSimulator()
    app.mainloop()
