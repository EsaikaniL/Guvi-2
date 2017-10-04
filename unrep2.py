s=[]
t1=[]
t2=[]
t3=[]
num1=int(input('How many elements? \n'))
print 'Enter the elments:\n'
for x in range(0,num1):
	num=int(input())
	s.append(num)
for x in s:
	if x not in t1:
		t1.append(x)
	else:
		t2.append(x)
for x in t1:
	if x not in t2:
		t3.append(str(x))
print 'Ans:\n',','.join(t3)
