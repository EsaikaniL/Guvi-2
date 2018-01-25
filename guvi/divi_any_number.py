n=int(input("Enter Any value:"))
flag=0
for x in range(2,n):
	if n%x==0:
		flag=1
		break
if flag==1:
	print("Yes")
else:
	print("No")
