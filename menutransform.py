import numpy as np
import os
import print as pt
import transformasi as tr
from math import pi
# Transform
# N.B : Fungsi yang memiliki parameter berbeda untuk ruang 2D dan 3D
# translate
# rotate
# custom

def isFloat(x):
    i = 0
    try:
        i = float(x)
        bool = True
    except:
        bool = False
    return bool


def menu(dimension,Mat):
    "Menu Transformasi"
    os.system('cls')
    Matinit = Mat
    print('Pilih transformasi yang diinginkan')
    choice = 'input'
    while not(choice == 'exit'):
        choice = input('>> ')
        S = choice.split()
        if S[0] == 'translate':
            if (dimension == 2):
                dx = (float(S[1]))
                dy = (float(S[2]))
                Mat = tr.translate2D(dimension,Mat,dx,dy)
                pt.Print(np.transpose(Mat))
            elif (dimension == 3):
                dx = (float(S[1]))
                dy = (float(S[2]))
                dz = (float(S[3]))
                Mat = tr.translate3D(dimension,Mat,dx,dy,dz)
                pt.Print(np.transpose(Mat))
        elif S[0] == 'dilate':
            k = (float(S[1]))
            Mat = tr.dilate(dimension,Mat,k)
            pt.Print(np.transpose(Mat))
        elif S[0] == 'rotate':
            if (dimension == 2):
                sudut = (float(S[1]))
                a = (float(S[2]))
                b = (float(S[3]))
                Mat = tr.rotate2D(dimension,Mat,sudut/180*pi,a,b)
                pt.Print(np.transpose(Mat))
            elif (dimension == 3):
                sudut = (float(S[1]))
                a = (float(S[2]))
                b = (float(S[3]))
                c = (float(S[4]))
                Mat = tr.rotate3D(dimension,Mat,sudut/180*pi,a,b,c)
                pt.Print(np.transpose(Mat))
        elif S[0] == 'reflect':
            param = S[1]
            Mat = tr.reflect(dimension,Mat,param)
            pt.Print(np.transpose(Mat))
        elif S[0] == 'shear':
            param = S[1]
            k = (float(S[2]))
            Mat = tr.shear(dimension,Mat,param,k)
            pt.Print(np.transpose(Mat))
        elif S[0] == 'stretch':
            param = S[1]
            k = (float(S[2]))
            Mat = tr.stretch(dimension,Mat,param,k)
        elif S[0] == 'custom':
            if (dimension == 2):
                a = (float(S[1]))
                b = (float(S[2]))
                c = (float(S[3]))
                d = (float(S[4]))
                Mat = tr.custom2D(dimension,Mat,a,b,c,d)
                pt.Print(np.transpose(Mat))
            elif (dimension == 3):
                a = (float(S[1]))
                b = (float(S[2]))
                c = (float(S[3]))
                d = (float(S[4]))
                e = (float(S[5]))
                f = (float(S[6]))
                g = (float(S[7]))
                h = (float(S[8]))
                i = (float(S[9]))
                Mat = tr.custom3D(dimension,Mat,a,b,c,d,e,f,g,h,i)
                pt.Print(np.transpose(Mat))
        elif S[0] == 'multiple':
            n = (int(S[1]))
            S = ["" for x in range(n)]
            for i in range(n):
                choice = input('... ')
                S[i] = choice.split()
            for i in range(n):
                if S[i][0] == 'translate':
                    if (dimension == 2):
                        dx = (float(S[1]))
                        dy = (float(S[2]))
                        MatTemp = tr.translate2D(dimension,Mat,dx,dy)
                        dxinit = 0.01*dx
                        dyinit = 0.01*dy
                        while (not(np.all(Mat == MatTemp))):
                            Mat = tr.translate2D(dimension,Mat,dxinit,dyinit)
                            pt.Print(np.transpose(Mat))
                    elif (dimension == 3):
                        dx = (float(S[1]))
                        dy = (float(S[2]))
                        dz = (float(S[3]))
                        Mat = tr.translate3D(dimension,Mat,dx,dy,dz)
                        pt.Print(np.transpose(Mat))
                elif S[i][0] == 'dilate':
                    k = (float(S[1]))
                    Mat = tr.dilate(dimension,Mat,k)
                    pt.Print(np.transpose(Mat))
                elif S[i][0] == 'rotate':
                    if (dimension == 2):
                        sudut = (float(S[1]))
                        a = (float(S[2]))
                        b = (float(S[3]))
                        Mat = tr.rotate2D(dimension,Mat,sudut/180*pi,a,b)
                        pt.Print(np.transpose(Mat))
                    elif (dimension == 3):
                        sudut = (float(S[1]))
                        a = (float(S[2]))
                        b = (float(S[3]))
                        c = (float(S[4]))
                        Mat = tr.rotate3D(dimension,Mat,sudut/180*pi,a,b,c)
                        pt.Print(np.transpose(Mat))
                elif S[0] == 'reflect':
                    param = S[1]
                    Mat = tr.reflect(dimension,Mat,param)
                    pt.Print(np.transpose(Mat))
                elif S[0] == 'shear':
                    param = S[1]
                    k = (float(S[2]))
                    Mat = tr.shear(dimension,Mat,param,k)
                    pt.Print(np.transpose(Mat))
                elif S[0] == 'stretch':
                    param = S[1]
                    k = (float(S[2]))
                    Mat = tr.stretch(dimension,Mat,param,k)
                    pt.Print(np.transpose(Mat))
                elif S[0] == 'custom':
                    if (dimension == 2):
                        a = (float(S[1]))
                        b = (float(S[2]))
                        c = (float(S[3]))
                        d = (float(S[4]))
                        Mat = tr.custom2D(dimension,Mat,a,b,c,d)
                        pt.Print(np.transpose(Mat))
                    elif (dimension == 3):
                        a = (float(S[1]))
                        b = (float(S[2]))
                        c = (float(S[3]))
                        d = (float(S[4]))
                        e = (float(S[5]))
                        f = (float(S[6]))
                        g = (float(S[7]))
                        h = (float(S[8]))
                        i = (float(S[9]))
                        Mat = tr.custom3D(dimension,Mat,a,b,c,d,e,f,g,h,i)
                        pt.Print(np.transpose(Mat))
        elif S[0] == 'reset':
            Mat = Matinit
            pt.Print(np.transpose(Mat))
        elif S[0] == 'exit':
            print('\nArigatou Gozaimasu ^_^')
        else:
            print('Pilihan tersebut tidak ada, mohon input ulang')
