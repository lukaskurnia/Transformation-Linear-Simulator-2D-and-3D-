import os
# Menu

def exit():
    "Menu exit"
    print('Terima kasih telah menjalankan program ini')

def mainmenu():
    "Menu Utama"
    print('Selamat Datang di Transformasi Geometri!\n')
    choice = 0
    while choice < 1 or choice > 3:
        print('Pilih Dimensi yang anda inginkan')
        print('1.) 2 Dimensi')
        print('2.) 3 Dimensi')
        print('3.) exit\n')
        choice = (int(input('>> ')))
        print()
        if choice == 1:
            os.system('clear')
            return 2
        elif choice == 2:
            os.system('clear')
            return 3
        elif choice == 3:
            os.system('clear')
            exit()
        else:
            os.system('clear')
            print('Pilihan tersebut tidak ada, mohon input ulang')
