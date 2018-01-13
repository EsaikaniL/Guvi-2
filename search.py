n=int(input("Enter N value:"))
k=int(input("Enter K value:"))
print("Enter the Array:")
a=[]
flag=0
for x in range(n):
	k1=int(input())
	a.append(k1)
for x in a:
	if x==k:
		flag=1
if(flag==1):
	print("Yes")
else:
	print("No")
