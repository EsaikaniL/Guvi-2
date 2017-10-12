r=int(input('Enter the row\n'))
s=['' for x in range(0,r)]
st=''
for x in range(0,r):
	s[x]=raw_input()
for x in range(0,r):
	if x%2==0:
		st=st+s[x]
	else:
		st=st+(s[x][::-1])
print st
