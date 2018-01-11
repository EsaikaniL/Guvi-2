num=int(input("Enter number:"))
ans=''
while(num!=0):
	t=num%10
	if t%2!=0:
		ans=ans+' '+str(t)
	num=num//10
print("ODD number is",ans[::-1])
