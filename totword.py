str=raw_input('Enter your line: \n')
c=0
d=1
sym=",./<>?;':[]{}+_=-)(*&^%$#@!~`)"
for x in str:
	if (x.isalpha()) or (x.isdigit()) or (x in sym):
		c=c+1
	else:
		d=d+1
print 'The total word in the string is:',d
