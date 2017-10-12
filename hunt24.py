n=int(input('How many elements?\n'))
print '\n Enter the elements\n'
s=[]
for x in range(0,n):
	num=int(input())
	s.append(num)
k=int(input('\n Enter the target'))
for x in range(0,len(s)-1):
	for y in range(x+1,len(s)):
		sum=s[x]+s[y]
		if sum==k:
			a=x
			b=y
			break
print 'The Elements are',s[a],s[b]
