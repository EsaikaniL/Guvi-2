n=int(input('How many elements?\n'))
print 'Enter the numbers\n'
s=[]
a=[]
for x in range(0,n):
	num=int(input())
	s.append(num)
for x in s:
	if str(x) not in a:
		e=str(x)
		a.append(e)
print ''.join(a)
