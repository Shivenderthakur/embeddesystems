import matplotlib.pyplot as plt
import math
import numpy as np
"""
This file shows the forward kinematics with one joint and twojoing
"""

class OneJoint:
    def __init__(self):
        pass
    def calculatenextCoordinateForwardTransformation(self,x,y,theta):
        """as the formula is sin(alpha + theta)=ycostheta+xsintheta  an"""

        cos = round(np.cos(theta))
        sin = round(np.sin(theta))
        print(x*cos-y*sin,y*cos+x*sin)
        return (x*cos-y*sin,y*cos+x*sin)

    def plotnextCoordinateTransformation(self,x0,y0,xb=0,yb=0):
        "all the lines must be drawn from the x axis right now so "
        val = max(abs(int(v)) for v in [x0,y0,x1,y1])+10
        plt.xlim(-val, val)
        plt.ylim(-val, val)

        # Adding grid to help visualize quadrants
        plt.grid(True)    


        plt.plot([xb, x0], [yb, y0], label="Base to Previous",color="red")

        plt.show()
#aloksg@gmail.com
'''x,y,theta=input("Enter the x ,y ,theta").split()
print(x,y,theta)
(x1,y1)=OneJoint.calculatenextCoordinateForwardTransformation(int(x),int(y),int(theta))
OneJoint.plotnextCoordinateTransformation(int(x),int(y),x1,y1)

'''
class TwoJoints(OneJoint):
    def __init__(self,is_save=False):
        super().__init__()
        self.points=[90,90,0,0,0,0]
        self.issave =is_save
    def save_points(self,points):
        if self.issave:
            self.points=points

            
    def plotnextCoordinateTransformation(self,xp,yp,x1,y1,xb=0,yb=0):
        print(xp,yp,x1,y1)
        "all the lines must be drawn from the x axis right now so "
        val = max(abs(int(v)) for v in [xp,yp,x1,y1])+10
        plt.xlim(-val, val)
        plt.ylim(-val, val)

        # Adding grid to help visualize quadrants
        plt.grid(True)    


        plt.plot([xb, xp], [yb, yp], label="first joint",color="red")
        plt.plot([xp, x1], [yp, y1], label="second joint",color="blue")
        plt.show()                       
    def calculateCoordinatesForUpperJoint(self,xp,yp,x,y,theta1,theta2=90):
        xp1,yp1=xp,yp
        theta1=np.radians(theta1)
        theta2=np.radians(theta2)
        (xp_dash,yp_dash)=self.calculatenextCoordinateForwardTransformation(xp,yp,theta1)


        cos_12 = np.cos(theta1+theta2)
        sin_12 =np.sin(theta1+theta2)# if theta >=0 else np.sin(theta)*-1
        cos = np.cos(theta1)
        sin =np.sin(theta1)# if theta >=0 else np.sin(theta)*-1        
        l2 =math.sqrt(math.pow(x-xp1,2)+math.pow(y-yp1,2))
        l1=math.sqrt(math.pow(xp1,2)+math.pow(yp1,2))
        y_dash = l1*sin+l2*sin_12
        x_dash = l2*cos+l2*cos_12
        print(xp_dash,yp_dash,x_dash,y_dash)
        return xp_dash,yp_dash,x_dash,y_dash

        
def menu():
    theta1=90
    theta2=90
    twoj = TwoJoints()
    if str(input("Want to save previous coordinates y/n")).lower == "y":
        twoj = TwoJoints(is_save=True)
    while True:        
        link = int(input("""
        1.Rotate Base Link default for second link is 90
        2.Rotate Second Link default for first link is 90
        3.Both
        0.To exit
        default coordinates are xp,yp (5,5) x,y (10,10) for plotting 
        """))
        if link not in [1,2,3,0]:
            print("Enter the Correct Choice")
            continue
        if link == 0:
            exit()
        twoj.points=[90,45,5,5,15,5]
        if link==1 or link ==3:   
            while True:
                try:
                    theta1 =float(input("Angle of the base link in respect to x axis")) 
                except:
                    print("Enter the angle in float or int")
                    continue                    
                th1=1
                if not (theta1>=-360 and theta1 <=360):
                    print(f"Angle {theta1} of the base link in respect to x axis is invalid ")
                    continue
                break
        if link==2 or link==3:
            while True:
                try:
                    theta2 = float(input("Angle of the joint between end link in respect to base link"))    
                except:
                    print("Enter the angle in float or int")
                    continue
                if not (theta2>=-360 and theta2 <=360):
                    print(f"Angle {theta1} of the base link in respect to x axis is invalid ")                
                    continue
                break
        [xp,yp,x,y] = twoj.points[2:]
        twoj.plotnextCoordinateTransformation(xp,yp,x,y)
        xp_dash,yp_dash,x_dash,y_dash=twoj.calculateCoordinatesForUpperJoint(xp,yp,10,10,twoj.points[0],twoj.points[1])
        twoj.save_points([theta1,theta2,xp_dash,yp_dash,x_dash,y_dash])

        twoj.save_points([theta1,theta2,xp_dash,yp_dash,x_dash,y_dash])
        twoj.plotnextCoordinateTransformation(xp_dash,yp_dash,x_dash,y_dash)
                



        
        
        

if __name__=="__main__":
    menu()




