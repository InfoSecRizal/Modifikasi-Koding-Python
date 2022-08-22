# syntax string
string = 'ini adalah string'

# cara print
print(string)
print(string[0])
print(string[1:3])

# method dan operator format
teks = 'teks ini berjumlah %d kata dalam bentuk file %s' % (100, 'microsoft word')
print(teks)

# manipulasi string


# escape characters
'''
karakter backslash ( \ ) bisa kita gunakan untuk mengescape
karakter karakter yang bisa memutus string dan membuat sintaks 
menjadi error
'''

# jika seperti ini akan membuat sintaks menjadi error
# kiat akan mendapat error karena sintaks terputus
# print("PS C: "Users\HP Pavilion 14\Modifikasi Koding\00 - Template"")

# solusi yang benar

# menggunakan petik satu
print('PS C: \"Users\HP Pavilion 14\Modifikasi Koding\\00 - Template\"')

# menggunakan petik dua
print("PS C: \"Users\HP Pavilion 14\Modifikasi Koding\\00 - Template\"")

# menggunakan double blackslash untuk mengescape satu backslash
expected_output = '\(<_> \) (/ -_-/)'
print('\\(<_> \) (/ -_-/)')

print(10*'=')
print('KALKULATOR')
print(10*'=')

def tambah (x, y):
  return x + y 
def kurang (x, y):
  return x - y
def kali (x, y):
  return x * y
def bagi (x, y):
  return x / y

print('\nPilih operator: ')
print('1.tambah')
print('2.kurang')
print('3.kali')
print('4.bagi')

while True:
    pilihan = input('\nMasukan pilihan (1/2/3/4): ')
    angka1 = float(input('Masukan angka pertama: '))
    angka2 = float(input('Masukan angka kedua: '))

    if pilihan == '1':
        print(angka1, '+', angka2, '=', tambah(angka1, angka2))
    elif pilihan == '2':
        print(angka1, '-', angka2, '=', kurang(angka1, angka2))
    elif pilihan == '3':
        print(angka1, '*', angka2, '=', kali(angka1, angka2))
    elif pilihan == '4':
        print(angka1, '/', angka2, '=', bagi(angka1, angka2))
    else:
        print('Input tidak valid!')

    berhitung = input('Ingin berhitung lagi?: ya/tidak? ')
    if berhitung == 'tidak':
        break        