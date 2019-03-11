/* Simulasi Transformasi Linier pada bidang 2D dan 3D dengan Menggunakan OpenGL API */

/* Requirements */
Executable file hanya dapat dijalankan pada sistem operasi Windows 10.
Software dan library yang perlu terinstall :
- Python 3
- Pygame
- PyOpenGL
- Numpy

/* Kompilasi & eksekusi */
#) Untuk kompilasi dan eksekusi program :
	-> dapat mengetik pada cmd : 'python main_algeo2.py'

#) Jika ingin langsung eksekusi program tanpa kompilasi :
	-> run program main_algeo2.exe pada folder bin

/* Format Input Pada Program */
#) Untuk Menu Utama, program hanya dapat menerima 1 input bilangan bulat yaitu :
   1. 2 Dimensi
   2. 3 Dimensi
   3. Exit

#) Untuk input bidang 2 dimensi,
   - program menerima banyak titik untuk membuat suatu bidang 2 dimensi
     (input akan valid jika banyak titiknya lebih besar dari 2)
   - lalu diikuti dengan penginputan titik dengan format (x,y)
     (input akan valid jika titik yang diinput belum pernah diinput sebelumnya dan dapat membentuk benda 2 dimensi)

#) Untuk input bidang 3 dimensi, program di set hanya membentu bangun ruang kubus.
   - program akan menerima input 1 bilangan bulat yaitu :
     1. Default (akan terbentuk kubus dengan titik diset secara default)
     2. Input Manual (program menginput 8 titik kubus hingga valid)

#) Untuk input perintah transformasi, program menerima input dengan format :
   A. 2 dimensi :
      - translate <dx> <dy>        (dx,dy adalah bilangan real untuk pergeseran titik)
      - dilate <k>                 (k adalah bilangan real untuk koefisien skala pengali titik)
      - rotate <deg> <x> <y>       (deg adalah bilangan real untuk besar sudut perputaran)
                                   (x dan y adalah bilangan real untuk titik acuan rotasi)
      - reflect <param>            (param dapat berupa : {x, y, y=x, y=-x, (a,b)} dengan (a,b) merupakan titik sebagai acuan pencerminan)
      - shear <param> <k>          (param dapat berupa : {x,y} dan k adalah bilangan real sebagai koefisien pengali pergeseran titik)
      - stretch <param> <k>        (param dapat berupa : {x,y} dan k adalah bilangan real sebagai koefisien pengali pergeseran titik)

   B. 3 dimensi :
      - translate <dx> <dy> <dz>   (dx,dy,dz adalah bilangan real untuk pergeseran titik)
      - dilate <k>                 (k adalah bilangan real untuk koefisien skala pengali titik)
      - rotate <deg> <param>       (deg adalah bilangan real untuk besar sudut perputaran)
                                   (param dapat berupa : {x,y,z} sebagai sumbu putaran)
      - reflect <param>            (param dapat berupa : {x, y, z, xy, yz, zx} sebagai acuan pencerminan)
      - shear <param> <k>          (param dapat berupa : {x,y,z} dan k adalah bilangan real sebagai koefisien pengali pergeseran titik)
      - stretch <param> <k>        (param dapat berupa : {x,y,z} dan k adalah bilangan real sebagai koefisien pengali pergeseran titik)

#) Untuk input perintah lain yang dapat digunakan adalah :
   - multiple <n>                  (n merupakan bilangan bulat yang menunjukan banyak perintah yang akan dijalankan bersamaan)
   - reset                         (mengembalikan bentuk benda kepada awalnya)
   - exit


/* Kelompok */
Nama Kelompok : Los Santos
Anggota kelompok :
- Lukas Kurnia Jonathan - 13517006
- Willy Santoso         - 13517066
- Ferdy Santoso         - 13517116
