s=input("Enter a string and N value:")
st=s.split(" ")[0][::-1]
n=int(s.split(" ")[1])
ans=''
for x in range(n):
	ans=ans+st[x]
print(ans)
