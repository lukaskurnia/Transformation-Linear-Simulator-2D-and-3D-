import numpy as np
import os
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
            print(S)
        elif S[0] == 'dilate':
            k = (int(S[1]))
            print(S)
        elif S[0] == 'rotate':
            sudut = (float(S[1]))
            a = (int(S[2]))
            b = (int(S[3]))
            print(S)
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
            print(Mat)
        elif S[0] == 'exit':
            print('\nArigatou Gozaimasu ^_^')
        else:
            print('Pilihan tersebut tidak ada, mohon input ulang')
