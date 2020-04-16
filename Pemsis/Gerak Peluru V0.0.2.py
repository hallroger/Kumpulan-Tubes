import math
from math import radians,sin,cos
#import matplotlib.pyplot as plt
ax = 0
ay = -9.806 #percepatan sumbu y
v0 = 50
angle = 0.610865
timestep1 = 0.01
t = 0
vx = v0 * math.cos(angle)
vy = v0 * math.sin(angle)
x0= 0
y0= 0
y = 0
ymax = 0
xmax = 0
x= 0
vx1 = vx + float(ax) * float(timestep1)
vy1 = vy + float(ay) * float(timestep1)
print("Vy detik ke- ",(t+timestep1)," : ",vy1)
print("Vx detik ke- ",(t+timestep1)," : ",vx1)
x= x + (vx1*timestep1)
y= y + (vy1*timestep1)
print (x)
print ("This Y 1",y)
t = t + timestep1

while( y > 0):
    vx1 = vx1 + float(ax) * float(timestep1)
    vy1 = vy1 + float(ay) * float(timestep1)
    print("Vy detik ke- ",(t+timestep1)," : ",vy1)
    print("Vx detik ke- ",(t+timestep1)," : ",vx1)
    x= x + (vx1*timestep1)
    y= y + (vy1*timestep1)
    #print (x)
    #print ("This Y2",y)
    t = t + timestep1
    if (y > ymax):
        ymax=y
    xmax = x
print (x)
print ("This Y2",y)
print ("This Xmax 1: ",xmax)
print ("This Ymax 1:",ymax)
xmax = x0 + (vx * t) + 1/2 * ax * t*t

ymax = y0 + (vy * t) - 1/2 * ay * t*t
print (xmax)
print (ymax)



#plt.show