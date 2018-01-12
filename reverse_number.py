num=int(input("Enter any Number:"))
ans=0
while(num!=0):
	t=num%10
	ans=ans*10+t
	num=num//10
print(ans)
