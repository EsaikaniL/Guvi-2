st1=input("Enter the string:")
st=list(st1)
for x in range(len(st)):
	if st[x]==' ':
		st[x]=''
ans=''
for x in st:
	ans=ans+x
print(ans.strip())
