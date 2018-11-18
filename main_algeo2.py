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
dimension = menu.mainmenu() #Menerima input dimensi yang diinginkan oleh user
if (dimension != 0):
    Mat = make.shape(dimension)

    if(dimension==2):
        pt.displayWindow2D()
        pt.Print2D(np.transpose(Mat))
        mt.menu(dimension,Mat)
    else: #dimension == 3D
        pt.displayWindow3D()
        pt.Print3D(np.transpose(Mat))
        mt.menu(dimension,Mat)
