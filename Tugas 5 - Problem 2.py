print('Menghitung tahun kabisat\n')
print('Masukan tahun = ', end='')
tahun = int(input())

if (tahun % 400 == 0):
        print(tahun, 'Merupakan tahun Kabisat')
elif (tahun % 100 == 0):
    print(tahun, 'Bukan tahun Kabisat')
elif (tahun % 4 == 0):
    print(tahun, 'Merupakan tahun Kabisat')
else:
    print(tahun, 'Bukan tahun Kabisat')
