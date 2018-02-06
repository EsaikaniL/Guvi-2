st1=input("Enter the string1: ")
st2=input("Enter the string2: ")
flag=0
for x in st1:
	for y in st2:
		if x==y:
			flag=1
			break
if flag==1:
	print("Yes")
else:
	print("No")
