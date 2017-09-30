str=raw_input('Enter numbers in string;\n')
st=list(str)
re=0
for x in st:
	s=int(x)
	re=re*10+s
print re
