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
    #fungsi bernilai true jika x adalah bilangan real
    i = 0
    try:
        i = float(x)
        bool = True
    except:
        bool = False
    return bool

def isInt(x):
    #fungsi bernilai true jika x adalah bilangan real
    i = 0
    try:
        i = Int(x)
        bool = True
    except:
        bool = False
    return bool

def isParamValid(x,n):
    #fungsi bernilai true jika ditemukan n character berupa spasi
    i = 0
    count = 0
    while(i<len(x)):
        if(x[i]==' '):
            count = count + 1
        i = i+1

    if(count==n):
        bool=True
    else:
        bool=False
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
            #perintah fungsi translasi benda
            if (dimension == 2): #translasi benda 2 dimensi
                if(isParamValid(choice,2)):
                    if(isFloat(S[1]) and isFloat(S[2])):
                        dx = (float(S[1]))
                        dy = (float(S[2]))
                        Mat = tr.translate2D(dimension,Mat,dx,dy)
                        pt.Print2D(np.transpose(Mat))
                    else:
                        print('Input salah. Format input : translate <dx> <dy>')
                else:
                    print('Input salah. Format input : translate <dx> <dy>')

            elif (dimension == 3): #translasi benda 3 dimensi
                if(isParamValid(choice,3)):
                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3])):
                        dx = (float(S[1]))
                        dy = (float(S[2]))
                        dz = (float(S[3]))
                        Mat = tr.translate3D(dimension,Mat,dx,dy,dz)
                        pt.Print3D(np.transpose(Mat))
                    else:
                        print('Input salah. Format input : translate <dx> <dy> <dz>')
                else:
                    print('Input salah. Format input : translate <dx> <dy> <dz>')

        elif S[0] == 'dilate':
            #perintah fungsi dilatasi benda
            if(isParamValid(choice,1)):
                if(isFloat(S[1])):
                    k = (float(S[1]))
                    Mat = tr.dilate(dimension,Mat,k)
                    if(dimension==2):
                        pt.Print2D(np.transpose(Mat))
                    elif(dimension==3):
                        pt.Print3D(np.transpose(Mat))
                else:
                    print('Input salah. Format input : dilate <k>')
            else:
                print('Input salah. Format input : dilate <k>')

        elif S[0] == 'rotate':
            #perintah fungsi rotasi benda
            if (dimension == 2): #rotasi benda 2 dimensi
                if(isParamValid(choice,3)):
                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3])):
                        sudut = (float(S[1]))
                        a = (float(S[2]))
                        b = (float(S[3]))
                        Mat = tr.rotate2D(dimension,Mat,sudut/180*pi,a,b)
                        pt.Print2D(np.transpose(Mat))
                    else:
                        print('Input salah. Format input : rotate <deg> <a> <b>')
                else:
                    print('Input salah. Format input : rotate <deg> <a> <b>')

            elif (dimension == 3): #rotasi benda 3 dimensi
                if(isParamValid(choice,4)):
                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3]) and isFloat(S[4])):
                        sudut = (float(S[1]))
                        a = (float(S[2]))
                        b = (float(S[3]))
                        c = (float(S[4]))
                        Mat = tr.rotate3D(dimension,Mat,sudut/180*pi,a,b,c)
                        pt.Print3D(np.transpose(Mat))
                    else:
                        print('Input salah. Format input : rotate <deg> <a> <b> <c>')
                else:
                    print('Input salah. Format input : rotate <deg> <a> <b> <c>')

        elif S[0] == 'reflect':
            #perintah fungsi refleksi benda
            if(isParamValid(choice,1)):
                param = S[1]
                Mat = tr.reflect(dimension,Mat,param)
                if(dimension==2):
                    pt.Print2D(np.transpose(Mat))
                elif(dimension==3):
                    pt.Print3D(np.transpose(Mat))
            else:
                print('Input salah. Format input : reflect <param>')

        elif S[0] == 'shear':
            #perintah fungsi shear benda
            if(isParamValid(choice,2)):
                if(isFloat(S[2])):
                    param = S[1]
                    k = (float(S[2]))
                    Mat = tr.shear(dimension,Mat,param,k)
                    if(dimension==2):
                        pt.Print2D(np.transpose(Mat))
                    elif(dimension==3):
                        pt.Print3D(np.transpose(Mat))
                else:
                    print('Input salah. Format input : shear <param> <k>')
            else:
                print('Input salah. Format input : shear <param> <k>')

        elif S[0] == 'stretch':
            #perintah fungsi stretch benda
            if(isParamValid(choice,2)):
                if(isFloat(S[2])):
                    param = S[1]
                    k = (float(S[2]))
                    Mat = tr.stretch(dimension,Mat,param,k)
                    if(dimension==2):
                        pt.Print2D(np.transpose(Mat))
                    elif(dimension==3):
                        pt.Print3D(np.transpose(Mat))
                else:
                    print('Input salah. Format input : stretch <param> <k>')
            else:
                print('Input salah. Format input : stretch <param> <k>')

        elif S[0] == 'custom':
            #perintah fungsi custom perkalian matriks dengan benda
            if (dimension == 2): #fungsi custom 2 dimensi
                if(isParamValid(choice,4)):
                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3]) and isFloat(S[4])):
                        a = (float(S[1]))
                        b = (float(S[2]))
                        c = (float(S[3]))
                        d = (float(S[4]))
                        Mat = tr.custom2D(dimension,Mat,a,b,c,d)
                        pt.Print2D(np.transpose(Mat))
                    else:
                        print('Input salah. Format input : custom <a> <b> <c> <d>')
                else:
                    print('Input salah. Format input : custom <a> <b> <c> <d>')

            elif (dimension == 3): #fungsi custom 3 dimensi
                if(isParamValid(choice,9)):
                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3]) and isFloat(S[4]) and isFloat(S[5]) and isFloat(S[6]) and isFloat(S[7]) and isFloat(S[8]) and isFloat(S[9])):
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
                        pt.Print3D(np.transpose(Mat))
                    else:
                        print('Input salah. Format input : custom <a> <b> <c> <d> <e> <f> <g> <h> <i>')
                else:
                    print('Input salah. Format input : custom <a> <b> <c> <d> <e> <f> <g> <h> <i>')

        elif S[0] == 'multiple':
            #perintah fungsi dengan banyak operasi terhadap benda
            if(isParamValid(choice,1)):
                if(isInt(S[1])):
                    n = (int(S[1]))
                    S = ["" for x in range(n)]
                    for i in range(n):
                        choice = input('... ')
                        S[i] = choice.split()
                    for i in range(n):
                        if S[0] == 'translate':
                            #perintah fungsi translasi benda
                            if (dimension == 2): #translasi benda 2 dimensi
                                if(isParamValid(choice,2)):
                                    if(isFloat(S[1]) and isFloat(S[2])):
                                        dx = (float(S[1]))
                                        dy = (float(S[2]))
                                        Mat = tr.translate2D(dimension,Mat,dx,dy)
                                        pt.Print2D(np.transpose(Mat))
                                    else:
                                        print('Input salah. Format input : translate <dx> <dy>')
                                else:
                                    print('Input salah. Format input : translate <dx> <dy>')

                            elif (dimension == 3): #translasi benda 3 dimensi
                                if(isParamValid(choice,3)):
                                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3])):
                                        dx = (float(S[1]))
                                        dy = (float(S[2]))
                                        dz = (float(S[3]))
                                        Mat = tr.translate3D(dimension,Mat,dx,dy,dz)
                                        pt.Print3D(np.transpose(Mat))
                                    else:
                                        print('Input salah. Format input : translate <dx> <dy> <dz>')
                                else:
                                    print('Input salah. Format input : translate <dx> <dy> <dz>')

                        elif S[0] == 'dilate':
                            #perintah fungsi dilatasi benda
                            if(isParamValid(choice,1)):
                                if(isFloatS[1]):
                                    k = (float(S[1]))
                                    Mat = tr.dilate(dimension,Mat,k)
                                    if(dimension==2):
                                        pt.Print2D(np.transpose(Mat))
                                    elif(dimension==3):
                                        pt.Print3D(np.transpose(Mat))
                                else:
                                    print('Input salah. Format input : dilate <k>')
                            else:
                                print('Input salah. Format input : dilate <k>')

                        elif S[0] == 'rotate':
                            #perintah fungsi rotasi benda
                            if (dimension == 2): #rotasi benda 2 dimensi
                                if(isParamValid(choice,3)):
                                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3])):
                                        sudut = (float(S[1]))
                                        a = (float(S[2]))
                                        b = (float(S[3]))
                                        Mat = tr.rotate2D(dimension,Mat,sudut/180*pi,a,b)
                                        pt.Print2D(np.transpose(Mat))
                                    else:
                                        print('Input salah. Format input : rotate <deg> <a> <b>')
                                else:
                                    print('Input salah. Format input : rotate <deg> <a> <b>')

                            elif (dimension == 3): #rotasi benda 3 dimensi
                                if(isParamValid(choice,4)):
                                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3]) and isFloat(S[4])):
                                        sudut = (float(S[1]))
                                        a = (float(S[2]))
                                        b = (float(S[3]))
                                        c = (float(S[4]))
                                        Mat = tr.rotate3D(dimension,Mat,sudut/180*pi,a,b,c)
                                        pt.Print3D(np.transpose(Mat))
                                    else:
                                        print('Input salah. Format input : rotate <deg> <a> <b> <c>')
                                else:
                                    print('Input salah. Format input : rotate <deg> <a> <b> <c>')

                        elif S[0] == 'reflect':
                            #perintah fungsi refleksi benda
                            if(isParamValid(choice,1)):
                                param = S[1]
                                Mat = tr.reflect(dimension,Mat,param)
                                if(dimension==2):
                                    pt.Print2D(np.transpose(Mat))
                                elif(dimension==3):
                                    pt.Print3D(np.transpose(Mat))
                            else:
                                print('Input salah. Format input : reflect <param>')

                        elif S[0] == 'shear':
                            #perintah fungsi shear benda
                            if(isParamValid(choice,2)):
                                if(isFloat(S[2])):
                                    param = S[1]
                                    k = (float(S[2]))
                                    Mat = tr.shear(dimension,Mat,param,k)
                                    if(dimension==2):
                                        pt.Print2D(np.transpose(Mat))
                                    elif(dimension==3):
                                        pt.Print3D(np.transpose(Mat))
                                else:
                                    print('Input salah. Format input : shear <param> <k>')
                            else:
                                print('Input salah. Format input : shear <param> <k>')

                        elif S[0] == 'stretch':
                            #perintah fungsi stretch benda
                            if(isParamValid(choice,2)):
                                if(isFloat(S[2])):
                                    param = S[1]
                                    k = (float(S[2]))
                                    Mat = tr.stretch(dimension,Mat,param,k)
                                    if(dimension==2):
                                        pt.Print2D(np.transpose(Mat))
                                    elif(dimension==3):
                                        pt.Print3D(np.transpose(Mat))
                                else:
                                    print('Input salah. Format input : stretch <param> <k>')
                            else:
                                print('Input salah. Format input : stretch <param> <k>')

                        elif S[0] == 'custom':
                            #perintah fungsi custom perkalian matriks dengan benda
                            if (dimension == 2): #fungsi custom 2 dimensi
                                if(isParamValid(choice,4)):
                                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3]) and isFloat(S[4])):
                                        a = (float(S[1]))
                                        b = (float(S[2]))
                                        c = (float(S[3]))
                                        d = (float(S[4]))
                                        Mat = tr.custom2D(dimension,Mat,a,b,c,d)
                                        pt.Print2D(np.transpose(Mat))
                                    else:
                                        print('Input salah. Format input : custom <a> <b> <c> <d>')
                                else:
                                    print('Input salah. Format input : custom <a> <b> <c> <d>')

                            elif (dimension == 3): #fungsi custom 3 dimensi
                                if(isParamValid(choice,9)):
                                    if(isFloat(S[1]) and isFloat(S[2]) and isFloat(S[3]) and isFloat(S[4]) and isFloat(S[5]) and isFloat(S[6]) and isFloat(S[7]) and isFloat(S[8]) and isFloat(S[9])):
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
                                        pt.Print3D(np.transpose(Mat))
                                    else:
                                        print('Input salah. Format input : custom <a> <b> <c> <d> <e> <f> <g> <h> <i>')
                                else:
                                    print('Input salah. Format input : custom <a> <b> <c> <d> <e> <f> <g> <h> <i>')
                else:
                    print('Input salah. Format input : multiple <n>')
            else:
                print('Input salah. Format input : multiple <n>')
                
        elif S[0] == 'reset':
            #perintah fungsi reset untuk mengembalikan benda ke posisi dan bentuk awal
            if(isParamValid(choice,0)):
                Mat = Matinit
                if(dimension==2):
                    pt.Print2D(np.transpose(Mat))
                elif(dimension==3):
                    pt.Print3D(np.transpose(Mat))
            else:
                print('Input salah. Format input : reset')

        elif S[0] == 'exit':
            #perintah fungsi untuk keluar dari program
            if(isParamValid(choice,0)):
                print('\nArigatou Gozaimasu ^_^')
            else:
                print('Input salah. Format input : exit')

        else:
            #input perintah yang dimasukkan tidak valid
            print('Pilihan tersebut tidak ada, mohon input ulang')
        print('')
