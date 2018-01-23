s1=input("Enter the 1st string:")
s2=input("Enter the 2nd string:")
s=list(s1)
flag=0
for x in range(len(s)-1):
	ans=''
	for y in range(x,len(s)):
		ans=ans+s[y]
	if ans==s2:
		flag=1
		break
if flag==1:
	print("Yes")
