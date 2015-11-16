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
		matrix[sel_r][sel_c]=random.randint(low,up)
	return matrix

def Transpose(r, c, matrix):
	tr = [[0 for x in range(r)] for x in range(c)]
#	for i in range(r)
#		for j in range(c)
#			tr[j][i] = matrix[i][j]
	return tr

r = 6 #input(">>> Please input the number of row: ")
c = 6 #input(">>> Please input the number of column: ")

a = random_spare(r, c, random.randint(7,17), 10, 1)
b = random_spare(r, c, random.randint(7,17), 10, 1)
c = Transpose(r, c, a)

print "A: "
pprint.pprint(a)
print "B: "
pprint.pprint(b)
print "C: "
pprint.pprint(c)