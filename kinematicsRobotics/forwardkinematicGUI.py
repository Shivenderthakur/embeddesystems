import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RoboticArmSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Robotic Arm Simulator By Shivender Singh Thakur")
        self.geometry("900x700")
        
        # Initialize joint angles before using them
        self.joint_angles = [90, 90]  # Initial angles in degrees
        
        # Initialize lengths of the links
        self.link_lengths = [10, 10]  # Lengths of the two links
        
        self.create_widgets()
        self.create_plot()
        self.update_plot()

    def create_widgets(self):
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.LEFT, padx=20, pady=20)

        ttk.Label(control_frame, text="Base Link Angle (θ₁):").grid(row=0, column=0, padx=5, pady=5)
        self.theta1_entry = ttk.Entry(control_frame)
        self.theta1_entry.grid(row=0, column=1, padx=5, pady=5)
        self.theta1_entry.insert(0, str(self.joint_angles[0]))  # Accessing joint_angles safely

        ttk.Label(control_frame, text="Upper Joint Angle (θ₂):").grid(row=1, column=0, padx=5, pady=5)
        self.theta2_entry = ttk.Entry(control_frame)
        self.theta2_entry.grid(row=1, column=1, padx=5, pady=5)
        self.theta2_entry.insert(0, str(self.joint_angles[1]))  # Accessing joint_angles safely

        update_button = ttk.Button(control_frame, text="Update Plot", command=self.update_angles)
        update_button.grid(row=2, column=0, columnspan=2, pady=10)

        reset_button = ttk.Button(control_frame, text="Reset Angles", command=self.reset_angles)
        reset_button.grid(row=3, column=0, columnspan=2, pady=10)

    def create_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.set_xlim(-25, 25)
        self.ax.set_ylim(-25, 25)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, padx=20, pady=20)

    def update_angles(self):
        try:
            theta1 = float(self.theta1_entry.get())
            theta2 = float(self.theta2_entry.get())
            if not (-360 <= theta1 <= 360):
                raise ValueError("θ₁ must be between -360 and 360 degrees.")
            if not (-360 <= theta2 <= 360):
                raise ValueError("θ₂ must be between -360 and 360 degrees.")
            self.joint_angles = [theta1, theta2]
            self.update_plot()
        except ValueError as e:
            print(f"Invalid input: {e}")

    def reset_angles(self):
        self.joint_angles = [90, 90]
        self.theta1_entry.delete(0, tk.END)
        self.theta1_entry.insert(0, str(self.joint_angles[0]))
        self.theta2_entry.delete(0, tk.END)
        self.theta2_entry.insert(0, str(self.joint_angles[1]))
        self.update_plot()

    def update_plot(self):
        self.ax.clear()
        self.ax.set_xlim(-25, 25)
        self.ax.set_ylim(-25, 25)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.grid(True)

        theta1_rad = np.radians(self.joint_angles[0])
        theta2_rad = np.radians(self.joint_angles[1])

        x0, y0 = 0, 0  # Base origin
        l1, l2 = self.link_lengths

        x1 = l1 * np.cos(theta1_rad)
        y1 = l1 * np.sin(theta1_rad)

        x2 = x1 + l2 * np.cos(theta1_rad + theta2_rad)
        y2 = y1 + l2 * np.sin(theta1_rad + theta2_rad)

        self.ax.plot([x0, x1], [y0, y1], label="Base to First Joint", color="red", linewidth=2)
        self.ax.plot([x1, x2], [y1, y2], label="First Joint to End Effector", color="blue", linewidth=2)
        self.ax.scatter([x0, x1, x2], [y0, y1, y2], color="black", zorder=5)
        self.ax.legend()

        self.canvas.draw()

if __name__ == "__main__":
    app = RoboticArmSimulator()
    app.mainloop()
