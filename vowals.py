c=raw_input('Enter any string:\n')
newstr = c
c1=list(c)
vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
for x in c:
	if x in vowels:
		newstr = newstr.replace(x,"")
c1.reverse()
print 'Reverse string is:\n',''.join(c1)
print 'After removing vowels:\n',newstr
 
