str=raw_input('Enter your line: \n')
c=0
sym=",./<>?!@~`#$%^&*()_+-={}[]:;"
for x in str:
	if x in sym:
		c=c+1
print 'The total character in the string is:',c
