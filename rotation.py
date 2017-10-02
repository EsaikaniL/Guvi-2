n=int(input('how many elemnts?\n'))
print 'Enter the elements:\n'
s=[]
for x in range(0,n):
	num=int(input())
	s.append(num)
k=int(input('Enter k value:\n'))
for x in range(0,k):
	t=s[n-1]
	for y in range(n-1,0,-1):
		s[y]=s[y-1]
	s[0]=t
print s
