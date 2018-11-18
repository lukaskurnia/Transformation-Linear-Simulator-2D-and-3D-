import numpy as np

# FUNGSI TRANSLASI MATRIKS
def translate2D(dimension,Mat,dx,dy):
# Melakukan translasi objek dengan menggeser nilai x sebesar dx
# dan menggeser nilai y sebesar dy untuk 2 dimensi
    "Ini prosedur rotation utuk 2 dimensi"
    #inisiasi matriks transformasi
    Mat2 = np.zeros((dimension,1))
    Mat3 = np.zeros((dimension,dimension))
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
    Mat2 = np.zeros((dimension,1))
    Mat3 = np.zeros((dimension,dimension))
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
    Mat2 = np.zeros((dimension,dimension))
    Mat3 = np.zeros((dimension,dimension))
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
        Mat2[2][1] = 0
        Mat2[2][2] = k
    #end if
    Mat3 = np.dot(Mat2,Mat)
    return Mat3

#FUNGSI ROTASI MATRIKS
def rotate2D(dimension,Mat,sudut,a,b):
# Melakukan rotasi objek secara berlawanan arah arum jam sebesar
# sudut terhadap titik a dan b untuk 2 dimensi
    "Ini prosedur rotation"
    #inisiasi matriks transformasi
    Mat2 = np.zeros((dimension,dimension))
    MatA = np.zeros((dimension,dimension))
    Mat3 = np.zeros((dimension,dimension))
    MatB = np.zeros((dimension,dimension))
    temp = np.zeros((dimension,1))

    temp[0][0] = a
    temp[1][0] = b
    Mat2[0][0] = np.cos(sudut)
    Mat2[0][1] = -np.sin(sudut)
    Mat2[1][0] = np.sin(sudut)
    Mat2[1][1] = np.cos(sudut)

    MatA = np.subtract(Mat,temp)
    MatB = np.dot(Mat2,MatA)
    Mat3 = np.add(MatB,temp)

    return Mat3

def rotate3D(dimension,Mat,sudut,parameter):
# def rotate3D(dimension,Mat,sudut,parameter):
# Melakukan rotasi objek secara berlawanan arah arum jam sebesar sudut pada sumbu dengan parameter x , y , atau z
    "Ini prosedur rotation"
    #inisiasi matriks transformasi
    Mat2 = np.zeros((dimension,dimension))
    Mat3 = np.zeros((dimension,dimension))

    if(parameter=='x'): #jika parameter adalah x
    #rotate benda 3 dimensi terhadap garis sumbu x
        Mat2[0][0] = 1
        Mat2[0][1] = 0
        Mat2[0][2] = 0
        Mat2[1][0] = 0
        Mat2[1][1] = np.cos(sudut)
        Mat2[1][2] = -np.sin(sudut)
        Mat2[2][0] = 0
        Mat2[2][1] = np.sin(sudut)
        Mat2[2][2] = np.cos(sudut)
    elif(parameter=='y'): #jika parameter adalah y
    #rotate benda 3 dimensi terhadap garis sumbu y
        Mat2[0][0] = np.cos(sudut)
        Mat2[0][1] = 0
        Mat2[0][2] = np.sin(sudut)
        Mat2[1][0] = 0
        Mat2[1][1] = 1
        Mat2[1][2] = 0
        Mat2[2][0] = -np.sin(sudut)
        Mat2[2][1] = 0
        Mat2[2][2] = np.cos(sudut)
    elif(parameter=='z'): #jika parameter adalah z
    #rotate benda 3 dimensi terhadap garis sumbu z
        Mat2[0][0] = np.cos(sudut)
        Mat2[0][1] = -np.sin(sudut)
        Mat2[0][2] = 0
        Mat2[1][0] = np.sin(sudut)
        Mat2[1][1] = np.cos(sudut)
        Mat2[1][2] = 0
        Mat2[2][0] = 0
        Mat2[2][1] = 0
        Mat2[2][2] = 1
    else:
        print('Input parameter hanya bisa x , y , atau z.')
        Mat2[0][0] = 1
        Mat2[0][1] = 0
        Mat2[0][2] = 0
        Mat2[1][0] = 0
        Mat2[1][1] = 1
        Mat2[1][2] = 0
        Mat2[2][0] = 0
        Mat2[2][1] = 0
        Mat2[2][2] = 1

    Mat3 = np.dot(Mat2,Mat)
    return Mat3

