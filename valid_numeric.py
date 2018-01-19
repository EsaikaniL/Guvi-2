ip=input("Enter your string:")
a=0
for x in ip:
	if x.isnumeric():
		a=a+1
if(a==len(ip)):
	print("Yes")
else:
	print("No")
