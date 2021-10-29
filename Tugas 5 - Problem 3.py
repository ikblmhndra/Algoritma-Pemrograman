print('Menghitung gaji bulanan apakah terkena pajak pertahunnya?\n')
print('masukan gaji bulanan anda = ', end='')
gaji = int(input())

tahunan = gaji * 12

print('Total gaji Pertahun anda = ', tahunan)
# if tahunan <= 54000000:
#    print('Gaji anda tidak terkena pajak.')
if tahunan >= 55000000 and tahunan < 60000000:
    pajak = 5/100*tahunan
    print('Gaji anda terkena pajak sebesar 5% pertahun')
    print('Total pajak anda pertahun adalah = ', int(pajak))
    print('Gaji bershin anda pertahun adalah = ', int(tahunan - pajak))
elif tahunan >= 60000000 and tahunan < 250000000:
    pajak = 15/100*tahunan
    print('Gaji anda terkena pajak sebesar 15% pertahun')
    print('Total pajak anda pertahun adalah = ', int(pajak))
    print('Gaji bershin anda pertahun adalah = ', int(tahunan - pajak))
elif tahunan >= 250000000:
    pajak = 25/100*tahunan
    print('Gaji anda terkena pajak sebesar 25% pertahun')
    print('Total pajak anda pertahun adalah = ', int(pajak))
    print('Gaji bershin anda pertahun adalah = ', int(tahunan - pajak))
else:
    print('Gaji anda tidak terkena pajak.')