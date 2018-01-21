st=input("Enter any String:")
ans=''
for x in st:
	if x.islower():
		ans=ans+x.upper()
	elif x.isupper():
		ans=ans+x.lower()
print(ans)
