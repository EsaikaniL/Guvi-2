num=int(input("Enter any number"))
ans=""
for x in range(1,num+1):
	if num%x==0:
		ans=ans+" "+str(x)
print(ans)
