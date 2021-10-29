start = 1
end = 50

# print list number from 1 to 50
for x in range(start,end+1):
    print(x, end=" " )
print('\n')

# print list prime number 
for i in range(start, end+1):
	if i > 1:
		for j in range(2, i):
			if(i % j == 0):
				break
		else:
			print(i, 'Ini bilangan Prima')
print('\n')

#print list of numbers divisible by 5
for z in range(start, end+1):
    if(z % 5 == 0):
        print(z, 'dapat di bagi 5')