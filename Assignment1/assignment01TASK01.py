from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
#sky
col=[0.0,0.0,0.0]
#direction
dir=0
def sky(key,x,y):
    global col
    if key==b'd' and col[0]<1.0 and col[1]<1.0 and col[2]<1.0:
        col[0]+=0.1
        col[1]+=0.1
        col[2]+=0.1
        print("day")
    elif key==b'n' and col[0]>0.0 and col[1]>0.0 and col[2]>0.0:
        col[0]-=0.1
        col[1]-=0.1
        col[2]-=0.1
        print("night")
    glutPostRedisplay()

def draw_line(x,x1,y,y1):
    glLineWidth(1)
    glColor3f(101/255, 188/255, 239/255) 
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glColor3f(0.0, 0.0, 0.0) 
    glVertex2f(x1,y1)


    glEnd()

def draw_points():
    glColor3f(col[0], col[1], col[2]) 
    glBegin(GL_QUADS)
    glVertex2f(0,350)
    glVertex2f(0,500)
    glVertex2f(500,500)
    glVertex2f(500,350)
     #jekhane show korbe pixel
    glEnd()


    glColor3f(164/255, 105/255, 45/255) 
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(0,350)
    glVertex2f(500,0)
    
    glVertex2f(500,0)
    glVertex2f(500,350)
    glVertex2f(0,350) #jekhane show korbe pixel
    glEnd()

# tree
def tree_triangle(x1,x2,x3,y1,y2,y3):
    glColor3f(37/255, 210/255, 55/255) 
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)

    glEnd()
def tree():
    x1=0
    y1=300
    x2=50
    y2=300
    x3=25
    y3=370
    for i in range(10):
        tree_triangle(x1,x2,x3,y1,y2,y3)
        x1+=50
        x2+=50
        x3+=50

#House

def house_draw():
    #base
    glColor3f(236/255, 226/255, 195/255) 
    glBegin(GL_QUADS)
    glVertex2f(100,200)
    glVertex2f(400,200)
    glVertex2f(400,300)
    glVertex2f(100,300)
    glEnd()

     #jekhane show korbe pixel
     #roof
    glColor3f(16/255, 49/255, 138/255) 
    glBegin(GL_TRIANGLES)
    glVertex2f(90,300)
    glVertex2f(410,300)
    glVertex2f(250,380)
    
    glEnd()
    
    #window
    glColor3f(101/255, 188/255, 239/255) 
    glBegin(GL_QUADS)
    glVertex2f(160,230)
    glVertex2f(200,230)
    glVertex2f(200,270)
    glVertex2f(160,270)
    glEnd()

    glColor3f(101/255, 188/255, 239/255) 
    glBegin(GL_QUADS)
    glVertex2f(340,230)
    glVertex2f(300,230)
    glVertex2f(300,270)
    glVertex2f(340,270)
    glEnd()   

    #Door
    glColor3f(101/255, 188/255, 239/255) 
    glBegin(GL_QUADS)
    glVertex2f(230,200)
    glVertex2f(270,200)
    glVertex2f(270,270)
    glVertex2f(230,270)
    glEnd()

    #Lines in windows
    glColor3f(0.0, 0.0, 0.0) 
    glBegin(GL_LINES)
    glVertex2f(180,230)
    glVertex2f(180,270)

    glVertex2f(160,250)
    glVertex2f(200,250)
    #FOR SCEOND LINE
    glVertex2f(320,230)
    glVertex2f(320,270)

    glVertex2f(300,250)
    glVertex2f(340,250)
    glEnd()

    #FOR DOOR LOCK
    glPointSize(8)
    glColor3f(0.0, 0.0, 0.0) 
    glBegin(GL_POINTS)
    glVertex2f(260,240)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    #xmin,xmax,ymin,ymax,zmin,zmax
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def animate():
    #//codes for any changes in Models, Camera
    rains(50,10)
    glutPostRedisplay()

#rains
def rains(col,drops):
    global dir
    x=0
    diffrence=10
    for i in range(col):
        for j in range(drops):
            y= random.randint(0,500)
            x1=x+dir
            y1=y-random.randint(5,15)
            draw_line(x,x1,y,y1)
        x+=diffrence

def angle_change(key,x,y):
    global dir
    if key==GLUT_KEY_RIGHT:
        if dir<5:
            dir+=1
            print("Right")
    if key==GLUT_KEY_LEFT:
        if dir>-5:
            dir-=1
            print("Left")

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #3/255,4/255 ei sequence e colour
    #call the draw methods here
    
    draw_points()
    tree()
    house_draw()
    rains(50,20)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(250, 250)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutKeyboardFunc(sky)
glutIdleFunc(animate)
glutSpecialFunc(angle_change)
glutMainLoop()
