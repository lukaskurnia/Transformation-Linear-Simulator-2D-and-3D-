import numpy as np
import os
import print as pt
import transformasi as tr
# Transform
# N.B : Fungsi yang memiliki parameter berbeda untuk ruang 2D dan 3D
# translate
# rotate
# custom

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
            dx = (int(S[1]))
            dy = (int(S[2]))
            MatTemp = tr.translate2D(dimension,Mat,dx,dy)
            dxinit = 0.01*dx
            dyinit = 0.01*dy
            while (not(np.all(Mat == MatTemp))):
                Mat = tr.translate2D(dimension,Mat,dxinit,dyinit)
                pt.Print(np.transpose(Mat))
        elif S[0] == 'dilate':
            k = (float(S[1]))
            MatInit = Mat
            if (k < 1):
                kinit = 1 - 0.01
                while (kinit >= k):
                    Mat = tr.dilate(dimension,MatInit,kinit)
                    kinit = kinit - 0.01
                    pt.Print(np.transpose(Mat))
            if (k >= 1):
                kinit = 1 + 0.1
                while (kinit <= k):
                    Mat = tr.dilate(dimension,MatInit,kinit)
                    kinit = kinit + 0.1
                    pt.Print(np.transpose(Mat))
        elif S[0] == 'rotate':
            sudut = (float(S[1]))
            a = (int(S[2]))
            b = (int(S[3]))
            Mat = tr.rotate(dimension,Mat,sudut,a,b)
        elif S[0] == 'reflect':
            param = S[1]
            print(S)
        elif S[0] == 'shear':
            param = S[1]
            k = (int(S[2]))
            print(S)
        elif S[0] == 'stretch':
            param = S[1]
            k = (int(S[2]))
            print(S)
        elif S[0] == 'custom':
            print(S)
        elif S[0] == 'multiple':
            n = (int(S[1]))
            S = ["" for x in range(n)]
            for i in range(n):
                choice = input('... ')
                S[i] = choice.split()
            for i in range(n):
                if S[i][0] == 'translate':
                    dx = (int(S[i][1]))
                    dy = (int(S[i][2]))
                    print(S[i])
                elif S[i][0] == 'dilate':
                    k = (int(S[i][1]))
                    print(S[i])
                elif S[i][0] == 'rotate':
                    sudut = (float(S[i][1]))
                    a = (int(S[i][2]))
                    b = (int(S[i][3]))
                    print(S[i])
                elif S[i][0] == 'reflect':
                    param = S[i][1]
                    print(S[i])
                elif S[i][0] == 'shear':
                    param = S[i][1]
                    k = (int(S[i][2]))
                    print(S[i])
                elif S[i][0] == 'stretch':
                    param = S[i][1]
                    k = (int(S[i][2]))
                    print(S[i])
                elif S[i][0] == 'custom':
                    print(S[i])
        elif S[0] == 'reset':
            Mat = Matinit
            pt.Print(np.transpose(Mat))
        elif S[0] == 'exit':
            print('\nArigatou Gozaimasu ^_^')
        else:
            print('Pilihan tersebut tidak ada, mohon input ulang')
