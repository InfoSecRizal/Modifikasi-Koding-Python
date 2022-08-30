'''
Apa itu parameter? Parameter adalah input yang anda tetapkan untuk fungsi anda.
Apa itu argumen? Argumen adalah nilai aktual/asli/sesungguhnya untuk parameter yang diberikan
Perbedaan antara print function dengan car? Print function mengambil input sedangkan car tidak

'''

# fungsi 
def car(first_name, last_name):
  print(f'Mobil Ferrari {first_name} {last_name}')
  print('Ditunggangi oleh CL16 dan CS55')

car('F1', '75')

'''
Dalam Programming, kita mempunyai 2 jenis fungsi, yaitu:
1. Mengerjakan sebuah tugas, contoh: seperti di atas
2. Mengembalikan sebuah nilai, contoh: operasi aritmatika
'''

# keyword argument
# ketika kita menambahkan double bintang ke dalam maka kita bisa menambahkan beberapa key:value 
# dan python secara otomatis mengemasnya menjadi dictionary
def save_user(**user): 
  print(user)

save_user(id=1, name='John', age=22)

print(10*'=')
print('KALKULATOR')
print(10*'=')

def tambah(x, y):
  return x + y 
def kurang(x, y):
  return x - y
def kali(x, y):
  return x * y
def bagi(x, y):
  return x / y

print('Pilih operator!: ')
print('1.tambah')
print('2.kurang')
print('3.kali')
print('4.bagi')

while True:
  pilihan = input('Masukan pilihan (1/2/3/4)!: ')
  num1 = float(input('Masukan angka pertama: '))
  num2 = float(input('Masukan angka kedua: '))

  if pilihan == '1':
    print(num1, '+', num2, '=', tambah(num1, num2))
  elif pilihan == '2':
    print(num1, '-', num2, '=', kurang(num1, num2))
  elif pilihan == '3':
    print(num1, '*', num2, '=', kali(num1, num2))
  elif pilihan == '4':
    print(num1, '/', num2, '=', bagi(num1, num2))
  else:
    print('Input tidak valid!')

  pilihan_selanjutnya = input('Ingin berhitung lagi? ya/tidak: ')
  if pilihan_selanjutnya == 'tidak':
    break  