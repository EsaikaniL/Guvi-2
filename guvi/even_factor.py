num=int(input("Enter the number:"))
ans=''
flag=0
for x in range(1,num+1):
	if num%x==x%2==0:
		ans=ans+' '+str(x)
		flag=1
if(flag==1):
	print(ans)
else:
	print("No even factor for this number")
