s1=[]
s2=[]
n1=int(input('How many elements in a1?\n'))
print 'Enter the a1 array elements:\n'
for x in range(0,n1):
	num=int(input())
	s1.append(num)
n2=int(input('How many elements in a2?\n'))
print 'Enter the a2 array elements:\n'
for x in range(0,n2):
	num=int(input())
	s2.append(num)
	c=0
for x in s1:
	if x in s2:
		continue
	else:
		c=1
		break
if c==1:
	print 'al is Not subset of a2'
else:
	print 'a1 is Subset of a2'
