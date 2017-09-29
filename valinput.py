n1=int(input('Enter starting range:\n'))
n2=int(input('Enter ending range:\n'))
n=int(input('Enter your input\n'))
while ( not ((n<=n2) and (n>=n1))):
	print '[ERROR] print valid number'
	n=int(input('Enter your input\n'))
print 'Your input is:',n
