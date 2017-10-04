def fun(list):
	s1=[]
	for x in range(0,len(list)):
		if(list[x]==list.index(list[x])):
			s1.append(str(x))
	print 'Ans:\n',','.join(s1)
s=[]
n=int(input('How many elements?\n'))
print 'Enter the elements \n'
for x in range(0,n):
	num=int(input())
	s.append(num)
fun(s)
