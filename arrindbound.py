n=int(input('how many elemnts?\n'))
print 'Enter the elements:\n'
s=[]
for x in range(0,n):
	num=int(input())
	s.append(num)
a=int(s[0])
c=0
for x in range(0,n,a):
	if (s.index(s[x])==s.index(s[n-1])):
		c=1
if c==0:
	print 'false'
else:
	print 'True'
