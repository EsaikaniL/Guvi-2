import random
print 'Find your partner'
s1=raw_input('Enter your name:')
s2=raw_input('Enter yourpartner name:')
t=0
a=len(s1)
b=len(s2)
c=min(a,b)
for x in range(0,c):
	if (s1[x]==s2[x]):
		t=t+1
r=float(t)/c
d=r*100
if (d<25):
	e=random.randint(1, 24)
	f=d+e
	print f,'%'
	print 'You are not well match'
elif (d<50):
	e=random.randint(1,24)
	f=d+e
	print f,'%'
	print 'You think befor commit '
elif (d<75):
	e=random.randint(1,24)
	f=d+e
	print f,'%'
	print 'You are well matched'
else:
	print '100%'
	print 'Congratulations!!!!!!! You will marry soon'
