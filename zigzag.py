str=raw_input('Enter any string:\n')
r=int(input('\nEnter the row:\n'))
if r==1:
	print str
else:
	n=r-1
	st=['' for x in range(0,r)]
	for x in range(0,len(str)):
		if(x//n)%2==0:
			st[x%n]=st[x%n]+str[x]
		elif(x//n)%2==1:
			st[n-(x%n)]=st[n-(x%n)]+str[x]
	s=''
	for x in range(0,r):
		s=s+st[x]
print s
