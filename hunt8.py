s=[]
t=[]
n=int(input('How many elements?\n'))
print 'Enter the elements \n'
for x in range(0,n):
	num=int(input())
	s.append(num)
for x in range(0,len(s)-1):
	for y in range(x+1,len(s)):
		sum=s[x]+s[y]
		if sum in s:
			print 'i:',s[x],'\t j:',s[y],'\t k:',sum
