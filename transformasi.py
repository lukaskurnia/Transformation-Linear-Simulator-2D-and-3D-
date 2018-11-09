

# fungsi dan posedure untuk operasi matriks
def translate(dimension):
# Melakukan translasi objek dengan menggeser nilai x sebesar dx
# dan menggeser nilai y sebesar dy
    "ini prosedur rotation"
    trans = input('>> ')
    temp = trans.split()
    deltaX = (int(temp[0]))
    deltaY = (int(temp[1]))
    return Mat

def dilate(dimension):
# Melakukan dilatasi objek dengan faktor scaling k
    "ini prosedure dilate"
    k = (int(input('>> ')))
    return Mat

def rotate(dimension):
# Melakukan rotasi objek secara berlawanan arah arum jam sebesar
# sudut terhadap titik a dan b
    "ini prosedur rotation"
    rot = input('>> ')
    temp = rot.split()
    sudut = (int(temp[0]))
    titikX = (int(temp[1]))
    titikY = (int(temp[2]))
    return Mat

def reflect(dimension):
# Melakukan pencerminan objek. Nilai paraeter adalah suatu nilai-nilai :
# x,y,y=x,y=-x,atau(a,b). Nilai (a,b) adalah titik untuk melakukan pencerminan
    "ini prosedure reflect"
    ref = input('>> ')
    return Mat

def shear(dimension):
# Melakukan operasi shear pada objek. NIlai parameter dapat berupa
# x (terhadap sumbu x) atau y (terhadap sumbu y). Nilai k adalah faktor shear.
    "ini prosedur shear"
    k = (int(input('>> ')))
    return Mat

def stretch(dimension):
# Melakukan operasi scretch pada objek. Nilai param dapat berupa x
# (terhadap sumbu x) atau y (terhadap sumbu y). Nilai k adalah faktor shear
    "ini prosedur sretch"
    k = (int(input('>> ')))
    return Mat

def custom(dimension):
# Melakukan transformasi linier pada onjek dengan matriks transformasi
# sebagai berikut : [a b]
#                   [c d]
    "ini prosedur custom"
    cust = (input(' '))
    temp = cust.split()
    if dimension == 2: #yang diinput ada 4 parameter
        Mat2[0][0] = (int(cust[0]))
        Mat2[0][1] = (int(cust[1]))
        Mat2[1][0] = (int(cust[2]))
        Mat2[1][1] = (int(cust[3]))
    elif dimension ==3: #yang diinput ada 9 parameter
        Mat2[0][0] = (int(cust[0]))
        Mat2[0][1] = (int(cust[1]))
        Mat2[0][2] = (int(cust[2]))
        Mat2[1][0] = (int(cust[3]))
        Mat2[1][1] = (int(cust[4]))
        Mat2[1][2] = (int(cust[5]))
        Mat2[2][0] = (int(cust[6]))
        Mat2[2][1] = (int(cust[7]))
        Mat2[2][2] = (int(cust[8]))
    Mat = np.dot(Mat,Mat2)
    return Mat

# def multiple(dimension):
# Melakukan transformasi linier pada objek sebanyak n kali berurutan
# Setiap baris input 1..n dapat berupa translate, rotate, shear, dll
# tetapi bukan multiple, reset, exit
    # "ini prosedur multiple"
