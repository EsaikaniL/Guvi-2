st=input("Enter the line")
a=st.split(" ")
st2=input("Enter the string:")
flag=0
for x in a:
	if x==st2:
		flag=1
		break
if  flag==0:
	print("No")
else:
	print("Yes")
