import matplotlib.pyplot as plt
import math
import numpy as np
def calculatenextCoordinateForwardTransformation(x,y,theta):
    """as the formula is sin(alpha + theta)=ycostheta+xsintheta"""

    cos = round(math.cos(theta))
    sin = round(math.sin(theta))
    print(x*cos-y*sin,y*cos+x*sin)
    return (x*cos-y*sin,y*cos+x*sin)

def plotnextCoordinateTransformation(x0,y0,x1,y1,xb=0,yb=0):
    "all the lines must be drawn from the x axis right now so "
    val = max(abs(int(v)) for v in [x0,y0,x1,y1])+10
    plt.xlim(-val, val)
    plt.ylim(-val, val)

    # Adding grid to help visualize quadrants
    plt.grid(True)    


    plt.plot([xb, x0], [yb, y0], label="Base to Previous",color="red")
    plt.plot([xb, x1], [yb, y1], label="Previous to Next",color="blue")
    plt.show()

x,y,theta=input("Enter the x ,y ,theta").split()
print(x,y,theta)
(x1,y1)=calculatenextCoordinateForwardTransformation(int(x),int(y),int(theta))
plotnextCoordinateTransformation(int(x),int(y),x1,y1)





