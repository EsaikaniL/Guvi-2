a=[[0 for x in range(0,2)]for y in range(0,2)]
for x in range(0,2):
	for y in range(0,2):
		a[x][y]=int(input())
b=[[0 for x in range(0,2)]for y in range(0,2)]
c=[[0 for x in range(0,2)]for y in range(0,2)]
for x in range(0,2):
	for y in range(0,2):
		b[x][y]=int(input())
for x in range(0,2):
	for y in range(0,2):
		for k in range(0,2):
			c[x][y]=c[x][y]+a[x][k]*b[k][y]
for x in range(0,2):
	for y in range(0,2):
		print c[x][y],
	print '\t'
