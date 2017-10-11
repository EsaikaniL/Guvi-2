def fun(a,b):
	count=0
	for x in range(a,b+1):
		l=0
		d=0
		s1=[]
		c=x
		while (c!=0):
			t=c%2
			s1.append(t)
			c=c/2
		for y in s1:
			if y==1:
				d=d+1
		for z in range(2,d-1):
			if d%z==0:
				l=1
		if (l==0)and (d!=1):
			count=count+1
	return count
i=int(input('Enter the 1st value:\n'))
j=int(input('Enter the 2 nd value:\n'))
a=fun(i,j)
print 'Ans is:',a
