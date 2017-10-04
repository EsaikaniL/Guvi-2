s=[]
t1=[]
t2=[]
t3=[]
n=int(input('How many elements? \n'))
print 'Enter the elments:\n'
for x in range(0,n):
	num=int(input())
	s.append(num)
for x in s:
	if x not in t1:
		t1.append(x)
	else:
		t2.append(str(x))
for x in t2:
	if x not in t3:
		t3.append(x)
print ','.join(t3)
