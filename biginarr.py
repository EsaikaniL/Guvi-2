s=[]
r=int(input('How many elements?'))
for x in range(0,r):
	n=int(input('Enter number:\n'))
	s.append(n)
s.sort()
print '\n\n Biggest number is:',s[r-1]
print '\n lowest number is:',s[0]
