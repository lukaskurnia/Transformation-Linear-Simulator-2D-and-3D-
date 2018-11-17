import numpy as np
# Make

def isNValid2D(x):
    #fungsi boolean yang akan menghasilkan True, jika nilai input merupakan
    #bilangan bulat yang lebih besar dari 2
    i = 0
    try:
        i = int(x)
        if(i>2):
            bool = True
        else:
            bool = False
    except:
        bool = False
    return bool

def isTitikValid2D(x):
    #fungsi boolean yang akan menghasilkan True, jika titik yang dimasukkan valid (x,y)
    i = 0
    count = 0
    while(i<len(x)):
        if(x[i]==','):
            count = count + 1
        i = i+1

    if(count==1):
        a = 0
        b = 0
        try:
            temp = x.split(',')
            a = float(temp[0])
            b = float(temp[1])
            val = True
        except:
            val = False
    else:
        val = False

    return val

def isTitikValid3D(x):
    #fungsi boolean yang akan menghasilkan True, jika titik yang dimasukkan valid (x,y,z)
    i = 0
    count = 0
    while(i<len(x)):
        if(x[i]==','):
            count = count + 1
        i = i+1

    if(count==2):
        a = 0
        b = 0
        c = 0
        try:
            temp = x.split(',')
            a = float(temp[0])
            b = float(temp[1])
            c = float(temp[2])
            val = True
        except:
            val = False
    else:
        val = False

    return val

def SearchTitik2D(x,n,Mat):
    #fungsi boolean yang akan menghasilkan True, jika titik yang dimasukkan sudah ada sebelumnya
    i = 0
    bool = True
    Ss = x.split(',')
    while(i<n and bool==True):
        if((Mat[i][0] == (float(Ss[0]))) and (Mat[i][1] == (float(Ss[1])))):
            bool = False
        else:
            i = i+1
    return bool

def SearchTitik3D(x,n,Mat):
    #fungsi boolean yang akan menghasilkan False, jika titik yang dimasukkan sudah ada sebelumnya
    i = 0
    bool = True
    Ss = x.split(',')
    while(i<n and bool==True):
        if((Mat[i][0] == (float(Ss[0]))) and (Mat[i][1] == (float(Ss[1]))) and (Mat[i][2] == (float(Ss[2])))):
            bool = False
        else:
            i = i+1
    return bool

def CekAllAbsis(x,n,Mat):
    #fungsi boolean yang akan menghasilkan True, jika semua absis dari titiknya sama
    i = 0
    bool = True
    while(i<n and bool==True):
        if((Mat[i][0] != x)):
            bool = False
        else:
            i = i+1
    return bool

def CekAllOrdinat(y,n,Mat):
    #fungsi boolean yang akan menghasilkan True, jika semua ordinat dari titiknya sama
    i = 0
    bool = True
    while(i<n and bool==True):
        if((Mat[i][1] != y)):
            bool = False
        else:
            i = i+1
    return bool

def CekAllTitikZ(z,n,Mat):
    #fungsi boolean yang akan menghasilkan True, jika semua Z dari titiknya sama
    i = 0
    bool = True
    while(i<n and bool==True):
        if((Mat[i][2] != z)):
            bool = False
        else:
            i = i+1
    return bool

def twodimension():

    status = False
    while(status==False):
        "Menu 2 Dimensi"
        print('Input banyaknya titik sudut bidang anda : ')
        x = input('>> ')
        while (isNValid2D(x)==False):
            print('Input harus bilangan bulat lebih besar dari 2.')
            x = input('>> ')
        #input harus >= 3

        N = (int(x))
        Mat = np.zeros( (N,2) )
        print('\nInput titik sudut bidang : ')

        #input titik pertama
        i = 0
        print('Input titik ke ', i+1)
        S = input()
        while (isTitikValid2D(S)==False):
            print('Format input yang dimasukkan harus (x,y).')
            print('Input titik ke ', i+1)
            S = input()

        Ss = S.split(',')
        Mat[i][0] = (float(Ss[0]))
        Mat[i][1] = (float(Ss[1]))
        print('')

        Absis = Mat[i][0]
        Ordinat = Mat[i][1]

        #input titik ke 2 sampai ke N
        i = 1
        while (i<N):
            print('Input titik ke ', i+1)
            S = input()

            if(isTitikValid2D(S)==True):
                if(SearchTitik2D(S,i,Mat)==True):
                    Ss = S.split(',')
                    Mat[i][0] = (float(Ss[0]))
                    Mat[i][1] = (float(Ss[1]))
                    i = i+1
                else:
                    print('Titik sudah pernah diinput.')
            else:
                print('Format input yang dimasukkan harus (x,y).')
            print('')
        #semua titik sudah diinput dengan valid

        if(CekAllAbsis(Absis,N,Mat)==False and CekAllOrdinat(Ordinat,N,Mat)==False):
            status=True
        else:
            print('Titik yang diinput bukan bidang 2 dimensi.')
            print('Ulangi input!')
        print('')
    #loop hingga input
    return Mat.transpose()

def threedimension():

    status=False
    while(status==False):
        "Menu 3 Dimensi"
        Mat = np.zeros( (8,3) )
        print('Bidang 3 dimensi yg digunakan adalah kubus')
        print('Input titik sudut kubus : ')

        #input titik pertama
        i = 0
        print('Input titik ke ', i+1)
        S = input()
        while (isTitikValid3D(S)==False):
            print('Format input yang dimasukkan harus (x,y,z).')
            print('Input titik ke ', i+1)
            S = input()
        Ss = S.split(',')
        Mat[i][0] = (float(Ss[0]))
        Mat[i][1] = (float(Ss[1]))
        Mat[i][2] = (float(Ss[2]))
        print('')

        Absis = Mat[i][0]
        Ordinat = Mat[i][1]
        TitikZ = Mat[i][2]

        #input titik ke 2 sampai ke N
        i = 1
        while (i<8):
            print('Input titik ke ', i+1)
            S = input()

            if(isTitikValid3D(S)==True):
                if(SearchTitik3D(S,i,Mat)==True):
                    Ss = S.split(',')
                    Mat[i][0] = (float(Ss[0]))
                    Mat[i][1] = (float(Ss[1]))
                    Mat[i][2] = (float(Ss[2]))
                    i = i+1
                else:
                    print('Titik sudah pernah diinput.')
            else:
                print('Format input yang dimasukkan harus (x,y,z).')
            print('')
        #semua titik sudah diinput dengan valid

        if(CekAllAbsis(Absis,8,Mat)==False and CekAllOrdinat(Ordinat,8,Mat)==False and CekAllTitikZ(TitikZ,8,Mat)==False):
            status=True
        else:
            print('Titik yang diinput bukan bidang 3 dimensi.')
            print('Ulangi input!')
        print('')
    #loop hingga input
    return Mat.transpose()

def shape(dimension):
    "Ini prosedur membuat shape"
    if dimension == 2:
        return twodimension()
    elif dimension == 3:
        return threedimension()
