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
    print(Mat)

def threedimension():
    "Menu 3 Dimensi"
    print('ini adalah menu 3 dimensi')


def shape(dimension):
    "Ini prosedur membuat shape"
    if dimension == 2:
        twodimension()
    elif dimension == 3:
        threedimension()
