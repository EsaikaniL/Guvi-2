st1=input("Enter Valid brackets:")
c1=0
c2=0
for x in st1:
	if x=='(':
		c1=c1+1
	elif x==')':
		c2=c2+1
if c1==c2:
	print("Yes")
else:
	print("No")
