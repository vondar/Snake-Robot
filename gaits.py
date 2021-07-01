# import sympy as sp
from numpy import sin,cos,pi
import numpy as np
import math as m
from sympy import symbols
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


a=1

def transform(a,b,d,l):
    rot=np.array([[cos(a),-sin(a)*cos(b), sin(a)*sin(b),l*cos(a)],
                  [sin(a), cos(a)*cos(b),-cos(a)*sin(b),l*sin(a)],
                  [0     ,        sin(b),        cos(b),       d],
                  [0     ,       0      ,        0     ,       1]])
    return rot
j=0

fig = plt.figure()
ax = plt.axes(projection='3d')
zline=[0,0,0,0,0,0,0,0,0,0]
xline=[0,0,0,0,0,0,0,0,0,0]
yline=[0,0,0,0,0,0,0,0,0,0]


def angle(i,key,t):

        #lateral undulation
    if key ==1:
        w=(5*np.pi)/6
        phi=0
        if i%2==0:
            a=np.pi/3
            do=(2*np.pi)/3
        else:
            a=0
            do=0
    #sidewinding
    if key ==2:
        a=np.pi/6
        w=(5*np.pi)/6
        do=(2*np.pi)/3
        phi=0
    #rolling
    if key ==3:
        a=np.pi/3
        w=(5*np.pi)/6
        do=pi/2
        if i%2==0:
            phi=0
        else:
            phi=np.pi/6
    #linear progression
    if key== 4:
        w=(5*np.pi)/6
        phi=0
        if i%2==0:
            a=0
            do=0
        else:
            a=np.pi/3
            do=(2*np.pi)/3
    angles=a*sin(w*t+i*do+phi)
    return angles
ang=[0,0,0,0,0,0,0,0,0,0]

key= int(input())

while True:

    for i in range(0,10):
        ang[i]= angle(i,key,j)
    #frames will carry all DH parameters
    frames=np.array([[ang[0],np.pi/2,0,a],
                    [ang[1],-np.pi/2,0,a],
                    [ang[2],np.pi/2, 0,a],
                    [ang[3],-np.pi/2,0,a],
                    [ang[4],np.pi/2, 0,a],
                    [ang[5],-np.pi/2,0,a],
                    [ang[6],np.pi/2, 0,a],
                    [ang[7],-np.pi/2,0,a],
                    [ang[8],np.pi/2, 0,a],
                    [ang[9],-np.pi/2,0,a]])

    
    xox=[0,0,0,0,0,0,0,0,0,0]
    
    for i in range(0,10):
        xox[i]=transform(frames[i][0],frames[i][1],frames[i][2],frames[i][3])
        

    xoy=[0,0,0,0,0,0,0,0,0,0]

    xoy[0]=xox[0]
    for i in range(1, 10):
        xoy[i]=xoy[i-1]@xox[i]
        
    for i in range(0, 10):
        zline[i]=xoy[i][2,3]
        
        xline[i]=xoy[i][0,3]
        
        yline[i]=xoy[i][1,3]
        

    ax.plot3D(xline, yline, zline,'ro')
    ax.plot3D(xline, yline, zline,'grey')
    ax.set_xlim3d(-2,7)
    ax.set_ylim3d(-2,7)
    ax.set_zlim3d(-2,7)
    plt.draw()
    plt.pause(0.01)
    plt.cla()
    j=j+0.01
