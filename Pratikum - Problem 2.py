print('Mengetahui Huruf yang di input Vokal atau Konsonan\n')
print('Masukan huruf :', end='')

huruf = str(input().lower());
vokal = ['a','i','u','e','o']

if huruf in vokal:
    print('Adalah huruf vokal')
else:
    print('Adalah huruf konsonan')