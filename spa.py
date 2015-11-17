import random
import pprint

def random_spare(r, c, num_nonzero, up, low):
	matrix = [[0 for x in range(c)] for x in range(r)]
	for x in range(num_nonzero):
		sel_r = random.randint(0,r-1)
		sel_c = random.randint(0,c-1)
		while matrix[sel_r][sel_c]!=0:
			sel_r = random.randint(0,r-1)
			sel_c = random.randint(0,c-1)
		matrix[sel_r][sel_c] = random.randint(low,up)
	return matrix

def Transpose(a):
	tr = [[0 for x in range(len(a))] for x in range(len(a[0]))]
	for i in range(len(a[0])):
		for j in range(len(a)):
			tr[i][j] = a[j][i]
	return tr

def Muitiply(a, b):
	mu = [[0 for x in range(len(b))] for x in range(len(a))]
	for i in range(len(a)):
		for j in range(len(b)):
			for k in range(len(b)):
				mu[i][j] += a[i][k]*b[k][j]
	return mu

row = 6 #input(">>> Please input the number of row: ")
col = 3 #input(">>> Please input the number of column: ")

a = random_spare(row, col, random.randint(7,17), 10, 1)
b = random_spare(col, row, random.randint(7,17), 10, 1)
c = Transpose(a)
d = Muitiply(a, b)

print "A: "
pprint.pprint(a)
print "B: "
pprint.pprint(b)
print "C: "
pprint.pprint(c)
print "D: "
pprint.pprint(d)