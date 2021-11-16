print('Menentukan segitiga berdasarkan panjang ketiga sisinya.\n')

sisiA=eval(input('Masukan nila sisi A :'))
sisiB=eval(input('Masukan nila sisi B :'))
sisiC=eval(input('Masukan nila sisi C :'))

if sisiA == sisiB == sisiC:
    print('Merupakan Segitiga Sama Sisi')
elif sisiA == sisiB or sisiA == sisiC or sisiB == sisiA or sisiB == sisiC or sisiC == sisiA or sisiC == sisiB:
    print('Merupakan Segitiga sama Kaki')
elif sisiA*sisiA + sisiB*sisiB == sisiC*sisiC or sisiA*sisiA + sisiC*sisiC == sisiB*sisiB or sisiC*sisiC + sisiB*sisiB == sisiA*sisiA:
    print('Merupakan Segitiga siku siku')
else:
    print('Merupakan Segitiga Sembarang')
