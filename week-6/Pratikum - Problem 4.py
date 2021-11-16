print('Siswa memilih pilihan jurusan\n')

nama = input('Isikan nama kamu : ')

jurusan = ['1. Teknik Informatika', '2. Teknik Mesin', '3. Desain Grafis', '4. Kedokteran', '5. Hukum\n']

print('Berikut adalah daftar jurusan yang tersedia\n', *jurusan, sep= "\n")
pilihan = int(input('Silahkan pilih jurusan yang kamu inginkan : '))

if pilihan == 1:
    print('Hay', nama, 'kamu memilih jurusan Teknik Infromatika')
elif pilihan == 2:
    print('Hay', nama, 'kamu memilih jurusan Teknik Mesin')
elif pilihan == 3:
    print('Hay', nama, 'kamu memilih jurusan Desain Grafis')
elif pilihan == 4:
    print('Hay', nama, 'kamu memilih jurusan Kedokteran')
elif pilihan == 5:
    print('Hay', nama, 'kamu memilih jurusan Hukum')