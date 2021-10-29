print('Tim Badminton Jakarta telah memasuki pertandingan semi final.\n')

hasil = input('Apa hasil pertandingan semi final? [menang/kalah]? ')
if hasil == "menang" or hasil == "Menang" or hasil == "MENANG":
    print('Tim Badminton Jakarta memasuki ronde final')
    hasil1 = input('Apa hasil pertandingan final? [menang/kalah]? ')
    if hasil1 == "menang" or hasil1 == "Menang" or hasil1 == "MENANG":
        print('Selamat Tim Badminton Jakarta Mendapatkan Medali Emas')
    else:
        print('Selamat Tim Badminton Jakarta Mendapatkan Medali Perak')
else:
    print('Tim Badminton Jakarta Kalah di Semi Final dan selanjutnya memperebutkan Medali Perunggu')
    hasil2 = input('Apa hasil pertandingan ? [menang/kalah]? ')
    if hasil2 == "menang" or hasil2 == "Menang" or hasil2 == "MENANG":
        print('Selamat Tim Badminton Jakarta Mendapatkan Medali Perunggu')
    else:
        print('Sayang sekali kepada Tim Badminton Jakarta harus pulang dengan tangan kosong')

