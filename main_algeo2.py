# Program utama Tugas Besar 2 Aljabar Geometri
import os
import menu
import make
import menutransform as mt
import print as pt
import numpy as np

os.system('cls')
dimension = menu.mainmenu()
Mat = make.shape(dimension)
pt.Print(np.transpose(Mat))
mt.menu(dimension,Mat)
