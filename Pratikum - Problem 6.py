print('Budi Meminta uang untuk membeli makanan\n')

nasiLiwet = 25000
esBuah = 15000
daftar=['Paket nasi liwet Rp.25.000','Es Buah Rp15.000\n']
print('Berikut yang inigin Budi beli\n', *daftar, sep= "\n")

uangBudi = int(input('Berapa uang yang ingin diberikan kepada budi = '))
if uangBudi >= nasiLiwet+esBuah:
    print('Budi bisa membeli paket nasi liwet dan esbuah')
elif uangBudi >= nasiLiwet:
    print('Budi hanya bisa membeli paket nasi liwet saja')
elif uangBudi > esBuah:
    print('Budi hanya bisa membeli es buah saja')
else:
    print('Budi tidak cukup uang untuk membeli keduanya')
