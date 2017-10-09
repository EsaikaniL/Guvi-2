n=int(input('How many elements?\n'))
print 'Enter the elements\n'
s=[]
t=[]
for x in range(0,n):
	m=int(input())
	s.append(m)
max=0
for x in range(0,n-1):
	for y in range(n,x,-1):
		sum=0
		for z in range(x,y):
			sum =sum+int(s[z])
		if sum>max:
			max=sum
			k=range(x,y)
for x in k:
	t.append(str(s[x]))
print 'The max sub array is:',','.join(t)
