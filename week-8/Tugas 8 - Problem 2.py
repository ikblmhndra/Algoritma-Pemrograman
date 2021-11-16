uangBudi = 50000
airMineral = 1500
jumlahHari = 0

while (uangBudi > 0):
    print('Uang Budi Sisa:', uangBudi)
    uangBudi = uangBudi - airMineral
    jumlahHari += 1
print(f'budi bisa beli air mineral : {jumlahHari}x' )