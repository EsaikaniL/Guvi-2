s=[]
sum=0
n=int(input('How many elements?\n'))
for x in range(0,n):
	n1=int(input('Enter the numbers:\n'))
	s.append(n1)
n2=len(s)
for x in range(1,n2,2):
	b=int(s[x])
	sum=sum+(b*b)
for x in range(0,n2,2):
	a=int(s[x])
	sum=sum+(a*a*a)
print sum
