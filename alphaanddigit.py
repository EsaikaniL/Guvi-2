st=input("Enter the string:")
flag1=0
flag2=0
for x in st:
	if x.isdigit():
		flag1=1
	if x.isalpha():
		flag2=1
if(flag1==1)and (flag2==1):
	print("Yes")
else:
	print("No")
