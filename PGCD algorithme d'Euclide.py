print("PGCD de A et B")
A = int(input('A = '))
B = int(input('B = '))
R0 = B
R1 = A%B
print(str(A) + " = " + str(R0) + " * " + str(A//B) + " + " + str(R1))
while(R1 != 0):
	x = R1
	R1 = R0%R1
	print(str(R0) + " = " + str(x) + " * " + str(R0//x) + " + " + str(R1))
	R0 = x
print("Le PGCD de A et B est: " + str(R0))
