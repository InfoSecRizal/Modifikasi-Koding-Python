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
#print("PS C: "Users\HP Pavilion 14\Modifikasi Koding\00 - Template"")

# solusi yang benar

# menggunakan petik satu
print('PS C: \"Users\HP Pavilion 14\Modifikasi Koding\\00 - Template\"')

# menggunakan petik dua
print("PS C: \"Users\HP Pavilion 14\Modifikasi Koding\\00 - Template\"")

# menggunakan double blackslash untuk mengescape satu backslash
expected_output = '\(<_> \) (/ -_-/)'
print('\\(<_> \) (/ -_-/)')

# Operasi in dan not in pada string
koran = 'hari ini telah terjadi bencana banjir di daerah jakarta'
print('jakarta' in koran)
print('cianjur' in koran)

print('banjir' not in koran)
print('tsunami' not in koran)

# memootong string
'''
Indexing string
Kita bisa mengambil karater pada index ke-i pada string
seperti ini:
'''

judul = 'MENINGKATKAN LITERASI DIGITAL'
print(judul[0])
print(judul[0:12])
print(judul[1])
print(judul[-7:-1])

# String + non string
# print('Sekarang tanggal: ' + 22)
'''
Tidak bisa menggabungkan int dengan str, solusinya dengan
menggunakan str() function
'''
print('Sekarang tanggal: ' + str(22))

# Perkalian string
print(10*'=')
print('KALKULATOR')
print(10*'=')

'''
Pengertian Format String Pada Python

String formatting pada python adalah satu proses memasukkan atau menyisipkan 
variabel atau nilai ke dalam template string yang telah ditentukan [1].
'''

# Memformat String dengan String Interpolation / F-Strings
motor = 'Ducati'
asal = 'Italia'
print(f'Motor {motor} ini ganteng sekali, oh jelas karena diproduksi di {asal}')

'''
Memecah String Menjadi List dan Sebaliknya

Fungsi selanjutnya adalah memecah string menjadi list.
Hal ini bisa kita lakukan menggunakan fungsi string.split() dan string.join().
'''

bahan_roti = 'air, gula, tepung, ragi'
print(bahan_roti.split())
print(bahan_roti.split(','))
print(bahan_roti.split(', '))
print('❤️'.join(['aku', 'suka', 'python']))
print('🦖'.join(bahan_roti.split(', ')))

# uppercase
print('hai kawan!'.upper())

# lowercase
print('HAI SAYANG!'.lower())

# titlecase
print('canggihnya teknologi di mobil f1'.title())

# reversecase
print('FERRARI BADUT'.swapcase())
print('Red Bull Sangar'.swapcase())

# find
majalah = 'banyak majalah yang beredar di pasaran seperti playboy dll'
print(majalah.find('playboy'))
print(majalah.find('minum'))

# replace 
ibu_kota = 'Jakarta'
print(ibu_kota.replace('Jakarta', 'Kalimantan Timur'))

# mengahpus karakter tertentu pada string
kota = 'Bandung'
print(kota.replace('a', ''))

# menghitung jumlah karakter yang muncul
kalimat = 'makin ke sana makin ke sini'
x = kalimat.count('makin')
print(f'Kata "makin" muncul sebanyak {x} kali') 