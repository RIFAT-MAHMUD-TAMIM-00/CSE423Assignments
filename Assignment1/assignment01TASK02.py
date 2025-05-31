from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 
W_Width,W_Height=500,500
balls=[]
blink=False
freeze=False
bl_time=0
speed=0.02
Xmin, Xmax,Ymin, Ymax = 0, W_Width,0, W_Height
def coordinate(x,y):
    global W_Width,W_Height
    m=x
    n=W_Width-y
    return m,n
    
def draw_points(x,y,s,color):
    a,b,c=color
    glColor3f(a,b,c)
    glPointSize(s)
    glBegin(GL_POINTS)
    glVertex2f(x,y) 

    glEnd() 

def draw_square(x0,y0,x1,y1,x2,y2,x3,y3,s):    

    glColor3f(0,0,0)

    glLineWidth(s)

    glBegin(GL_LINES)
    glVertex2f(x0,y0)
    glVertex2f(x1,y1)

    glVertex2f(x2,y2)

    glVertex2f(x2,y2)

    

    glVertex2f(x3,y3)

    glVertex2f(x1,y1)

    glEnd()


def mouseListener(button, state,x, y):########
    global balls,blink,freeze
    if button == GLUT_LEFT_BUTTON and not freeze:
        if state == GLUT_DOWN:
            blink= True
    if button==GLUT_RIGHT_BUTTON and not freeze:
        if state == GLUT_DOWN:  
            x0,x1=coordinate(x,y)
            a=random.uniform(0,1)
            b=random.uniform(0,1)
            c=random.uniform(0,1)
            dirX = random.choice([-1,1])
            dirY=random.choice([-1,1])
            balls.append([x0,x1,(a,b,c),dirX,dirY])
  
def freeze_balls(key,x,y):
    global freeze
    if key==b' ':
        freeze= not freeze
def Speed(key, x, y):##########3
    global speed
    if key== GLUT_KEY_DOWN and not freeze:
        speed /= 1.5
        print("decreased")  
    if key==GLUT_KEY_UP and not freeze:
        speed *= 1.5
        print("increased")

def random_points():
    global balls,freeze
    for i in balls:
            if blink:
                draw_points(i[0], i[1],7,(0,0,0))
            else:
                draw_points(i[0], i[1], 7,i[2])

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    random_points()
    draw_square(0,0,500,0,500,500,0,500,5)
   
    glutSwapBuffers()


def animate():
    global speed,balls,blink,bl_time,Xmin, Xmax,Ymin, Ymax
    if not freeze:    
        glutPostRedisplay()      
        for p in balls:
            p[0]=p[0]+(p[-2]*speed)
            p[1]=p[1]+(p[-1]*speed)
            if p[0] <= Xmin or p[0] >=Xmax:
                p[-2]=p[-2]*-1
            if p[1] <= Ymin or p[1] >=Ymax:
                p[-1]=p[-1]*-1   
        if blink:
            bl_time= bl_time+1
            if bl_time>=100:
                blink=False
                bl_time=0

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(250, 250)
wind = glutCreateWindow(b"OpenGL Coding Practice")

glutDisplayFunc(display)  
glutMouseFunc(mouseListener)
glutSpecialFunc(Speed)
glutKeyboardFunc(freeze_balls)
glutIdleFunc(animate)
glutMainLoop()















