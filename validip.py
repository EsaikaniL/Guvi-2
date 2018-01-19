num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
a=[]
if num1%num2==0 and num1%num1==0:
	a.append(num1)
if num2%num2==0 and num2%num1==0:
	a.append(num2)
print(min(a))
