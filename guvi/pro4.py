x=input("Enter X String:")
y=input("Enter Y String:")
a=list(x)
b=list(y)
c=[]
cost=0
l1=len(x)
l2=len(y)
if l1!=l2:
	for x in range(l2-l1):
		a.append(" ")
for x in range(max(l1,l2)):
	if a[x]!=b[x]:
		k1=ord(a[x])
		k2=ord(b[x])
		cost=cost+(max(k1,k2)-min(k1,k2))
print(cost)