#FUNGSI REFLEKSI/PENCERMINAN MATRIKS
def reflect(dimension,Mat,parameter):
# Melakukan pencerminan objek. Nilai paraeter adalah suatu nilai-nilai :
# x,y,y=x,y=-x,atau(a,b). Nilai (a,b) adalah titik untuk melakukan pencerminan
    "Ini prosedure reflect"
    #inisiasi matriks transformasi
    Mat2 = np.zeros((dimension,dimension))
    Mat3 = np.zeros((dimension,dimension))
    if(dimension==2):
        if (parameter=='x'): #jika parameter adalah x
        #refelction benda 2 dimensi terhadap garis sumbu x
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = -1
            Mat3 = np.dot(Mat2,Mat)
        elif(parameter=='y'): #jika parameter adalah y
        #refelction benda 2 dimensi terhadap garis sumbu y
            Mat2[0][0] = -1
            Mat2[0][1] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat3 = np.dot(Mat2,Mat)
        elif(parameter=='y=x'): #jika parameter adalah y=x
        #refelction benda 2 dimensi terhadap garis y=x
            Mat2[0][0] = 0
            Mat2[0][1] = 1
            Mat2[1][0] = 1
            Mat2[1][1] = 0
            Mat3 = np.dot(Mat2,Mat)
        elif(parameter=='y=-x'): #jika parameter adalah y=-x
        #refelction benda 2 dimensi terhadap garis sumbu y=-x
            Mat2[0][0] = 0
            Mat2[0][1] = -1
            Mat2[1][0] = -1
            Mat2[1][1] = 0
            Mat3 = np.dot(Mat2,Mat)
        else: #(parameter=='(a,b)')
        #refelction benda 2 dimensi terhadap titik a,b
            try:
                temp = parameter.split('(')
                temp = temp[1].split(')')
                temp = temp[0].split(',')
                absis = (int(temp[0]))
                ordinat = (int(temp[1]))
                MatA = np.zeros((dimension,dimension))
                MatB = np.zeros((dimension,dimension))
                MatC = np.zeros((dimension,1))
                MatD = np.zeros((dimension,1))

                #inisiasi matriks transformasi pertama
                MatA[0][0] = -1
                MatA[0][1] = 0
                MatA[1][0] = 0
                MatA[1][1] = 1

                MatB[0][0] = 1
                MatB[0][1] = 0
                MatB[1][0] = 0
                MatB[1][1] = -1

                MatC[0][0] = 2*absis
                MatC[1][0] = 0

                MatD[0][0] = 0
                MatD[1][0] = 2*ordinat

                temp = np.add(np.dot(MatA,Mat),MatC)
                Mat3 = np.add(np.dot(MatB,temp),MatD)
            except:
                print('Input tidak ada.')
                Mat3=Mat

    elif(dimension==3):
        if(parameter=='x'): #jika parameter adalah x
        #reflection benda 3 dimensi terhadap garis sumbu x
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = -1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = -1
        elif(parameter=='y'): #jika parameter adalah y
        #refelction benda 3 dimensi terhadap garis sumbu y
            Mat2[0][0] = -1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = -1
        elif(parameter=='z'): #jika parameter adalah z
        #refelction benda 3 dimensi terhadap garis sumbu z
            Mat2[0][0] = -1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = -1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1
        elif(parameter=='xy'): #jika parameter adalah xy
        #refelction benda 3 dimensi terhadap bidang xy
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = -1
        elif(parameter=='yz'): #jika parameter adalah yz
        #refelction benda 3 dimensi terhadap bidag yz
            Mat2[0][0] = -1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1
        elif(parameter=='zx'): #jika parameter adalah zx
        #refelction benda 3 dimensi terhadap bidang zx
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = -1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1
        else:
            print('Input tidak ada.')
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1
        Mat3 = np.dot(Mat2,Mat)

    return Mat3

