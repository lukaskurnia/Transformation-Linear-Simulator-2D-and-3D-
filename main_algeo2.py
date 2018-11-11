# Program utama Tugas Besar 2 Aljabar Geometri
import os
import menu
import make
import menutransform as mt
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

os.system('cls')
dimension = menu.mainmenu()
Mat = make.shape(dimension)
mt.menu(dimension,Mat)
