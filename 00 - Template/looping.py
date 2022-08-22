# for loop

# dengan string
kalimat = 'ini adalah kalimat'
for k in kalimat:
    if k == 'kalimat':
        break
    print(k)

for x in range(3):
    print('Halo dek!')

# dengan list
es_krim = ['coklat', 'vanilla', 'mint']
for e in es_krim:
    if e == 'mint':
        continue
    print(e)

# tiga ini dikombinasikan dengan keyword break continue dan fungsi range

# while loop
minuman = 3
minum = 1

while minuman > 0:
    print('Habiskan minumnya!')
    minuman -= minum

print('Berhenti minum!')

# dengan break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# dengan continue
z = 0
while z < 5:
    z += 1 
    if z == 3:
        continue
    print(z)

# nested loop/perulangan di dalam perulangan (perulangan bersarang)
dimensional = []
kolom1 = [0, 1, 2]
kolom2 = [0, 1, 2]

for x in kolom1:
    dimensional.append(x)
    dimensional[x] = []
    for y in kolom2:
        dimensional[x].append(y)
        dimensional[x][y] = str(x) + ',' + str(y)

print(dimensional)