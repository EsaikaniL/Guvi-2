n=int(input('Enter the number'))
c=0
for x in range(1,n/2):
	rt=1
	sd=1
	a=x
	stack=[]
	while x>0:
		t=x%10
		stack.append(t)
		x=x/10
 
	for y in stack:
		rt=rt*y
	sd=rt*a
	if (sd==n):
		print 'Seed for',n,'is', a
		c=1
if c!=1:
	print 'There is no seed for',n
