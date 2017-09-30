str=raw_input('Enter the line \n')
c=1
st=list(str)
n=len(st)
for x in range(0,n-1):
	if (st[x]==' ') and (st[x+1]!=' '):
		c=c+1
print c
