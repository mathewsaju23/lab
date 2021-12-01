import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)

def ROUND(a):
    return int((a+0.4)/100)

def plot():
    print('1. Polar')
    print('2. Non-Polar')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        xc = int(input('X centre: '))
        yc = int(input('Y centre: '))
        xr = int(input('X radius: '))
        yr = int(input('Y radius: '))
        theta = 0
        theta_end = 2*(3.14)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0,0.0,0.0)
        glPointSize(5.0)
        glBegin(GL_POINTS)
        while(theta <= theta_end):
            x = xr*(math.cos(theta)) 
            y = yr*(math.sin(theta)) 
            glVertex2f((x + xc)/100,(y + yc)/100)
            theta = theta + 0.001
        glEnd()
        glFlush()

    elif choice == 2:
        xc = int(input('X centre: '))
        yc = int(input('Y centre: '))
        xr = int(input('X radius: '))
        yr = int(input('Y radius: '))
        x = -xr
        b = yr
        a = xr
        
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0,0.0,0.0)
        glPointSize(5.0)
        glBegin(GL_POINTS)
        while(x < 0):
            v = 1-((x/a)*(x/a))
            y = b* (math.sqrt(v))
            glVertex2f((x + xc)/100,(y + yc)/100)
            glVertex2f((-x + xc)/100, (y + yc)/100)
            glVertex2f((-x + xc)/100, (-y + yc)/100)
            glVertex2f((x + xc)/100, (-y + yc)/100)
            x = x + 0.01
        glEnd()
        glFlush()

    else:
        print('Invalid Choice')






glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("ellipse")
glutInitWindowSize(100, 100)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot)
clearScreen()
glutMainLoop()


# glBegin(GL_LINES)
# glVertex2f(x1/10, y1/10)
# glVertex2f(x2/10, y2/10)