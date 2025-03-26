import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Joint:
    def __init__(self, x, y, xb=0, yb=0, theta=0):
        self.x = x
        self.y = y
        self.xb = xb
        self.yb = yb
        self.linklength = np.sqrt((x - xb)**2 + (y - yb)**2)
        self.theta = np.radians(theta)

class ForwardKinematics:
    def __init__(self):
        self.jointscount = 0
        self.jointCoordinates = []

    def pushJoint(self, x, y, xb, yb, theta=0):
        self.jointCoordinates.append(Joint(x, y, xb, yb, theta))
        self.jointscount += 1

    def calculateLinkCoordinates(self, index=0):
        if index == 0:
            cos_val = np.cos(self.jointCoordinates[0].theta)
            sin_val = np.sin(self.jointCoordinates[0].theta)
            x = self.jointCoordinates[0].x
            y = self.jointCoordinates[0].y
            self.jointCoordinates[0].x, self.jointCoordinates[0].y = x * cos_val - y * sin_val, y * cos_val + x * sin_val
        else:
            lcurr = self.jointCoordinates[index].linklength
            sin12 = np.sin(self.jointCoordinates[index - 1].theta + self.jointCoordinates[index].theta)
            cos12 = np.cos(self.jointCoordinates[index - 1].theta + self.jointCoordinates[index].theta)
            self.jointCoordinates[index].x = self.jointCoordinates[index - 1].x + lcurr * cos12
            self.jointCoordinates[index].y = self.jointCoordinates[index - 1].y + lcurr * sin12
            self.jointCoordinates[index].xb = self.jointCoordinates[index - 1].x
            self.jointCoordinates[index].yb = self.jointCoordinates[index - 1].y

    def updateJointAngles(self, base_angle, mid_angle, end_angle):
        # Set the joint angles (in degrees converted to radians)
        self.jointCoordinates[0].theta = np.radians(base_angle)
        self.jointCoordinates[1].theta = np.radians(mid_angle)
        self.jointCoordinates[2].theta = np.radians(end_angle)
        for i in range(self.jointscount):
            self.calculateLinkCoordinates(i)

    def plotJoints(self):
        x_vals = [joint.x for joint in self.jointCoordinates]
        y_vals = [joint.y for joint in self.jointCoordinates]
        return x_vals, y_vals

# Initialize the ForwardKinematics object with three joints:
fk = ForwardKinematics()
fk.pushJoint(15, 0, 0, 0, 0)    # Base joint (origin-based)
fk.pushJoint(10, 0, 15, 0, 0)   # Middle joint
fk.pushJoint(5, 0, 10, 0, 0)    # End joint

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')
ax.grid(True)

# Create separate line objects for each link:
line1, = ax.plot([], [], marker='o', markersize=5, linestyle='-', color='r')  # Base link: red
line2, = ax.plot([], [], marker='o', markersize=5, linestyle='-', color='b')  # Mid link: blue
line3, = ax.plot([], [], marker='o', markersize=5, linestyle='-', color='g')  # End link: green

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

# Global angle variables to track the state of each joint
base_angle = 0
mid_angle = 0
end_angle = 0

def animate(frame):
    global base_angle, mid_angle, end_angle
    # Increase the end joint's angle by 5° per frame
    end_angle += 1

    # When end joint completes a full rotation, update the mid joint
    if end_angle >= 360:
        end_angle -= 360
        mid_angle += 15

        # When mid joint completes a full rotation, update the base joint
        if mid_angle >= 360:
            mid_angle -= 360
            base_angle += 30
            # Stop base after full rotation, or you can reset it if desired
            if base_angle >= 360:
                base_angle = 360

    # Update joint angles in the kinematics model
    fk.updateJointAngles(base_angle, mid_angle, end_angle)

    # Update the base link (from its fixed base to the first joint)
    x0 = [fk.jointCoordinates[0].xb, fk.jointCoordinates[0].x]
    y0 = [fk.jointCoordinates[0].yb, fk.jointCoordinates[0].y]
    line1.set_data(x0, y0)

    # Update the mid link (from first joint to second joint)
    x1 = [fk.jointCoordinates[0].x, fk.jointCoordinates[1].x]
    y1 = [fk.jointCoordinates[0].y, fk.jointCoordinates[1].y]
    line2.set_data(x1, y1)

    # Update the end link (from second joint to third joint)
    x2 = [fk.jointCoordinates[1].x, fk.jointCoordinates[2].x]
    y2 = [fk.jointCoordinates[1].y, fk.jointCoordinates[2].y]
    line3.set_data(x2, y2)

    return line1, line2, line3


ani = animation.FuncAnimation(fig, animate, init_func=init, blit=True,interval=0.0004)
plt.show()
