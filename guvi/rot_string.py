st=input("Enter the string:")
n=int(input("How many rotation???"))
s=list(st)
ans=''
for x in range(n):
	temp=s[len(s)-1]
	for y in range(len(s)-1,0,-1):
		s[y]=s[y-1]
	s[0]=temp
for x in s:
	ans=ans+x
print(ans)
