import pygame
import numpy as np
from pygame.locals import*
from OpenGL.GLUT import *
from OpenGL.GL import*
from OpenGL.GLU import*


print('Input banyaknya titik sudut bidang anda : ')
N = (int(input('>> ')))
Mat = np.zeros( (N,2) )
print('\nInput titik sudut bidang : ')
for i in range(N):
    S = input()
    Ss = S.split(',')
    Mat[i][0] = (int(Ss[0]))
    Mat[i][1] = (int(Ss[1]))

vertices= Mat

edges = (
    (0,1),
    (0,2),
    (1,2)
)


def Maker():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex2fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (1000,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)



    gluPerspective(90, 1, 0.1, 500.0)

    glTranslatef(0.0,0.0, -500.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Maker()
        pygame.display.flip()
        pygame.time.wait(10)

main()
