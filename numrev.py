num=int(input('Enter the number:\n'))
sum=0
while (num>0):
	t=num%10
	sum=sum*10+t
	num=num/10
print sum
