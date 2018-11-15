import pygame
import numpy as np
from pygame.locals import*
from OpenGL.GLUT import *
from OpenGL.GL import*
from OpenGL.GLU import*

def displayWindow2D(): #Membuat layar pygame untuk 2 dimensi
    pygame.init()
    display = (1000,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(90, display[0]/display[1], 0.1, 500.0)
    glTranslatef(0.0,0.0, -500.0)

def displayWindow3D(): #Membuat layar pygame untuk 3 dimensi
    pygame.init()
    display = (1000,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, display[0]/display[1], 0.1, 1500.0)
    glTranslatef(0.0,0.0, -1200.0)
    gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0)

def sumbuX(): #Sumbu X diberi warna HIJAU
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex3f(-500,0,0)
    glVertex3f(500,0,0)
    glEnd()

def sumbuY(): #Sumbu Y diberi warna MERAH
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0,-500,0)
    glVertex3f(0,500,0)
    glEnd()

def sumbuZ(): #Sumbu Z diberi warna BIRU
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex3f(0,0,-500)
    glVertex3f(0,0,500)
    glEnd()

def Sumbu2D(): #Rendering sumbu pembentuk window 2 dimensi
    sumbuX()
    sumbuY()

def Sumbu3D(): #Rendering sumbu pembentuk window 3 dimensi
    sumbuX()
    sumbuY()
    sumbuZ()

def Maker2D(Mat):
    glBegin(GL_POLYGON)

    vertices= Mat #Menyalin isi matriks pembentuk bangun datar input dari user

    #Bagian membuat Matriks berisi sisi bangun datar
    N= len(Mat)
    Matedge = np.zeros((N,2))
    for i in range(N-1):
        Matedge[i][0] = int(i)
        Matedge[i][1] = int(i) + 1
    Matedge[N-1][0] = int(N)-1
    Matedge[N-1][1] = 0

    edges = Matedge #Matriks sisi disalin

    glColor3f(1,1,0)
    for edge in edges: #Membuat bidang dari titik dan sisi yang ada
        for vertex in edge:
            glVertex2fv(vertices[int(vertex)])
    glEnd()

def Maker3D(Mat):
    edges = [ #Titik sudut yang dapat membentuk rusuk
    	[0,1],
    	[0,3],
    	[0,4],
    	[2,1],
    	[2,3],
    	[2,7],
    	[6,3],
    	[6,4],
    	[6,7],
    	[5,1],
    	[5,4],
    	[5,7]
    	]


    colors = ( #List warna
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,1,0),
	(1,0,0),
	(1,1,1),
	(1,0,0),
	(0,1,1),
	(0,1,0),
	(0,0,1),
	(1,0,0),
	(1,0,0),
	(0,0,1),
	(0,1,1),
	)


    surfaces = [     #Kumpulan rusuk yang dapat membentuk bidang
	(4,0,3,6),
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2)
	]


    glBegin(GL_QUADS) #Membuat bidang bidang sehingga terbentuk bangun ruang
    for surface in surfaces:
        x=0
        for vertex in surface:
            x +=1
            glColor3fv(colors[x])
            glVertex3fv(Mat[vertex])
    glEnd()

    glBegin(GL_LINES) #Membuat rusuk (Garis)
    for edge in edges:
        for indeks in edge:
                glColor3fv((0,0,0))
                glVertex3f(Mat[indeks][0],Mat[indeks][1],Mat[indeks][2])
    glEnd()


    # glBegin(GL_QUADS)# top
    # glColor3f(1.0, 0.0, 0.0)
    # glNormal3f(0.0, 1.0, 0.0)
    # glVertex3f(-1, 1, 1)
    # glVertex3f(1, 1, 1)
    # glVertex3f(1, 1, -1)
    # glVertex3f(-1, 1, -1)
    # glEnd()
    #
    # glBegin(GL_QUADS)
    # glColor3f(0.0, 1.0, 0.0)
    # glNormal3f(0.0, 0.0, 1.0)
    # glVertex3f(1, -1, 1)
    # glVertex3f(1, 1, 1)
    # glVertex3f(-1, 1, 1)
    # glVertex3f(-1, -1, 1)
    # glEnd()
    #
    # glBegin(GL_QUADS)# right
    # glColor3f(0.0, 0.0, 1.0)
    # glNormal3f(1.0, 0.0, 0.0)
    # glVertex3f(1, 1, -1)
    # glVertex3f(1, 1, 1)
    # glVertex3f(1, -1, 1)
    # glVertex3f(1, -1, -1)
    # glEnd()
    #
    # glBegin(GL_QUADS)# let
    # glColor3f(0.0, 0.0, 1)
    # glNormal3f(-1.0, 0.0, 0.0)
    # glVertex3f(-1, -1, 1)
    # glVertex3f(-1, 1, 1)
    # glVertex3f(-1, 1, -1)
    # glVertex3f(-1, -1, -1)
    # glEnd()
    #
    # glBegin(GL_QUADS)# bottom
    # glColor3f(1, 0.0, 0.0)
    # glNormal3f(0.0, -1.0, 0.0)
    # glVertex3f(1, -1, 1)
    # glVertex3f(-1, -1, 1)
    # glVertex3f(-1, -1, -1)
    # glVertex3f(1, -1, -1)
    # glEnd()
    #
    # glBegin(GL_QUADS)	# back
    # glColor3f(0.0, 1, 0.0)
    # glNormal3f(0.0, 0.0, -1.0)
    # glVertex3f(1, 1, -1)
    # glVertex3f(1, -1, -1)
    # glVertex3f(-1, -1, -1)
    # glVertex3f(-1, 1, -1)
    # glEnd()

def Print2D(Mat): #Print window menu 2 dimensi ke layar
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Sumbu2D()
    Maker2D(Mat)
    pygame.display.flip()

def Print3D(Mat): #Print window 3 dimensi ke layar
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Maker3D(Mat)
    Sumbu3D()
    pygame.display.flip()
