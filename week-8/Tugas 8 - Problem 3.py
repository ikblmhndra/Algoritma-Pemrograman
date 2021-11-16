start = 1980
end = 2021

# print list of years
for x in range(start,end+1):
    print(x, end=" " )
print('\n')

# print of leap years
for z in range(start, end+1):
    if(z % 4 == 0):
        print(z, 'adalah tahun Kabisat')