num=int(input('Emter the test cases:\n'))
s=[]
for x in range(0,num):
	m=int(input('Enter the m value \n'))
	n=int(input('Enter the n value \n'))
	for y in range(m,n+1):
		c=0
		for z in range(2,y-1):
			if (y%z==0):
				c=1
		if (c==0) and (y!=1):
			print y
	print "\n"
