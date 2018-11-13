import numpy as np
# Make

def isInt(x):
    i = 0
    try:
        i = int(x)
        integer=True
    except:
        integer = False
    return integer

def isNValid2D(x):
    i = 0
    try:
        i = int(x)
        if(i>=3):
            integer=True
        else:
            integer=False
    except:
        integer = False
    return integer

def isTitikValid(x):
    i = 0
    val = False
    while(i<len(x) and val==False):
        if(x[i]==','):
            val = True
        else:
            i = i+1
    return val

def twodimension():
    "Menu 2 Dimensi"
    print('Input banyaknya titik sudut bidang anda : ')
    x = input('>> ')
    while (isNValid2D(x)==False):
        print('Input harus bilangan bulat minimal 3')
        x = input('>> ')
    #input harus >= 3

    N = (int(x))
    Mat = np.zeros( (N,2) )
    print('\nInput titik sudut bidang : ')
    for i in range(N):
        print('Input titik ke ', i+1)
        S = input()
        while (isTitikValid(S)==False):
            print('Input titik ke ', i+1)
            S = input()
        Ss = S.split(',')
        Mat[i][0] = (int(Ss[0]))
        Mat[i][1] = (int(Ss[1]))
    return Mat.transpose()

def threedimension():
    "Menu 3 Dimensi"
    Mat = np.zeros( (8,3) )
    print('Bidang 3 dimensi yg digunakan adalah kubus')
    print('Input titik sudut kubus : ')
    for i in range(8):
        S = input()
        Ss = S.split(',')
        Mat[i][0] = (int(Ss[0]))
        Mat[i][1] = (int(Ss[1]))
        Mat[i][2] = (int(Ss[2]))
    return Mat.transpose()

def shape(dimension):
    "Ini prosedur membuat shape"
    if dimension == 2:
        return twodimension()
    elif dimension == 3:
        return threedimension()
