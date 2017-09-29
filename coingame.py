import random
n=int(input('how many coins are there \n'))
s1=0
s2=0
for x in range(0,n,2):
	t2=random.sample([1,2,5,10],1)
	for i in t2:
		t=int(i)
	s1=s1+t
for y in range(1,n,2):
	t2=random.sample([1,2,5,10],1)
	for i in t2:
		t=int(i)
	s2=s2+t
print 'You need amount to win the game is:',max(s1,s2)
