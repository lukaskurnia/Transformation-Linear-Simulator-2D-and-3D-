# Program utama Tugas Besar 2 Aljabar Geometri
import os
import menu
import make

os.system('clear')
dimension = menu.mainmenu()
Mat = make.shape(dimension)
print(Mat)
