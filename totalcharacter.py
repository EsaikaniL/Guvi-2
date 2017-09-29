str=raw_input('Enter your line: \n')
c=0
for x in str:
	if (x.isalpha()):
		c=c+1
print 'The total character in the string is:',c
