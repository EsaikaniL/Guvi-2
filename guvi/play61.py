n=int(input("Enter the N value:"))
l=int(input("Enter the X value:"))
a=[]
flag=0
for x in range(n):
	k=int(input())
	a.append(k)
for x in range(n-1):
	ans=0
	for y in range(x+1,n):
		ans=a[x]+a[y]
		if ans==l:
			flag=1
			break
if flag==1:
	print("Yes")
else:
	print("NO")
