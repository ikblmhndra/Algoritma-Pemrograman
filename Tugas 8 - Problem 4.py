def pypart(n):
	for i in range(0, n):
		for j in range(0, i+1):
			print("+ ",end="")
		print("\r")

n = 12
pypart(n)

for x in range(0,7):
    print("+ +")