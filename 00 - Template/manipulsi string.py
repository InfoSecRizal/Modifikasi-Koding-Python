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
print("PS C: "Users\HP Pavilion 14\Modifikasi Koding\00 - Template"")

# solusi yang benar

# menggunakan petik satu
print('PS C: \"Users\HP Pavilion 14\Modifikasi Koding\\00 - Template\"')

# menggunakan petik dua
print("PS C: \"Users\HP Pavilion 14\Modifikasi Koding\\00 - Template\"")

# menggunakan double blackslash untuk mengescape satu backslash
expected_output = '\(<_> \) (/ -_-/)'
print('\\(<_> \) (/ -_-/)')

