s=[]
st=[]
n=int(input('How many elements?\n'))
for x in range(0,n):
	n1=int(input('Enter the numbers:\n'))
	s.append(n1)
n2=len(s)
for x in range(0,n2):
	for y in range(x+1,n2):
		sum=s[x]+s[y]
		st.append(sum)
st.sort()
n3=len(st)
print 'Highest possible is:',min(st)
print 'Lowest possible is:',max(st)
