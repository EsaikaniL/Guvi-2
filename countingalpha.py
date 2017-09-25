s=raw_input('Enter any string')
alp=0
integer=0
for x in s:
	if x.isdigit():
		integer=integer+1
	elif x.isalpha():
		alp=alp+1
print 'The no of  integer in string is:',integer
print 'The no of alpha in string is:',alp
print 'The alpha numerical in string is:',integer+alp
