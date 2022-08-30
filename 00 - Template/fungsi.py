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
