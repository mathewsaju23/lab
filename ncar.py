from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame import mixer
import random

from math import pi,  radians, sin, cos

import sys


# Default Values
WINDOW_SIZE = 600
car_ref = [-WINDOW_SIZE + 200,-50]
car_length = 150
car_height = 100
car_tyreRadius = car_length * 0.15
speed = 2
TO_RIGHT = True

mixer.init()
mixer.music.load("./horn.mp3")
mixer.music.set_volume(0.7)

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def draw_circle(RADIUS, x, y):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(361):
        glColor3f(random.randint(0,1), random.randint(0,1), random.randint(0,1))
        glVertex2f(RADIUS * cos( pi * i / 180) + x, RADIUS * sin( pi * i / 180) + y)
    glEnd()

def controls(key, x, y):
    global TO_RIGHT, speed
    if key == b"d":
        speed = speed + 1
    elif key == b"a":
        speed = speed - 1
    elif key == b"r":
        TO_RIGHT = False
    elif key == b"f":
        TO_RIGHT = True
    elif key == b"h":
        mixer.music.play()
    

def draw_line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(-WINDOW_SIZE, 0)
    glVertex2f(WINDOW_SIZE, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-WINDOW_SIZE, -car_height)
    glVertex2f(WINDOW_SIZE, -car_height)
    glEnd() 

def drawCar():

    vertices = [
        [car_ref[0], car_ref[1]],
        [car_ref[0], car_ref[1] +  car_height],
        [car_ref[0] + car_length * 0.75, car_ref[1] + car_height],
        [car_ref[0] + car_length , car_ref[1] + car_height * 0.4],
        [car_ref[0] + car_length, car_ref[1]],
    ]

    tyres = [
        [car_ref[0]+car_length*0.20, car_ref[1]],
        [car_ref[0]+car_length*0.80, car_ref[1]],
    ]


    glLineWidth(2.0)
    glBegin(GL_POLYGON)

    for i in vertices:
        glVertex2fv(i)
    
    glEnd()

    # Car tyres
    for i in tyres:
        draw_circle(car_tyreRadius, i[0],i[1])

    glutSwapBuffers()

def update(value):
    if TO_RIGHT:
        car_ref[0] +=  speed * 1
    else:
        car_ref[0] -=  speed * 1

    glutPostRedisplay()
    glutTimerFunc(int(1000/60), update, 0)
    

def display():
    draw_line()
    drawCar()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("ANIMATED CAR")
    glutDisplayFunc(display)
    glutKeyboardFunc(controls)
    glutTimerFunc(0, update, 0)
    glutIdleFunc(display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()