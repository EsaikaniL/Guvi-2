s=[]
t=[]
n=int(input('How many elements?\n'))
print 'Enter the elements \n'
for x in range(0,n):
	num=int(input())
	s.append(num)
for x in s:
	if x not in t:
		t.append(x)
	else:
		print x
		break
