str=raw_input('Enter the string:\n')
st=list(str)
n=len(st)
for x in range(0,n-1,2):
	t=st[x]
	st[x]=st[x+1]
	st[x+1]=t
print ''.join(st)