#FUNGSI SHEAR MATRIKS
def shear(dimension,Mat,parameter,k):
# Melakukan operasi shear pada objek. NIlai parameter dapat berupa
# x (terhadap sumbu x) atau y (terhadap sumbu y). Nilai k adalah faktor shear.
    "Ini prosedur shear"
    #inisiasi matriks transformasi
    Mat2 = np.zeros((dimension,dimension))
    Mat3 = np.zeros((dimension,dimension))
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
        else:
            print('Input tidak ada.')
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1

    elif(dimension==3):
        if(parameter=='x'): #jika parameter = x
            Mat2[0][0] = 1
            Mat2[0][1] = k
            Mat2[0][2] = k
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1
        elif(parameter=='y'): #jika parameter = y
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = k
            Mat2[1][1] = 1
            Mat2[1][2] = k
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1
        elif(parameter=='z'): #jika parameter = z
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = k
            Mat2[2][1] = k
            Mat2[2][2] = 1
        else:
            print('Input tidak ada.')
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1

    Mat3 = np.dot(Mat2,Mat)
    return Mat3

#FUNGSI STRETCH MATRIKS
def stretch(dimension,Mat,parameter,k):
# Melakukan operasi scretch pada objek. Nilai param dapat berupa x
# (terhadap sumbu x) atau y (terhadap sumbu y). Nilai k adalah faktor shear
    "Ini prosedur sretch"
    #inisiasi matriks transformasi
    Mat2 = np.zeros((dimension,dimension))
    Mat3 = np.zeros((dimension,dimension))
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
        else:
            print('Input tidak ada.')
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1

    elif(dimension==3):
        if(parameter=='x'): #jika paremeter berupa x (terhadap sumbu x)
            Mat2[0][0] = k
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1
        elif(parameter=='y'): #jika paremeter berupa y (terhadap sumbu y)
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = k
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1
        elif(parameter=='z'): #jika parameter berupa z (terhadap sumbu z)
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = k
        else:
            print('Input tidak ada.')
            Mat2[0][0] = 1
            Mat2[0][1] = 0
            Mat2[0][2] = 0
            Mat2[1][0] = 0
            Mat2[1][1] = 1
            Mat2[1][2] = 0
            Mat2[2][0] = 0
            Mat2[2][1] = 0
            Mat2[2][2] = 1

    Mat3 = np.dot(Mat2,Mat)
    return Mat3

#FUNGSI CUSTOM MATRIKS
def custom2D(dimension,Mat,a,b,c,d):
# Melakukan transformasi linier pada onjek dengan matriks transformasi
# sebagai berikut : [a b] untuk 2 dimensi
#                   [c d]
    "Ini prosedur custom"
    #inisiasi matriks transformasi
    Mat2 = np.zeros((dimension,dimension))
    Mat3 = np.zeros((dimension,dimension))
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
    Mat2 = np.zeros((dimension,dimension))
    Mat3 = np.zeros((dimension,dimension))
    Mat2[0][0] = (a)
    Mat2[0][1] = (b)
    Mat2[0][2] = (c)
    Mat2[1][0] = (d)
    Mat2[1][1] = (e)
    Mat2[1][2] = (f)
    Mat2[2][0] = (g)
    Mat2[2][1] = (h)
    Mat2[2][2] = (i)

    Mat3 = np.dot(Mat2,Mat)
    return Mat3
