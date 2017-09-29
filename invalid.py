print 'Enter any number between 0 to 9 \n'
n=int(input())
if (n==0) or(n==9):
	print 'You entered number is:',n
if (n<0) and (n>9):
	print 'You entered number is:',n
else:
	print 'Invalid input'
