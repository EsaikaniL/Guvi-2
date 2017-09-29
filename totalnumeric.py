str=raw_input('Enter your line: \n')
c=0
for x in str:
	if (x.isalpha()) or (x.isdigit()):
		c=c+1
print 'The total numeric character in the string is:',c
