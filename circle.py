import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def clearScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)


def plot_line():
    d = 100
    print(' How do you want to draw a circle? ')
    print('1. using Mid point circle drawing algorithm')
    print('2. using Polar circle generation algorithm')
    print('3. using Non-Polar circle generation algorithm')
    ch = int(input('Enter your choice: '))
    if (ch==1):
        xc = int(input('Enter the x coordinate of centre: '))
        yc = int(input('Enter the y coordinate of centre: '))
        r = int(input('Enter the radius of circle: '))
        p = 1-r
        x = 0
        y = r
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POINTS)
        while(x<=y):
            glVertex2f((xc+x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc-y)/d)
            glVertex2f((xc+x)/d,(yc-y)/d)
            glVertex2f((xc+y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc-x)/d)
            glVertex2f((xc+y)/d,(yc-x)/d)
            if(p<=0):
                x = x + 1
                p = p + (2*x) + 1
            else:
                y = y - 1
                x = x + 1
                p = p + (2*(x-y)) + 1
        glEnd()
        glFlush()




    elif (ch==2):
        xc = int(input('Enter the x coordinate of centre: '))
        yc = int(input('Enter the y coordinate of centre: '))
        r = int(input('Enter the radius of circle: '))
        dtheta = 1/r
        theta = 0
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POINTS)
        while(theta <= 22/28):
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f((xc+x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc-y)/d)
            glVertex2f((xc+x)/d,(yc-y)/d)
            glVertex2f((xc+y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc-x)/d)
            glVertex2f((xc+y)/d,(yc-x)/d)
            theta = theta + dtheta
        glEnd()
        glFlush()


    elif (ch==3):
        xc = int(input('Enter the x coordinate of centre: '))
        yc = int(input('Enter the y coordinate of centre: '))
        r = int(input('Enter the radius of circle: '))
        d1 = 3 - (2*r)
        x = 0
        y = r
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POINTS)
        while(x<=y):
            glVertex2f((xc+x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc-y)/d)
            glVertex2f((xc+x)/d,(yc-y)/d)
            glVertex2f((xc+y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc-x)/d)
            glVertex2f((xc+y)/d,(yc-x)/d)
            if (d1<0):
                d1 = d1 + (4*x) + 6
            else:
                d1 = d1 + (4*(x-y)) +10
                y = y-1
            x = x+1
        glEnd()
        glFlush()
    else:
        print('Invalid Choice')


glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("Circle")
glutInitWindowSize(100, 100)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot_line)
clearScreen()
glutMainLoop()