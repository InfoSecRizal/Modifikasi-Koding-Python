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