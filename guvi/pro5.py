n=int(input("Enter N value:"))
a=int(input("Enter A Value:"))
b=int(input("Enter B Value:"))
c=[]
flag=0
if n%2==0:
	for x in range(n//4):
		ans=0
		for y in range(n//4):
			ans=a*x+b*y
			if ans==n//2:
				k1=x
				k2=y
				flag=1
				break
	for s1 in range(k1):
		c.append(a)
	for s2 in range(k2):
		c.append(b)
	print(c,c)
elif(flag==0):
	print("It is not possible to partiate by",a,",",b)
else:
	print("It is not Divided by 2")
