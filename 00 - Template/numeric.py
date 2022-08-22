'''
Ada 3 tipe numerik dalam python:
int 
float
complex
'''
 
kalimat = 'ini adalah'
kalimat2 = True
kalimat3 = 1
kalimat4 = 2.5
kalimat5 = 2j
 
print(type(kalimat))
print(type(kalimat2))
print(type(kalimat3))
print(type(kalimat4))
print(type(kalimat5))

# dari int ke float
konversi_float = float(kalimat3)

# dari float ke int
konversi_int = int(kalimat4)

# dari int ke complex
konversi_complex = complex(kalimat3)

print(konversi_float, konversi_int, konversi_complex)

# fungsi matematika dalam python
import math as mt

x = [1, 2, 3]
y = [4, 5, 6]

print(max(x))
print(min(y))

# tentunya masih banyak fungsi yang lain dalam modul ini, 
# kode diatas adalah beberapa contohnya