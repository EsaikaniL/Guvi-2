n=int(input('How many elemenst?\n'))
print 'Enter the elements\n'
s=[]
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
for x in range(0,n):
	num=int(input())
	s.append(num)
for x in s:
	if x<0:
		s1.append(x)
	elif x>0:
		s2.append(x)
for x in s1:
	for y in s2:
		sum=x+y
		s3.append(sum)
for x in s3:
	if x<0:
		s4.append(x)
	elif x>0:
		s5.append(x)
a=min(s5)
b=max(s4)
ct1=0
ct2=0
for x in range(0,a):
	ct1=ct1+1
for x in range(b,0):
	ct2=ct2+1
if (ct1<ct2):
	print 'The sum that is near to zero:',a
else:
	print 'The sum that is near to zero:',b
