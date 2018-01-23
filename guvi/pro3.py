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
		cost=cost+1
print("Ans:",cost)
