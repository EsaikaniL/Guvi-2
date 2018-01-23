count=int(input("How many Strings???"))
a=[]
print("Enter your Strings:")
for x in range(count):
	t=input()
	a.append(t)
mi=len(a[0])
for x in a:
	if (len(x)<mi):
		mi=len(x)
ans=''		
for x in range(mi):
	for y in range(count):
		flag=0
		if a[0][x]==a[y][x]:
			flag=1
		else:
			flag=0
	if flag==1:
		ans=ans+a[0][x]
print(ans)
