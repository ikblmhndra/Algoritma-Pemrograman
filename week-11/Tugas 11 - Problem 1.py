namaBarang = []
hargaBarang = []

def menu():
    print('-'*30)
    print('1. Tampilkan daftar harga barang')
    print('2. Tambahkan data barang')
    print('3. Hapus data barang')
    print('4. Ubah harga barang')
    print('5. Keleuar')
    print('-'*30)
    menu = input('Masukan angka: ')
    print('-'*30)

    if menu == '1':
        show_list()
    elif menu == '2':
        add_list()
    elif menu == '3':
        remove_list()
    elif menu == '4':
        edit_list()
    elif menu == '5':
        exit()
    else:
        print('Input tidak valid!')

def show_list():
    daftarharga = {}
    i = 0
    while i < len(namaBarang):
        daftarharga[namaBarang[i]] = hargaBarang[i]
        i+=1
    print('NAMA BARANG \t HARGA')
    for key, value in daftarharga.items():
        print(key, '\t\t', value)

def add_list():
    tambah = input('Masukan nama barang : ')
    if tambah in namaBarang:
        print('Daftar Barang sudah ada')
    else:
        namaBarang.append(tambah)
        harga = input('Masukan harga barang : ')
        hargaBarang.append(harga)
        print('Data berhasil di tambah')

def remove_list():
    hapus = input('Masukan nama barang : ')
    if hapus not in namaBarang:
        print(hapus, 'Barang Tersebut tidak ada')
    else:
        namaBarang.remove(hapus)
        hapusHarga = input('Harga barang yang ingin di hapus : ')
        hargaBarang.remove(hapusHarga)
        print('Barang Berhasil di hapus')

def edit_list():
    # dictBarang = dict(zip(namaBarang,hargaBarang))
    cekNama = input('Masukan nama barang yang ingin diubah : ')
    if cekNama not in namaBarang:
        print(cekNama, 'Barang tidak tersedia !')
    else:
        hargaAwal = input('Masukan harga awal :')
        if hargaAwal not in hargaBarang:
            print(hargaBarang, 'Tidak sesuai')
        else:
            newPrice = input('Masukan harga terbaru : ')
            hargaBarang.remove(hargaAwal)
            hargaBarang.append(newPrice)

        
if __name__ == '__main__':
    while True:
        menu()