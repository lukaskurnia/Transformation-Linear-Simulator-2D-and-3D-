# Nama File : transformasi.py
# Deskripsi : fungsi dan posedure untuk operasi matriks
# Tanggal   : 1 November 2018
# Kelompok  : Los Santos

import numpy as np

# FUNGSI TRANSLASI MATRIKS
def translate2D(dimension,Mat,dx,dy):
# Melakukan translasi objek dengan menggeser nilai x sebesar dx
# dan menggeser nilai y sebesar dy untuk 2 dimensi
    "Ini prosedur rotation utuk 2 dimensi"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,1)
    Mat3 = np.zeros(dimension,dimension)
    Mat2[0][0] = dx
    Mat2[1][0] = dy

    Mat3 = np.add(Mat,Mat2)
    return Mat3

def translate3D(dimension,Mat,dx,dy,dz):
# Melakukan translasi objek dengan menggeser nilai x sebesar dx,
# menggeser nilai y sebesar dy dan menggeser nilai z sebesar dz
# untuk 3 dimensi
    "Ini prosedur rotation untuk 3 dimensi"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,1)
    Mat3 = np.zeros(dimension,dimension)
    Mat2[0][0] = dx
    Mat2[1][0] = dy
    Mat2[2][0] = dz

    Mat3 = np.add(Mat,Mat2)
    return Mat3

#FUNGSI DILATASI MATRIKS
def dilate(dimension,Mat,k):
# Melakukan dilatasi objek dengan faktor scaling k
    "Ini prosedure dilate"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,dimension)
    Mat3 = np.zeros(dimension,dimension)
    if(dimension==2): #matriks transformasi untuk dimensi 2
        Mat2[0][0] = k
        Mat2[0][1] = 0
        Mat2[1][0] = 0
        Mat2[1][1] = k
    elif(dimension==3): #matriks transformasi untuk dimensi 3
        Mat2[0][0] = k
        Mat2[0][1] = 0
        Mat2[0][2] = 0
        Mat2[1][0] = 0
        Mat2[1][1] = k
        Mat2[1][2] = 0
        Mat2[2][0] = 0
        Mat2[2][0] = 0
        Mat2[2][0] = k
    #end if
    Mat3 = np.dot(Mat2,Mat)
    return Mat3

#FUNGSI ROTASI MATRIKS
def rotate2D(dimension,Mat,sudut,a,b):
# Melakukan rotasi objek secara berlawanan arah arum jam sebesar
# sudut terhadap titik a dan b untuk 2 dimensi
    "Ini prosedur rotation"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,dimension)
    MatA = np.zeros(dimension,dimension)
    Mat3 = np.zeros(dimension,dimension)
    MatB = np.zeros(dimension,dimension)
    temp = np.zeros(dimension,1)
    temp[0][0] = a
    temp[1][0] = b
    Mat2[0][0] = np.cos(sudut)
    Mat2[0][1] = -np.sin(sudut)
    Mat2[1][0] = np.sin(sudut)
    Mat2[1][1] = np.cos(sudut)

    MatA = np.substract(Mat,temp)
    MatB = np.dot(Mat2,MatA)
    Mat3 = np.add(MatB,temp)

    return Mat3

def rotate3D(dimension,Mat,sudut,a,b,c):
# Melakukan rotasi objek secara berlawanan arah arum jam sebesar
# sudut terhadap vektor normal a, b, dan c untuk 3 dimensi
    "Ini prosedur rotation"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,dimension)
    Mat3 = np.zeros(dimension,dimension)
    Mat2[0][0] = a*a*(1-np.cos(sudut)) + np.cos(sudut)
    Mat2[0][1] = a*b*(1-np.cos(sudut)) - c*(np.sin(sudut))
    Mat2[0][2] = a*c*(1-np.cos(sudut)) + b*(np.sin(sudut))
    Mat2[1][0] = a*b*(1-np.cos(sudut)) + c*(np.sin(sudut))
    Mat2[1][1] = b*b*(1-np.cos(sudut)) + np.cos(sudut)
    Mat2[1][2] = b*c*(1-np.cos(sudut)) - a*(np.sin(sudut))
    Mat2[2][0] = a*c*(1-np.cos(sudut)) - b*(np.sin(sudut))
    Mat2[2][0] = b*c*(1-np.cos(sudut)) + a*(np.sin(sudut))
    Mat2[2][0] = c*c*(1-np.cos(sudut)) + np.cos(sudut)

    Mat3 = np.dot(Mat2,Mat)
    return Mat3

