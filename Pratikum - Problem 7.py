print('Menonton bioskop. Menentukan apakah seseorang boleh menonton film berdasarkan umurnya.\n')

umur = int(input('Berapa tahun kamu ?'))

if umur >= 14:
    print('Kamu di perbolehkan menonton film tersebut')
elif umur < 14:
    print('Umur Kamu harus di dampingin orang tua.')
    orangTua = input('Apakah kamu di dampingin orang tua? [ya/tidak]: ')
    if orangTua == "ya" or orangTua == "YA" or orangTua == "Ya":
        print('kamu diperbolehkan menonton')
    else:
        print('kamu tidak diperbolehkan menonton sendiri ')
