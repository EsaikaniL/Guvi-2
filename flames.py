s1="Muthu"
s2="Muhu"
str1=list(s1)
str2=list(s2)
for x in s1:
	for y in s2:
		if (x==y):
			del str1[str1.index(x)]
			del str2[str2.index(y)]
			break
a=len(str1)+len(str2)
print a
 
