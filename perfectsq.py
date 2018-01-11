num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
flag=0
prod=num1*num2
for x in range(1,max(num1,num2)+1):
	k=x*x
	if k==prod:
		flag=1
if (flag==0):
	print("NO")
else:
	print("Yes")
