num1=int(input('Enter the binary:\n'))
num=[int(i) for i in str(num1)]
s=len(num)
st=[]
sum=0
for x in num:
	a=1
	for y in range(0,s-1):
		if(x==1):
			a=a*2
	if(x==1):
		st.append(a)
	s=s-1
for x in st:
	sum=sum+x
print 'Decimal equlant is',sum
