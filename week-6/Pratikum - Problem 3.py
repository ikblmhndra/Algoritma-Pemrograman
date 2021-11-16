print('Menentukan mana bilangan terbesar\n')

a, b, c = (
    int(input('Masukan nila a :')),
    int(input('Masukan nila b :')),
    int(input('Masukan nila c :')),

)

if a > b and a > c:
    print('A yang terbesar')
elif b > a and b > c:
    print('B yang terbesar')
else:
    print('C yang terbesar')

    