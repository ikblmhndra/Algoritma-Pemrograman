print("Masukan nilai IPK =", end='')
ipk = float(input())

if ipk >= 3.5 and ipk <= 4.0:
    print('Predikat Cumlaude')
elif ipk >= 3.0 and ipk < 3.5:
    print('Predikat Sangant Memuaskan')
elif ipk >= 2.75 and ipk < 3.0:
    print('Predikat Memuaskan')
elif ipk <2.75 and ipk >= 0:
    print('Tidak Lulus')
else:
    print('IPK Tidak Valid')