from _typeshed import SupportsReadline


print('Uang sakut =', end='')
uangSaku = int(input())

kost = 500000
makan = 400000
kuliah =  300000
tabungan = 300000
sedekah = 100000

kewajiba = kost + makan + kuliah
sisa = uangSaku - kewajiba

if sisa > 0:
    if sisa > (tabungan+sedekah):
        print('Budi menabung dan bersedekah')
        sisa2 = sisa - (tabungan+sedekah)
        if sisa2 > 1050000:
            print