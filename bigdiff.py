n=int(input('how many elements?'))
s=[]
t=[]
for x in range(0,n):
	num=int(input('Enter numbers:\n'))
	s.append(num)
for x in range(0,n-1):
	y=s[x]-s[x+1]
	if (y<0):
		t.append(-y)
	else:
		t.append(y)
t.sort()
print t[n-2]
