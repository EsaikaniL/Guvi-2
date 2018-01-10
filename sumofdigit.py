num=int(input("Enter your number:"))
ans=0
while(num!=0):
	t=num%10
	ans=ans+t
	num=num//10
print("The sum of digit is:",ans)