#FUNGSI REFLEKSI/PENCERMINAN MATRIKS
def reflect(dimension,Mat,parameter):
# Melakukan pencerminan objek. Nilai paraeter adalah suatu nilai-nilai :
# x,y,y=x,y=-x,atau(a,b). Nilai (a,b) adalah titik untuk melakukan pencerminan
    "Ini prosedure reflect"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,dimension)
    Mat3 = np.zeros(dimension,dimension)
    if(dimesion ==2):
        if(parameter=='(a,b)'):
            MatA = np.zeros(dimension,dimension)
            MatB = np.zeros(dimension,dimension)
            MatC = no,zeros(dimension,1)
            MatD = no,zeros(dimension,1)
            #inisiasi matriks transformasi pertama
            MatA[0][0] = -1
            MatA[0][1] = 0
            MatA[1][0] = 0
            MatA[1][1] = 1

            MatB[0][0] = 1
            MatB[0][1] = 0
            MatB[1][0] = 0
            MatB[1][1] = -1

            MatC[0][0] = 2*a
            MatC[1][0] = 0

            MatD[0][0] = 0
            MatD[1][0] = 2*b

            temp = np.add(np.dot(MatA,Mat),MatC)
            Mat3 = np.add(np.dot(MatB,temp),MatD)

        else
            if (parameter=='x'):
                Mat2[0][0] = 1
                Mat2[0][1] = 0
                Mat2[1][0] = 0
                Mat2[1][1] = -1
            elif(parameter=='y'):
                Mat2[0][0] = -1
                Mat2[0][1] = 0
                Mat2[1][0] = 0
                Mat2[1][1] = 1
            elif(parameter=='y=x'):
                Mat2[0][0] = 0
                Mat2[0][1] = 1
                Mat2[1][0] = 1
                Mat2[1][1] = 0
            elif(parameter=='y=-x'):
                Mat2[0][0] = 0
                Mat2[0][1] = -1
                Mat2[1][0] = -1
                Mat2[1][1] = 0
            Mat3 = np.dot(Mat2,Mat)

    # elif(dimension==3):

    return Mat3

#FUNGSI SHEAR MATRIKS
def shear(dimension,Mat,parameter,k):
# Melakukan operasi shear pada objek. NIlai parameter dapat berupa
# x (terhadap sumbu x) atau y (terhadap sumbu y). Nilai k adalah faktor shear.
    "Ini prosedur shear"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,dimension)
    Mat3 = np.zeros(dimension,dimension)
    if(dimension==2):
        if(parameter=='x'):
            Mat2[0][0] = 1
            Mat2[0][1] = k
            Mat2[1][0] = 0
            Mat2[1][1] = 1
        elif(parameter=='y'):
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[1][0] = k
            Mat2[1][1] = 1
    # elif(dimension==3):


    Mat3 = np.dot(Mat2,Mat)
    return Mat3

#FUNGSI STRETCH MATRIKS
def stretch(dimension):
# Melakukan operasi scretch pada objek. Nilai param dapat berupa x
# (terhadap sumbu x) atau y (terhadap sumbu y). Nilai k adalah faktor shear
    "Ini prosedur sretch"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,dimension)
    Mat3 = np.zeros(dimension,dimension)
    if(dimension==2):
        if(parameter=='x'): #jika parameter berupa x (terhadap sumbu x)
            Mat2[0][0] = k
            Mat2[0][1] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
        elif(parameter=='y'): #jika parameter berupa y (terhadap sumbu y)
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = k
    elif(dimension==3):
        if(parameter=='x'): #jika paremeter berupa x (terhadap sumbu x)
            Mat2[0][0] = k
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][0] = 0
            Mat2[2][0] = 1
        elif(paremeter=='y'): #jika paremeter berupa y (terhadap sumbu y)
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = k
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][0] = 0
            Mat2[2][0] = 1
        elif(paremeter=='z'): #jika parameter berupa z (terhadap sumbu z)
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][0] = 0
            Mat2[2][0] = k

    Mat3 = np.dot(Mat2,Mat)
    return Mat3

#FUNGSI CUSTOM MATRIKS
def custom2D(dimension,Mat,a,b,c,d):
# Melakukan transformasi linier pada onjek dengan matriks transformasi
# sebagai berikut : [a b] untuk 2 dimensi
#                   [c d]
    "Ini prosedur custom"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,dimension)
    Mat3 = np.zeros(dimension,dimension)
    Mat2[0][0] = (a)
    Mat2[0][1] = (b)
    Mat2[1][0] = (c)
    Mat2[1][1] = (d)

    Mat3 = np.dot(Mat2,Mat)
    return Mat3

def custom3D(dimension,Mat,a,b,c,d,e,f,g,h,i):
# Melakukan transformasi linier pada onjek dengan matriks transformasi
# sebagai berikut : [a b] untuk 3 dimensi
#                   [c d]
    "Ini prosedur custom"
    #inisiasi matriks transformasi
    Mat2 = np.zeros(dimension,dimension)
    Mat3 = np.zeros(dimension,dimension)
    Mat2[0][0] = (a)
    Mat2[0][1] = (b)
    Mat2[0][2] = (c)
    Mat2[1][0] = (d)
    Mat2[1][1] = (e)
    Mat2[1][2] = (f)
    Mat2[2][0] = (g)
    Mat2[2][1] = (h)
    Mat2[2][2] = (i)

    Mat3 = np.dot(Mat2,Mat2)
    return Mat3
