print('Masukan nila:', end='')
a = int(input())

if a > 0:
    print(a, 'adalah bilangan positif')
elif a == 0:
    print('0')
else:
    print(a, 'adalah bilangan negatif')
    print(abs(a), 'ini adalaha bilangan absolut')