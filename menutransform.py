import numpy as np
import os
import transform as tr
# Transform

def menu(dimension,Mat):
    "Menu Transformasi"
    os.system('cls')
    Matinit = Mat
    while not(choice == 'exit'):
        print('Pilih transformasi yang diinginkan')
        choice = input('>> ')
        S = choice.split()
        if S[0] == 'translate':
            dx = S[1]
            dy = S[2]
            tr.translate(dimension,Mat,dx,dy)
        elif S[0] == 'dilate':
            
        elif S[0] == 'rotate':

        elif S[0] == 'reset':
            Mat = Matinit
        elif S[0] == 'exit':
            print('Arigatou Gozaimasu ^_^')
        else:
            print('Pilihan tersebut tidak ada, mohon input ulang')
