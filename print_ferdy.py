import pygame
import numpy as np
from pygame.locals import*
from OpenGL.GLUT import *
from OpenGL.GL import*
from OpenGL.GLU import*


# print('Input banyaknya titik sudut bidang anda : ')
# N = (int(input('>> ')))
# Mat = np.zeros( (N,2) )
# print('\nInput titik sudut bidang : ')
# for i in range(N):
#     S = input()
#     Ss = S.split(',')
#     Mat[i][0] = (int(Ss[0]))
#     Mat[i][1] = (int(Ss[1]))


def Sumbu():
    glBegin(GL_LINES)

    koordinatinti= (
        (0,0),
        (500,0),
        (-500,0),
        (0,500),
        (0,-500)
    )

    garisinti= (
        (0,1),
        (0,2),
        (0,3),
        (0,4)
    )

    for garis in garisinti:
        for koordinat in garis:
            glVertex2fv(koordinatinti[koordinat])
    glEnd()

def Maker(Mat):
    glBegin(GL_POLYGON)
    vertices= Mat

    N= len(Mat)
    Matedge = np.zeros((N,2))
    for i in range(N-1):
        Matedge[i][0] = int(i)
        Matedge[i][1] = int(i) + 1
    Matedge[N-1][0] = int(N)-1
    Matedge[N-1][1] = 0

    edges = Matedge

    for edge in edges:
        for vertex in edge:
            glVertex2fv(vertices[int(vertex)])
    glEnd()

def Print(Mat):


    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    pygame.init()
    display = (1000,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(90, 1, 0.1, 500.0)
    glTranslatef(0.0,0.0, -500.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Sumbu()
    Maker(Mat)
    pygame.display.flip()
    #pygame.time.wait(10)
