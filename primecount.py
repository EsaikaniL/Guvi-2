m=int(input('Enter the m value \n'))
n=int(input('Enter the n value \n'))
d=0
for y in range(m,n+1):
	c=0
	for z in range(2,y-1):
		if (y%z==0):
			c=1
	if (c==0) and (y!=1):
		d=d+1
print d
