p=int(input("Enterthe perimeter:"))
a=int(input("Enter the area:"))
ans=[]
for x in range(1,25):
	for y in range(1,25):
		k=2*x+2*y
		if k==p:
			ans.append(x*y)
if a in ans:
	print("Yes")
else:
	print("No")
