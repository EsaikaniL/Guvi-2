ip=input("Enter string with number:")
ans=''
for x in ip:
	if x.isdigit():
		ans=ans+x
print(ans)
