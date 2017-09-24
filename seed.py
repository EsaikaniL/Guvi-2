n=int(input('Enter the number'))
c=0
for x in range(1,125):
	rt=1
	ft=1
	a=x
	stack=[]
	while x>0:
		t=x%10
		stack.append(t)
		x=x/10
 
	for y in stack:
		rt=rt*y
	ft=rt*a
	if (ft==n):
		print 'Seed for',n,'is', a
		c=1
if c!=1:
	print 'There is no seed for',n
