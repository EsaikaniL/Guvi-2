num=int(input("Enter your number:"))
ans=0
while(num!=0):
	temp=num%10
	ans=ans+(temp*temp)
	num=num//10
print("ANS is:",ans)
