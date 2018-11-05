import numpy as np
# Make

def twodimension():
    "Menu 2 Dimensi"
    print('Input banyaknya titik sudut bidang anda : ')
    N = (int(input('>> ')))
    Mat = np.zeros( (N,2) )
    print('\nInput titik sudut bidang : ')
    for i in range(N):
        S = input()
        Ss = S.split()
        Mat[i][0] = (int(Ss[0]))
        Mat[i][1] = (int(Ss[1]))
    return Mat

def threedimension():
    "Menu 3 Dimensi"
    Mat = np.zeros( (8,3) )
    print('Bidang 3 dimensi yg digunakan adalah kubus')
    print('Input titik sudut kubus : ')
    for i in range(8):
        S = input()
        Ss = S.split()
        Mat[i][0] = (int(Ss[0]))
        Mat[i][1] = (int(Ss[1]))
        Mat[i][2] = (int(Ss[2]))
    return Mat


def shape(dimension):
    "Ini prosedur membuat shape"
    if dimension == 2:
        return twodimension()
    elif dimension == 3:
        return threedimension()
