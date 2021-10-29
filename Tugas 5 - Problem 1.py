print('Membandingkan nilai. lebih besar, lebih kecil, sama dengan\n')
print('Masukan bilangan A = ', end='')
a = int(input())
print('Masukan bilangan B = ', end='')
b = int(input())

if a > b:
    print('A lebih besar dari B')
elif a == b:
    print('A sama dengan B')
else:
    print('A lebih kecil dari B')