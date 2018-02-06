st=input("Enter the 1st string")
st2=input("Enter the 2nd string:")
if len(st)!=len(st2):
	print("No")
else:
	flag=0
	for x in range(len(st)):
		if st[x]!=st2[x]:
			flag=1
			break
	if flag==1:
		print("No")
	else:
		print("Yes")
