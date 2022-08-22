'''
Operator dikelompokan menjadi beberapa bagian:

Operator Aritmatika (Arithmetic Operators)
Operator Perbandingan (Comparison (Relational) Operators)
Operator Penugasan (Assignment Operators)
Operator Logika (Logical Operators)
Operator Identitas (Identity Operators)
Operator Keanggotaan (Membership Operators)
Operator Bitwise (Bitwise Operators)
'''

''' 
operator aritmatika (+, -, *, /, %, **, //)
% modulus
Mendapatkan sisa pembagian dari nilai operan.
9 % 2 = 1
9 % 3 = 0

** pangkat 
Memangkatkan operan berdasarkan nilai dari operan sebelah kanan.

9 ** 2 = 81
2 ** 3 = 8

// pembagian bulat
Sama seperti pembagian. Hanya saja hasil pembagian dibulatkan kebawah.
9 // 2 = 4
8 // 3 = 3
'''

'''
Operator Perbandingan
Operator perbandingan (comparision operators) adalah suatu operator yang digunakan untuk membandingkan suatu nilai atau kondisi dari masing - masing operan.

Keluaran operator perbandingan hanya ada 2 yaitu True dan False

    Operator	                  Penggunaan
Sama Dengan (==)	                x == y
Tidak Sama Dengan (!=)	            x != y
Lebih Besar Dari (>)	            x > y
Lebih Kecil Dari (<)	            x < y
Lebih Besar Atau Sama Dengan (>=)	x >= y
Lebih Kecil Atau Sama Dengan (<=)	x <= y

'''

'''
Operator Penugasan
Operator penugasan adalah sebuah operator yang digunakan untuk memodifikasi nilai dari operator yang sudah ada.

Operator	Penggunaan	Sama Seperti	Contoh
                                        Anggap x = 5
=	           x = y	    x = y	      x = 5
+=	           x += y	  x = x + y	      x += 3 -> 8
-=	           x -= y	  x = x - y	      x -= 3 -> 2
*=	           x *= y	  x = x * y	      x *= 3 -> 15
/=	           x /= y	  x = x / y	      x /= 2 -> 2.5
%=	           x %= y	  x = x % y	      x %= 2 -> 1
//=	           x //= y	  x = x // y	  x //= 2 -> 2
**=	           x **= y	  x = x ** y	  x = 2 -> 9
&=	           x &= y	  x = x & y	      x &= 3 -> 1
^=	           x ^= y	  x = x ^ y	      x ^= 3 -> 6
>>=	           x >>= y	  x = x >> y	  x »= 3 -> 0
<<=	           x <<= y	  x = x << y	  x «= 3 -> 40
'''

'''
Operator Logika
Operator Logika adalah operator yang digunakan untuk menghasilkan return(True atau False) dari suatu kondisi dengan menggabungkan statement yang berbeda.

Operator	     Penggunaan
Dan (and)	     (x == y) and (a == b)
Atau (or)	     (x == y) or (a == b)
Bukan (not)	     not (x == y)
'''

'''
Dan
Membandingkan dua statement, menghasilkan nilai True jika keduanya bernilai benar(True), dan jika salah satu statement salah maka hasilnya False. Walaupun statement lainnya bernilai True.
(10 == 10) and (20 == 20) -> True
(10 == 9) and (20 == 20) -> False

Atau
Membandingkan dua statement, menghasilkan nilai True jika salah satunya bernilai benar(True), dan jika kedua statement salah maka hasilnya False. Walaupun statement lainnya bernilai False.
(10 == 9) and (20 == 20) -> True
(8 == 10) and (9 == 20) -> False

Bukan
Menghasilkan hasil sebaliknya, jika nilai operan adalah benar(True), maka hasilnya akan False, dan jika nilai operan adalah salah (False), maka hasilnya True.
not (20 == 20) -> False
not (20 == 10) -> True
'''

'''
Operator Identitas
Operator Identitas adalah operator yang digunakan untuk membandingkan object. Jika object bernilai sama dan memiliki lokasi memori yang sama maka hasilnya True.

Hampir sama seperti perbandingan (== dan !=) tetapi lebih spesifik dan lebih agresif dalam melakukan perbandingan

Operator	  Penggunaan	     Contoh
is	            x is y	        {} is dict() -> False
                                10 is 10 -> True
is not	        x is not y	    [] is not list() -> True
                                "ad" is not "ad" -> False
'''

'''
Operator Keanggotaan
Operator Kenggotaan adalah operator yang digunakan untuk mengecek apakah nilai operan berada di dalam sequence (list, dictionary, tuple).

Operator	Penggunaan	        Contoh
in	          x in y	    5 in [1,2,3,4,5] -> True
not in	      x not in y	5 not in [2,3,4,6] -> True
'''

'''
Operator Bitwise
Operator Bitwise adalah operator yang digunakan untuk membandingkan data binari. Biasa digunakan untuk membuat rangkaian logika (AND, OR, XOR, NOT).

Operator	Alias	       Penggunaan
&	         AND	         x & y
             OR	
^	         XOR	         x ^ y
~	         NOR	         ~x
<<	     Binary Left Shift	 x << y
>>	     Binary Right Shift	 x >> y
'''

'''
AND
Jika masing - masing operan memiliki bit 1 pada setiap pembanding, maka nilainya 1.

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = a & b         # 12 = 0000 1100
print(c)

OR
Jika salah satu atau kedua operan memiliki bit 1 pada setiap pembanding, maka nilainya 1.

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = a | b         # 61 = 0011 1101
print(c)

XOR
Jika hanya salah satu operan memiliki bit 1 pada setiap pembanding, maka nilainya 1, jika pembanding memilki nilai sama maka 0.

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = a ^ b         # 49 = 0011 0001
print(c)

NOR
Membalik semua nilai pada bit.

a = 60            # 60 = 0011 1100
c = ~a;           # -61 = 1100 0011
print(c)

Binary Left Shift
Mengubah posisi biner ke kiri dengan menambahkan nilai zero.

a = 60            # 60 = 0011 1100
c = a << 2;       # 240 = 1111 0000
print(c)

Binary Right Shift
Mengubah posisi biner ke kanan dengan menambahkan nilai zero.

a = 60            # 60 = 0011 1100
c = a >> 2;       # 15 = 0000 1111
print(c)
'''