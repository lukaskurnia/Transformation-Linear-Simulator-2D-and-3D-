# Program utama Tugas Besar 2 Aljabar Geometri
import os
import menu
import make

os.system('cls')
dimension = menu.mainmenu()
Mat = make.shape(dimension)
print(Mat)
