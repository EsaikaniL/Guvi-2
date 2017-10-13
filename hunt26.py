s=[]
def fun(b):
	s.append(b)
str=raw_input('Enter any string\n')
st=list(str)
for x in range(len(st)-1,-1,-1):
	a=fun(st[x])
for x in s:
	print x,
