# Program utama Tugas Besar 2 Aljabar Geometri
import os
import menu
import make
import menutransform as mt
import print as pt
import numpy as np
import pygame
from OpenGL.GLUT import *
from OpenGL.GL import*
from OpenGL.GLU import*
from pygame.locals import*



os.system('cls')
dimension = menu.mainmenu()
if (dimension != 0):
    #tampilan pygame
    pygame.init()
    display = (1000,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(90, 1, 0.1, 500.0)
    glTranslatef(0.0,0.0, -500.0)

    Mat = make.shape(dimension)
    pt.Print(np.transpose(Mat))
    mt.menu(dimension,Mat)
