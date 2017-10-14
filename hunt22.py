s=[]
s1=[]
num=int(input('How many elements?\n'))
for x in range(0,num):
	n=int(input())
	s.append(n)
for x in range(0,num):
	m=1
	for y in range(0,num):
		if x!=y:
			m=m*s[y]
	s1.append(m)
print s1
