print(" Nama Depan : ", end=" ")
namaDepan = input()
print(" Nama Belakang : ", end=" ")
namaBelakang = input()
print(" Asal : ", end=" ")
asal = input()
print(" Umur : ", end=" ")
umur = input()

txt = "BIODATA ANDA"
x = txt.center(100)

txt1 = "TERIMAKASIH"
z = txt1.center(100)

print(100*"=")
print(x)
print(100*"-")
print("\tNAMA\t:",namaDepan,namaBelakang)
print("\tASAL\t:",asal)
print("\tUMUR\t:",umur,"Tahun")
print(100*"-")
print(z)
print(100*"=")

input("Press Enter to continue...")