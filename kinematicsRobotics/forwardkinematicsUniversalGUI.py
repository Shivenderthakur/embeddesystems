import tkinter as tk
from tkinter import ttk, messagebox
import random, math, webbrowser
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_unique_color(existing_colors):
    while True:
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        if color not in existing_colors:
            return color

class ForwardKinematicsSim:
    def __init__(self, base=(0,0)):
        self.base = base
        self.link_lengths = []
        self.angles = []

    def add_arm(self, endpoint):
        if not self.link_lengths:
            x0, y0 = self.base
        else:
            last_pos = self.compute_positions()[-1]
            x0, y0 = last_pos
        x, y = endpoint
        dx, dy = x - x0, y - y0
        length = math.hypot(dx, dy)
        if length == 0:
            raise ValueError("Link length cannot be zero.")
        angle = math.degrees(math.atan2(dy, dx))
        self.link_lengths.append(length)
        self.angles.append(angle)

    def remove_arm(self):
        if self.link_lengths:
            self.link_lengths.pop()
            self.angles.pop()

    def clear(self):
        self.link_lengths = []
        self.angles = []

    def compute_positions(self):
        positions = []
        x, y = self.base
        cumulative_angle = 0
        for i, length in enumerate(self.link_lengths):
            cumulative_angle += self.angles[i]
            x += length * math.cos(math.radians(cumulative_angle))
            y += length * math.sin(math.radians(cumulative_angle))
            positions.append((x, y))
        return positions

class KinematicsGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Infinite Robotic Arm Simulator")
        self.geometry("900x750")
        
        self.fk = ForwardKinematicsSim(base=(0,0))
        self.colors = []
        self.fast_increment = 15  # Faster rotation
        self.slow_increment = 2
        
        self.fig, self.ax = plt.subplots(figsize=(6,6))
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Next Joint Coordinates (x,y):").pack(side=tk.LEFT)
        self.coord_entry = ttk.Entry(control_frame, width=20)
        self.coord_entry.insert(0, "10,10")
        self.coord_entry.pack(side=tk.LEFT, padx=5)
        
        add_button = ttk.Button(control_frame, text="Add Arm", command=self.add_arm)
        add_button.pack(side=tk.LEFT, padx=5)
        
        remove_button = ttk.Button(control_frame, text="Remove Last Arm", command=self.remove_arm)
        remove_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = ttk.Button(control_frame, text="Clear All Arms", command=self.clear_chain)
        clear_button.pack(side=tk.LEFT, padx=5)
        
        self.ani = animation.FuncAnimation(self.fig, self.animate, init_func=self.init_anim,
                                           blit=True, interval=30)  # Faster animation
        
        self.create_about_section()
        self.info_frame = ttk.Frame(self)
        self.info_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
        
        # Initial axis limit state (symmetric around 0)
        self.current_limit = 10

    def create_about_section(self):
        about_frame = ttk.LabelFrame(self, text="About", relief=tk.RIDGE)
        about_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        about_label = tk.Label(about_frame, text="Universal Robotic Arm Simulator\n", 
                               background="lightyellow", font=("Helvetica", 10, "bold"))
        about_label.pack(side=tk.LEFT, padx=5, pady=5)
        about_link = tk.Label(about_frame, text="Connect with me on LinkedIn", fg="blue", 
                               cursor="hand2", background="lightyellow", font=("Helvetica", 10, "underline"))
        about_link.pack(side=tk.LEFT, padx=5, pady=5)
        about_link.bind("<Button-1>", lambda e: webbrowser.open("https://www.linkedin.com/in/shivender-singh-thakur/"))
    
    def init_anim(self):
        self.ax.cla()
        self.ax.grid(True)
        return []
    
    def animate(self, frame):
        if not self.fk.link_lengths:
            return []
        
        # Cascading rotation logic
        self.fk.angles[-1] += self.fast_increment
        for i in range(len(self.fk.angles) - 1, -1, -1):
            if self.fk.angles[i] >= 360:
                self.fk.angles[i] -= 360
                if i > 0:
                    self.fk.angles[i-1] += self.slow_increment
        
        positions = self.fk.compute_positions()
        self.ax.cla()
        self.ax.grid(True)
        x_prev, y_prev = self.fk.base
        lines = []
        
        for i, pos in enumerate(positions):
            x, y = pos
            color = self.colors[i] if i < len(self.colors) else "black"
            line, = self.ax.plot([x_prev, x], [y_prev, y], marker='o', markersize=5, linestyle='-', color=color)
            lines.append(line)
            x_prev, y_prev = x, y
        
        self.update_coordinates_display(positions)
        
        # Dynamic zoom out only (do not shrink the axis limits)
        all_x = [self.fk.base[0]] + [p[0] for p in positions]
        all_y = [self.fk.base[1]] + [p[1] for p in positions]
        max_val = max(max(map(abs, all_x)), max(map(abs, all_y)))
        padding = 10
        if max_val + padding > self.current_limit:
            self.current_limit = max_val + padding
        self.ax.set_xlim(-self.current_limit, self.current_limit)
        self.ax.set_ylim(-self.current_limit, self.current_limit)
        
        self.canvas.draw()
        return lines
    
    def update_coordinates_display(self, positions):
        for widget in self.info_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.info_frame, text="Joint Coordinates:", font=("Helvetica", 10, "bold")).pack()
        for i, pos in enumerate(positions):
            ttk.Label(self.info_frame, text=f"Joint {i+1}: {pos}").pack()
    
    def add_arm(self):
        coord_text = self.coord_entry.get()
        try:
            x, y = map(float, coord_text.split(","))
            endpoint = (x, y)
            self.fk.add_arm(endpoint)
            self.colors.append(get_unique_color(self.colors))
        except Exception as e:
            messagebox.showerror("Error", str(e))
        self.draw_current_frame()
    
    def remove_arm(self):
        self.fk.remove_arm()
        if self.colors:
            self.colors.pop()
        self.draw_current_frame()
    
    def clear_chain(self):
        self.fk.clear()
        self.colors = []
        self.draw_current_frame()
    
    def draw_current_frame(self):
        self.animate(0)

if __name__ == "__main__":
    app = KinematicsGUI()
    app.mainloop()
